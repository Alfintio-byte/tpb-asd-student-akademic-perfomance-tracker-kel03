from src.data_structures.sorting import bubble_sort

def test_sorting():

    data = [3, 1, 2]

    hasil = bubble_sort(data)

    assert hasil == [1, 2, 3]