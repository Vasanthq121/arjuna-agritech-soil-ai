import requests

try:
    r = requests.get("http://127.0.0.1:8000/docs", timeout=5)
    print("SUCCESS")
    print(r.status_code)
except Exception as e:
    print("FAILED")
    print(e)