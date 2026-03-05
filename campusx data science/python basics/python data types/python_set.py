# sets {1,2,3,4}
# mutable
# sequence doesnot matter
# cant contain mutable data types
# hetrogeneous

# empty set 
set1 = set()

set2 = {1,2,3,4}

# repeated values considered only once
set3 = {1,2,3,4,4,5,5}       # size = 5

set4 = {1,2,3,(1,2,3,4),'hello'}

print(set1,set2,set3,set4, sep = '\n')

# indexing/slicing not posssible

# other way to creat set
s1 = set([1,2,3,4,4,3])
print(s1)

#--------------------------------------------------------------------------------------
# operations

# 1. Basic Set Functions
# | Function      | Explanation                                                            |
# | ------------- | ---------------------------------------------------------------------- |
# | `set()`       | Creates a new set object from an iterable like list, tuple, or string. |
# | `len(set)`    | Returns the total number of elements in the set.                       |
# | `max(set)`    | Returns the largest element in the set.                                |
# | `min(set)`    | Returns the smallest element in the set.                               |
# | `sum(set)`    | Returns the sum of all numeric elements in the set.                    |
# | `sorted(set)` | Returns a sorted list containing set elements.                         |


# 2. Set Modification Functions
# | Function           | Explanation                                                        |
# | ------------------ | ------------------------------------------------------------------ |
# | `add(x)`           | Adds a single element to the set.                                  |
# | `update(iterable)` | Adds multiple elements from another iterable to the set.           |
# | `remove(x)`        | Removes an element; raises an error if the element does not exist. |
# | `discard(x)`       | Removes an element if present; does nothing if it is absent.       |
# | `pop()`            | Removes and returns a random element from the set.                 |
# | `clear()`          | Removes all elements from the set.                                 |
# | `copy()`           | Returns a shallow copy of the set.                                 |

# 3. Set Mathematical Operations
# | Operation            | Function                               | Explanation                                  |                                                                          |
# | -------------------- | -------------------------------------- | -------------------------------------------- | ------------------------------------------------------------------------ |
# | Union                | `A.union(B)` or `A                     | B`                                           | Returns a set containing all elements from both sets without duplicates. |
# | Intersection         | `A.intersection(B)` or `A & B`         | Returns elements common to both sets.        |                                                                          |
# | Difference           | `A.difference(B)` or `A - B`           | Returns elements in A but not in B.          |                                                                          |
# | Symmetric Difference | `A.symmetric_difference(B)` or `A ^ B` | Returns elements in either set but not both. |                                                                          |


# 4. Set Comparison Functions
# | Function       | Explanation                                               |
# | -------------- | --------------------------------------------------------- |
# | `issubset()`   | Checks if one set is completely contained in another set. |
# | `issuperset()` | Checks if a set contains all elements of another set.     |
# | `isdisjoint()` | Returns True if two sets have no common elements.         |

# 5. Update Operations (In-place operations)
# | Function                        | Explanation                                               |
# | ------------------------------- | --------------------------------------------------------- |
# | `intersection_update()`         | Updates the set with elements common to both sets.        |
# | `difference_update()`           | Removes elements found in another set.                    |
# | `symmetric_difference_update()` | Updates the set with elements in either set but not both. |



s1.add(7)
print(s1)

s1.update([1,7,8,9,10])
print(s1)

# del , discard , remove , pop , clear

del(set1)
s1.discard(5)
s1.remove(8)
s1.pop()
s1.clear()



#----------------------------------------------------------------------------------------
# frozen set --> it is immutable type of set
# but you can do all non editing operations
# 2d frozen sets are possible

fs = frozenset([1,2,3,4,56,7,8])


# ----------------------------------------------------------------------------------------

# set comprehension is possible
setn = {i**2 for i in fs if i%2==0}
print(setn)


