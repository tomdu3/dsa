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

## Insertion sort
- 
[Insertion sort](https://en.wikipedia.org/wiki/Insertion_sort)
- First we compare first and second element. If first is greater than second we shift the first element to the right and insert second element before the first one.
- Then we compare second and third element. If second is smaller than third we leave both as they are and go on. If third is greater than fourth we shift the third element to the right and insert fourth element before the third one. Then we compare second and fourth and if fourth is smaller, we shift the second element to the right and insert fourth element before the second one. and so on.

## Implementation

```python
def insertion_sort(my_list):
    for i in ragne(1, len(my_list)):
        number_to_order = my_list[i]
        j = i - 1
        while j >= 0 and number_to_order < my_list[j]:
            my_list[j+1] = my_list[j]
            j -= 1
        my_list[j+1] = number_to_order
    return my_list
```

## Time Complexity

- Worst case: $O(n^2)$
- Best case: $\Omega(n)$
- Average case: $\Theta(n^2)$
