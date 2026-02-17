# Python Assignment Operators Reference Guide

## Table of Contents
1. [Basic Assignment](#basic-assignment)
2. [Arithmetic Assignment Operators](#arithmetic-assignment-operators)
3. [Comparison with Regular Operators](#comparison-with-regular-operators)
4. [Practical Examples](#practical-examples)

---

## Basic Assignment

### `=` (Assignment)
**Description:** Assigns a value to a variable.

**Syntax:** `variable = value`

**Example:**
```python
x = 10
name = "Peter"
price = 99.99
```

---

## Arithmetic Assignment Operators

These operators combine arithmetic operations with assignment.

### `+=` (Add and Assign)
**Description:** Adds the right value to the variable and assigns the result back to the variable.

**Syntax:** `x += y` is equivalent to `x = x + y`

**Example:**
```python
score = 10
score += 5      # score is now 15
score += 3      # score is now 18
```

---

### `-=` (Subtract and Assign)
**Description:** Subtracts the right value from the variable and assigns the result back.

**Syntax:** `x -= y` is equivalent to `x = x - y`

**Example:**
```python
lives = 3
lives -= 1      # lives is now 2
lives -= 1      # lives is now 1
```

---

### `*=` (Multiply and Assign)
**Description:** Multiplies the variable by the right value and assigns the result back.

**Syntax:** `x *= y` is equivalent to `x = x * y`

**Example:**
```python
points = 10
points *= 2     # points is now 20
points *= 3     # points is now 60
```

---

### `/=` (Divide and Assign)
**Description:** Divides the variable by the right value and assigns the result back.

**Syntax:** `x /= y` is equivalent to `x = x / y`

**Example:**
```python
total = 100
total /= 2      # total is now 50.0
total /= 5      # total is now 10.0
```

**Note:** Always results in a float, even if the numbers divide evenly.

---

### `//=` (Floor Divide and Assign)
**Description:** Divides the variable by the right value (rounding down) and assigns the result back.

**Syntax:** `x //= y` is equivalent to `x = x // y`

**Example:**
```python
items = 17
items //= 5     # items is now 3 (17 ÷ 5 = 3 remainder 2)
items //= 2     # items is now 1 (3 ÷ 2 = 1 remainder 1)
```

**Use Case:** When you need whole numbers only (e.g., counting groups).

---

### `%=` (Modulus and Assign)
**Description:** Gets the remainder of division and assigns it back to the variable.

**Syntax:** `x %= y` is equivalent to `x = x % y`

**Example:**
```python
remainder = 17
remainder %= 5  # remainder is now 2 (17 ÷ 5 = 3 remainder 2)
remainder %= 2  # remainder is now 0 (2 ÷ 2 = 1 remainder 0)
```

**Use Case:** Check if a number is even/odd, or find leftover items.

---

### `**=` (Exponent and Assign)
**Description:** Raises the variable to the power of the right value and assigns the result back.

**Syntax:** `x **= y` is equivalent to `x = x ** y`

**Example:**
```python
base = 2
base **= 3      # base is now 8 (2³ = 8)
base **= 2      # base is now 64 (8² = 64)
```

**Use Case:** Calculating powers, areas, volumes, compound interest.

---

## Comparison with Regular Operators

| Long Form | Short Form (Assignment Operator) |
|-----------|----------------------------------|
| `x = x + 5` | `x += 5` |
| `x = x - 3` | `x -= 3` |
| `x = x * 2` | `x *= 2` |
| `x = x / 4` | `x /= 4` |
| `x = x // 2` | `x //= 2` |
| `x = x % 3` | `x %= 3` |
| `x = x ** 2` | `x **= 2` |

**Why use assignment operators?**
- More concise and readable
- Less typing
- Reduces chance of typos
- Industry standard practice

---

## Practical Examples

### Example 1: Shopping Cart Total
```python
cart_total = 0
cart_total += 29.99    # Add item 1
cart_total += 15.50    # Add item 2
cart_total += 8.25     # Add item 3
print(f"Total: ${cart_total}")  # Total: $53.74
```

### Example 2: Game Score with Multiplier
```python
score = 100
score *= 2         # Double points power-up
score += 50        # Collect 50 coins
print(f"Score: {score}")  # Score: 250
```

### Example 3: Temperature Conversion
```python
celsius = 25
# Convert to Fahrenheit: F = C × 9/5 + 32
fahrenheit = celsius
fahrenheit *= 9
fahrenheit /= 5
fahrenheit += 32
print(f"{celsius}°C = {fahrenheit}°F")  # 25°C = 77.0°F
```

### Example 4: BMI Calculator
```python
weight = 70        # kg
height = 1.75      # meters
height **= 2       # Square the height
bmi = weight / height
print(f"BMI: {bmi:.2f}")  # BMI: 22.86
```

### Example 5: Check Even or Odd
```python
number = 17
check = number
check %= 2         # Get remainder when divided by 2
if check == 0:
    print("Even")
else:
    print("Odd")   # Odd
```

### Example 6: Splitting Items into Groups
```python
total_items = 25
group_size = 4
groups = total_items // group_size      # 6 groups
leftover = total_items % group_size     # 1 item left
print(f"{groups} groups of {group_size}, with {leftover} leftover")
# Output: 6 groups of 4, with 1 leftover
```

---

## Quick Reference Table

| Operator | Name | What it does | Example | Result |
|----------|------|--------------|---------|--------|
| `=` | Assignment | Assign value | `x = 5` | x is 5 |
| `+=` | Add Assign | Add and assign | `x += 3` (x was 5) | x is 8 |
| `-=` | Subtract Assign | Subtract and assign | `x -= 2` (x was 8) | x is 6 |
| `*=` | Multiply Assign | Multiply and assign | `x *= 3` (x was 6) | x is 18 |
| `/=` | Divide Assign | Divide and assign | `x /= 3` (x was 18) | x is 6.0 |
| `//=` | Floor Divide Assign | Floor divide and assign | `x //= 4` (x was 6) | x is 1 |
| `%=` | Modulus Assign | Get remainder and assign | `x %= 3` (x was 7) | x is 1 |
| `**=` | Exponent Assign | Raise to power and assign | `x **= 3` (x was 2) | x is 8 |

---

## Common Mistakes to Avoid

### Mistake 1: Using == instead of =
```python
# Wrong
x == 5    # This checks if x equals 5, doesn't assign!

# Correct
x = 5     # This assigns 5 to x
```

### Mistake 2: Forgetting the variable is modified
```python
count = 10
count += 5
print(count)  # 15, not 10! The variable was changed.
```

### Mistake 3: Using assignment operators on undefined variables
```python
# Wrong
total += 10   # Error if total doesn't exist yet

# Correct
total = 0     # Initialize first
total += 10   # Now it works
```

---

## Tips for Beginners

1. **Always initialize variables before using assignment operators**
   ```python
   count = 0      # Initialize
   count += 1     # Now safe to use
   ```

2. **Use meaningful variable names**
   ```python
   # Unclear
   x += 5

   # Clear
   total_price += 5
   ```

3. **Assignment operators modify the original variable**
   ```python
   age = 25
   age += 1       # age is now 26 (modified!)
   ```

4. **You can chain operations**
   ```python
   price = 100
   price *= 1.2   # Add 20% markup (now 120)
   price -= 10    # Subtract discount (now 110)
   ```

---

## Summary

Assignment operators are shortcuts that make your code:
- **Shorter** - Less typing
- **Cleaner** - Easier to read
- **Professional** - Industry standard
- **Safer** - Less chance of typos

Instead of writing `total = total + 10`, simply write `total += 10`.

**Most commonly used:**
- `+=` - Adding to counters, totals, scores
- `-=` - Subtracting from lives, inventory
- `*=` - Applying multipliers, scaling values
- `/=` - Dividing quantities, calculating averages

---

**Created for UDEMY Python Course**
**Date:** 2026-02-06
