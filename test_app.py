import pytest
from api.sort import merge_sort

def test_sorting_normal_array():
    """ჩვეულებრივი მასივის სორტირების ტესტირება"""
    assert merge_sort([5, 2, 8, 1, 9]) == [1, 2, 5, 8, 9]

def test_sorting_empty_array():
    """ცარიელი მასივის დამუშავების ტესტირება"""
    assert merge_sort([]) == []

def test_sorting_negative_numbers():
    """უარყოფით რიცხვებთან მუშაობის ტესტირება"""
    assert merge_sort([3, -1, 0, -5, 2]) == [-5, -1, 0, 2, 3]

def test_already_sorted_array():
    """უკვე დახარისხებული მასივის ტესტირება"""
    assert merge_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
