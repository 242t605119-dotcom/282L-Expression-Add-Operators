# LeetCode 282 - Expression Add Operators

## Problem Statement

Given a string `num` that contains only digits and an integer `target`, return all possible expressions by inserting the operators `+`, `-`, and `*` between the digits so that the resulting expression evaluates to `target`.

The digits in the original string must remain in the same order.

Numbers with leading zeros are not allowed.

### Example

```text
Input:
num = "123"
target = 6

Output:
["1+2+3", "1*2*3"]
```

### Explanation

Both expressions evaluate to `6`:

```text
1 + 2 + 3 = 6
1 * 2 * 3 = 6
```

---

## Approach

We use **Backtracking** to try all possible ways of inserting the operators.

At every position, we can:

* Choose `+`
* Choose `-`
* Choose `*`
* Choose multiple digits together to form a number

For multiplication, we need to keep track of the previous number so that operator precedence is handled correctly.

For example:

```text
1 + 2 * 3
```

should be evaluated as:

```text
1 + (2 * 3) = 7
```

not:

```text
(1 + 2) * 3 = 9
```

Therefore, when multiplication is used, we remove the previous value and add the multiplied value.

---

## Algorithm

1. Create an empty result list.
2. Start backtracking from index `0`.
3. Choose one or more digits to form the current number.
4. Avoid numbers with leading zeros.
5. If it is the first number:

   * Start the expression with the number.
6. Otherwise, try:

   * Addition `+`
   * Subtraction `-`
   * Multiplication `*`
7. Keep track of:

   * Current calculated value
   * Previous number
8. When all digits are used:

   * If the calculated value equals the target, add the expression to the result.
9. Return all valid expressions.

---

## Example Walkthrough

```text
num = "123"
target = 6
```

Possible expressions include:

```text
1+2+3 = 6
1-2+3 = 2
1*2*3 = 6
12-3 = 9
123 = 123
```

The expressions that equal the target are:

```text
1+2+3
1*2*3
```

Therefore:

```text
Output:
["1+2+3", "1*2*3"]
```

---

## Leading Zero Condition

Numbers such as:

```text
05
```

are not valid.

Therefore, if the current number starts with `0`, we stop considering longer numbers beginning with that zero.

For example:

```text
num = "105"
```

We can use:

```text
1
10
5
```

but not:

```text
05
```

---

## Handling Multiplication

Multiplication has higher precedence than addition and subtraction.

Suppose:

```text
1 + 2
```

Current value:

```text
3
```

If we add `*3`, we should calculate:

```text
1 + (2 * 3)
```

So instead of:

```text
3 * 3
```

we calculate:

```text
3 - 2 + (2 * 3)
```

which gives:

```text
7
```

This is why the previous number is stored.

---

## Time Complexity

There can be many possible expressions because every position can have different operator choices.

The approximate time complexity is:

```text
O(4^n)
```

where `n` is the length of the input string.

The exact complexity depends on the number of possible partitions and operator combinations.

---

## Space Complexity

The recursion depth can be at most `O(n)`.

The result list can contain many valid expressions.

Therefore, auxiliary recursion space is:

```text
O(n)
```

excluding the space required to store the output.

---

## Key Concept

The main concepts used are:

* Backtracking
* Recursion
* String manipulation
* Operator precedence
* Leading-zero handling

---

## Language

Python

## LeetCode Problem

282 - Expression Add Operators

## Author

T. Nandhini
