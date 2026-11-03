async function sortArray() {
    const inputElement = document.getElementById('arrayInput');
    const btn = document.getElementById('sortBtn');
    const input = inputElement.value;
    
    // სტრიქონიდან რიცხვების პარსირება
    const numbers = input.split(',')
                         .map(n => parseFloat(n.trim()))
                         .filter(n => !isNaN(n));

    if (numbers.length === 0) {
        alert('გთხოვთ, შეიყვანოთ სწორი რიცხვები მძიმით გამოყოფილი!');
        return;
    }

    // ჩატვირთვის სტატუსის ჩართვა
    btn.disabled = true;

    try {
        // მოთხოვნის გაგზავნა Python სერვერზე 
        const response = await fetch('/api/sort', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ array: numbers })
        });

        if (!response.ok) {
            throw new Error('სერვერის შეცდომა');
        }
        
        const data = await response.json();
        
        // შედეგების გამოტანა ეკრანზე
        document.getElementById('originalArray').innerText = JSON.stringify(data.original);
        document.getElementById('sortedArray').innerText = JSON.stringify(data.sorted);
    } catch (err) {
        // შეცდომის დამუშავება სერვერთან კავშირის პრობლემისას
        console.error('სერვერის შეცდომა:', err);
        alert('შეცდომა სერვერთან დაკავშირებისას: ' + err.message);
    } finally {
        btn.disabled = false;
    }
}