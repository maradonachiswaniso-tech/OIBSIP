# BMI Calculator

## Description
A simple Python program that calculates Body Mass Index (BMI) based on weight and height.

## How to Run
1. Open terminal
2. Navigate to the `Task2_BMI_Calculator` folder
3. Run: `python main.py`

## Features
- Input weight in kilograms
- Input height in meters
- Calculates BMI
- Shows category: Underweight, Normal, Overweight, Obese

## BMI Categories
| Category | BMI Range |
|----------|-----------|
| Underweight | Less than 18.5 |
| Normal | 18.5 - 24.9 |
| Overweight | 25 - 29.9 |
| Obese | 30 and above |

## Example
```python
weight = 70
height = 1.75
bmi = weight / (height ** 2)
print(bmi)
```

Example output:
```text
22.86
```

This falls in the Normal category.
