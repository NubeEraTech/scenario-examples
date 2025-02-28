## 7.1: Handle Division by Zero

Use `try-except` to handle division by zero errors.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print('Cannot divide by zero')
```{exec}
