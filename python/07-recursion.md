# Recursion

## Definition
- Function that calls itself
- Almost all the situations where we use loops
  - substitute the loops using recursion
- Can solve problems that seem very complex at first

## Examples
- Factorial
- $n! = n \cdot (n - 1) \cdot (n - 2) \cdot \ldots \cdot 1$
  $5! = 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 = 120$

**Factorial without recursion**
```python
def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result
```

**Factorial with recursion**
$n! = n \cdot (n - 1)!$

- if we do it like this, we will have a stack overflow (code will run forever):
  ```python
  def factorial(n):
    return n * factorial(n - 1)
  ```
- We need to have a **base case** to stop the recursion
- base case:
  - add a condition to stop the recursion - ensures that our algorithm doesn't execute infinitely
  - **Factorial base case**: $1! = 1$, that is $n = 1$
```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
```
## How recursion works
- Computer uses a **stack** to keep track of the functions
  - **Call stack**:
    - `factorial(5)` starts
    - before `factorial(5)` is finished, it returns to `call stack` and starts `factorial(4)`
    - it will keep track of `factorial(4)` and `factorial(3)` and so on
    - `factorial(1)` finishes and returns `1` and goes back to `call stack`, pops the returned value and starts `factorial(2)`
    - `factorial(2)` finishes and returns `2` and goes back to `call stack`, pops the returned value and starts `factorial(3)`, and so on

## Dynamic programming
- Optimization technique
- Mainly applied to recursion
- Can reduce the complexity of recursive algorithms
- Used for:
  - Any problem that can be divided into smaller subproblems
  - Subproblems overlap
- Solutions of subproblems are stored in a table, avoiding the need to recalculate them
  - Memoization