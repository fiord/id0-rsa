import hashlib
a = hashlib.sha256(b"id0-rsa.pub")
b = hashlib.md5(a.hexdigest().encode("ascii"))
print(b.hexdigest())
