#284
#medium

#Design an iterator that supports the peek operation on an existing iterator in addition to the hasNext and the next operations.

#Implement the PeekingIterator class:

#PeekingIterator(Iterator<int> nums) Initializes the object with the given integer iterator iterator.
#int next() Returns the next element in the array and moves the pointer to the next element.
#boolean hasNext() Returns true if there are still elements in the array.
#int peek() Returns the next element in the array without moving the pointer.
#Note: Each language may have a different implementation of the constructor and Iterator, but they all support the int next() and boolean hasNext() functions.



#correct python3 solution (could not solve):




# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.right = self.iterator.next() #caching next value
        print(self.right)
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.right
        

    def next(self):
        """
        :rtype: int
        """
        res = self.right
        print(res)
        if self.iterator.hasNext():
            self.right = self.iterator.next()
        else:
            self.right = None
        return res


        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.right != None
