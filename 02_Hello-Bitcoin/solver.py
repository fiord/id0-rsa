from cryptos import *
c = Bitcoin(testnet=False)
priv_key = hex(94176137926187438630526725483965175646602324181311814940191841477114099191175)[2:]
pub_key = c.privtopub(priv_key)
print(c.pubtoaddr(pub_key))
