## 9.1: Make an HTTP Request

Use `requests` to fetch data from `example.com`.

```plain
import requests
res = requests.get('http://example.com')
print(res.status_code)
```{exec}
