import requests

r = requests.get("https://api.github.com/users/getfutureproof")

print(r.status_code)
