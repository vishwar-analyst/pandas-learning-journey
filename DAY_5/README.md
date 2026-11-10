**LeetCode Problem:** [1757. Recyclable and Low Fat Products](https://leetcode.com/problems/recyclable-and-low-fat-products/)

**Difficulty:** Easy

**Topic:** Pandas – Filtering DataFrame Rows

## Problem Description

Write a solution to find the IDs of products that are both low fat and recyclable.

Return the result as a DataFrame containing only the `product_id` column.

## Input

**Products DataFrame:**

| product_id | low_fats | recyclable |
|---|---|---|
| 0 | Y | N |
| 1 | Y | Y |
| 2 | N | Y |
| 3 | Y | Y |
| 4 | N | N |

## Expected Output

| product_id |
|---|
| 1 |
| 3 |

## Python Solution

```python
import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[
        (products['low_fats'] == 'Y') &
        (products['recyclable'] == 'Y')
    ][['product_id']]
```

## Concepts Learned

- `pd.DataFrame` – Working with DataFrames.
- Column selection using `df['column']`.
- Boolean filtering using conditions.
- `&` operator for combining multiple conditions (AND).
- Selecting specific columns using `[['column']]`.

## Key Learning

Use boolean filtering to select rows that satisfy multiple conditions.

**Time Complexity:** O(n), where n is the number of rows.

**Space Complexity:** O(k), where k is the number of matching rows in the returned DataFrame.

## Result

Accepted – LeetCode

---
