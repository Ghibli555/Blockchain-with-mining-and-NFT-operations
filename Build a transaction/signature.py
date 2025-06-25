from ecdsa import SigningKey, BadSignatureError, SECP256k1

secret_key = SigningKey.generate( curve = SECP256k1)
print("private key：" + secret_key.to_string().hex())
public_key = secret_key.verifying_key
print("public key：" + public_key.to_string().hex())

doc = "This is the document I want to send."
signature = secret_key.sign(doc.encode('utf-8'))
print("signature：" + signature.hex())

try:
    public_key.verify(signature, doc.encode('utf-8'))
    print("The document is not changed. The signature is valid.")
except BadSignatureError:
    print("The document is changed. The signature is invalid.")