import hashlib

indata = "Hello World!"
hash = hashlib.sha256(indata.encode('utf-8')).hexdigest()
print(hash)
indata = "Hello World!"
hash = hashlib.sha256(indata.encode('utf-8')).hexdigest()
print(hash)