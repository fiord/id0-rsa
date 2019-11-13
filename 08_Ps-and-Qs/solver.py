import math

# result of `openssl rsa -text -pubin <rsa.pem`
N = int("ACE5E558204976FF266DA8AA43DE450C2DA661A52E725336B7B82CAC77554963B4BCD85A3E31A06F9A1C1A2EC094FB0F27A26E96AC087F1875EAEBE332064CD5", 16)
e = 65537
# result of `openssl rsa -text -pubin <rsa2.pem`
N2 = int("FB2BA70C79E8E4E52AD1805A7DB86E8E47520DF162D9F39D38F55FFF07ABBA4B60D215139ED8C68CABDF34CE38126E7E04CDCDD292D117394E2E33654902910BE9", 16)

c = int("f5ed9da29d8d260f22657e091f34eb930bc42f26f1e023f863ba13bee39071d1ea988ca62b9ad59d4f234fa7d682e22ce3194bbe5b801df3bd976db06b944da", 16)
p = math.gcd(N, N2)
q = N // p

# ed + k(p-1)(q-1) = 1 (k<0)
def ext_gcd(x, y):
    a = [1, 0]
    b = [0, 1]
    while y != 0:
        a = [a[1], a[0] - a[1] * (x // y)]
        b = [b[1], b[0] - b[1] * (x // y)]
        x, y = y, x % y
    return (a[0], b[0], x)

d, _, _ = ext_gcd(e, (p-1) * (q-1))
if d < 0:
    d += (p-1) * (q-1)
print(d)
print(e * d % ((p-1)*(q-1)))
m = pow(c, d, N)
print(hex(m))
