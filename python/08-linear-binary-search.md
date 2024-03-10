# Searching Algorithms

- **searching** is an essential operation in computer science
  - several ways
- Algorithms that search for an element within a collection:
  - **linear search**
  - **binary search**

## Linear search
- looping through each element in a collection
- elements found:
  - algorithm terminates
  - returns the result
- elements not found:
  - algorithm continues

```python
def linear_search(unordered_list, search_value):
    for index in range(len(unordered_list)):
        if unordered_list[index] == search_value:
            return True
    return False

print(linear_search([1, 2, 3, 4, 5], 3)) # True
print(linear_search([1, 2, 3, 4, 5], 6)) # False
```

### Linear search time complexity
- **time complexity**: $O(n)$
  - $n$: number of elements in the collection

## Binary search
- only applied to sorted collections - ordered lists


|2|5|10|12|15|17|20|
|--|--|--|--|--|--|--|

```python
def binary_search(sorted_list, search_value):
    first = 0
    last = len(sorted_list) - 1

    while first <= last:
        middle = (first + last) // 2
        if search_value == sorted_list[middle]:
            return True
        elif search_value <sorted_list[middle]:
            last = middle - 1            
        else:
            first = middle + 1

    return False

print(binary_search([2, 5, 10, 12, 15, 17, 20], 15)) # True
print(binary_search([2, 5, 10, 12, 15, 17, 20], 21)) # False
```

### Binary search time complexity
- **time complexity**: $O(log n)$
  - $n$: number of elements in the collection
