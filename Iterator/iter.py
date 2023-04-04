'''Iterable & Iterator  
Iterable: Any object that can be looped over by using for loop or while loop.

Iterator : Any object that produces the next value in the sequence.
'''

# iterbale
'''When you iterate over the iterable python creates a new iterator object behind the scene, and uses that
iterator to loop over the elements of the iterable'''
my_list = [1, 4, 5, 6, 7, 8, 9]

iterator = iter(my_list)
'''Python calls the __next__ method on the iterator object for getting next element in the sequence'''
item = next(iterator)
print(item)
item = next(iterator)
print(item)
