import requests

# The xxx.xxx.xxx.xxx need to replace with your server's IP address.
res = requests.get("http://xxx.xxx.xxx.xxx:8000/transaction_pool")
transactions_dict = res.json()
print(transactions_dict["transactions"])