import pandas as pd

transaction = pd.read_pickle("signed_transaction.pkl")
print("This is untampered Transaction：")
print(transaction)
transaction = { "time": transaction["time"], "sender": transaction["sender"], "receiver": transaction["receiver"], "amount": 30 , "signature": transaction["signature"]}
print("This is tampered Transaction：")
print(transaction)
pd.to_pickle(transaction, "signed_transaction.pkl")