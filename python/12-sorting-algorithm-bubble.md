# Sorting Algorithms

- Deeply studied
- Solve how to **sort** a **unsorted collection** in **ascending** or **descending** order
- can **reduce complexity** of problems
- Some sorting algorithms:
    - Bubble sort
    - selection sort
    - insertion sort
    - merge sort
    - quick sort

## Bubble sort
- if First value is greater than next value
    - swap them
- if second value is greater than first value
    - no need to swap
- repeat this process until we arrive to the end of the list

## Implementation
- we are doing it with the nested loop

```python
def bubble_sort(my_list):
    list_length = len(my_list)
    for i in range(list_length-1):
        for j in range(list_length-i-1):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list
```

- improved version:
```python
def bubble_sort(my_list):
    list_length = len(my_list)
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(list_length-1):
            if my_list[i] > my_list[i+1]:
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
                is_sorted = False
        list_length -= 1
    return my_list
```

## Time Complexity

- Worst case: $O(n^2)$
- Best case - not improved version: $\Omega(n^2)$
- Best case - improved version: $\Omega(n)$
- Average case: $\Theta(n^2)$
- Doesn't perform well with highly unsorted large lists
- Performes well:
  - large sorted/almost sorted lists
  - small unsorted lists