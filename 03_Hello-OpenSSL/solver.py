c = int("6794893f3c47247262e95fbed846e1a623fc67b1dd96e13c7f9fc3b880642e42", 16)

# result of `openssl rsa -text <rsa.pem`
n = int("00:e6:dc:a0:a5:26:5d:39:95:0c:7e:e3:b7:a1:31:96:47:87:00:2c:1b:56:ba:2e:54:ce:b4:30:db:ff:09:95:9d".replace(":", ""), 16)
d = int("00:8f:67:e1:8a:75:28:57:ca:94:76:85:f1:dd:79:b6:05:0e:35:05:e7:f9:ed:da:23:e6:de:14:aa:22:d9:78:a9".replace(":", ""), 16)

m = pow(c, d, n)
print(hex(m))
