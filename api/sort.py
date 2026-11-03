from http.server import BaseHTTPRequestHandler
import json

def merge_sort(arr):
    """
    Merge Sort (სორტირება შერწყმით) ალგორითმის რეალიზაცია.
    დროითი სირთულე: O(n log n)
    """
    if len(arr) <= 1:
        return list(arr)
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    """
    ორი დახარისხებული მასივის გაერთიანების დამხმარე ფუნქცია.
    """
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    return result

class handler(BaseHTTPRequestHandler):
    """
    Vercel Serverless ფუნქციის დამუშავება.
    """
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {"status": "ok", "service": "Python Merge Sort API"}
        self.wfile.write(json.dumps(response).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        
        try:
            body = json.loads(post_data.decode('utf-8'))
            array = body.get('array', [])
            
            # Merge Sort ალგორითმის გამოძახება
            sorted_array = merge_sort(array)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            result = {
                "original": array,
                "sorted": sorted_array
            }
            self.wfile.write(json.dumps(result).encode('utf-8'))
        except Exception as e:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))