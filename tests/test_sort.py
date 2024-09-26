import unittest
from ..sorts.bubble_sort import bubble
from ..sorts.insertion_sort import insertion_sort
from ..sorts.selection_sort import selection_sort




class TestSorts(unittest.TestCase):
    
    def test_bubble(self):
        l = [7, 4, 8, 6, 2 ,1 ,9, 10, 5, 3, 15]
        ans = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15]
        bubble(l)
        self.assertEqual(l, ans,"The bubble sort is incorrect!")
    
    def test_selection(self):
        l = [7, 4, 8, 6, 2 ,1 ,9, 10, 5, 3, 15]
        ans = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15]
        selection_sort(l)
        self.assertEqual(l, ans,"The selection sort is incorrect!")

    def test_insertion(self):
        l = [7, 4, 8, 6, 2 ,1 ,9, 10, 5, 3, 15]
        ans = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15]
        insertion_sort(l)
        self.assertEqual(l, ans,"The insertion sort is incorrect!")


if __name__ == "__main__":
    unittest.main()