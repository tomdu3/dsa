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

