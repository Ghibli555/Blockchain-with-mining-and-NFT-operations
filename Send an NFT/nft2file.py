import base64

NFT = "（Copy and paste the string content of nft_data here.）"
with open("./sample.jpg", "wb") as f:
    f.write(base64.b64decode(NFT))