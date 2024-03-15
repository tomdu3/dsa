# Sorting Algorithms

## Quicksort
- Follows **divide and conquer** principle
- Implemented by many **programming languages**
- **Partition** technique
  - **Pivot**
  - items **smaller** than the pivot $\rightarrow$  left
  - items **greater** than the pivot $\rightarrow$ right
- Elements to the **left** will be sorted recursively
- Elements to the **right** will be sorted recursively

- Hoare's partition
  - Move **left** pointer until a value **greater** than pivot is found
  - Move **right** pointer until a value **smaller** than pivot is found

## Implementation

```python
def quicksort(my_list, first_index, last_index):
    if first_index < last_index:
        partition_index = partition(my_list, first_index, last_index)
        quicksort(my_list, first_index, partition_index - 1)
        quicksort(my_list, partition_index + 1, last_index)


def partition(my_list, first_index, last_index):
    pivot = my_list[first_index]
    left_pointer = first_index + 1
    right_pointer = last_index
    while True:
        while my_list[left_pointer] < pivot and left_pointer < last_index:
            left_pointer += 1

        while my_list[right_pointer] > pivot and right_pointer >= first_index:
            right_pointer -= 1

        if left_pointer > right_pointer:
            break
        else:
            my_list[left_pointer], my_list[right_pointer] = my_list[right_pointer], my_list[left_pointer]

    my_list[first_index], my_list[right_pointer] = my_list[right_pointer], my_list[first_index]
    return right_pointer
```

## Time Complexity

- **Worst Case**: $O(n^2)$
  - Very efficient!
- **Best Case**: $\Omega(n \log n)$
- **Average Case**: $\Theta(n \log n)$
- Space complexity: $O(n \log n)$
