# Sorting algorithms

## Selection sort
- Select the smallest value
- Swap it with the first value
- Repeat this process until we arrive to the end of the list
[Selection sort](https://en.wikipedia.org/wiki/Selection_sort)

## Implementation

```python
def selection_sort(my_list):
    list_length = len(my_list)
    for i in range(list_length-1):
        lowest = my_list[i]
        lowest_index = i
        for j in range(i+1, list_length):
            if my_list[j] < lowest:
                lowest = my_list[j]
                lowest_index = j
        my_list[i], my_list[lowest_index] = my_list[lowest_index], my_list[i]
    return my_list
```

## Time Complexity

- Worst case: $O(n^2)$
- Best case: $\Omega(n^2)$
- Average case: $\Theta(n^2)$


