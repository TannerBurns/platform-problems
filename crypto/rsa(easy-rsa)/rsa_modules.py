#!/usr/bin/python
# -*- coding: utf-8 -*-

import gmpy
from Crypto.Util.number import *
import base64

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def extended_gcd(a, b):
    x,y = 0, 1
    lastx, lasty = 1, 0
    while b:
        a, (q, b) = b, divmod(a,b)
        x, lastx = lastx-q*x, x
        y, lasty = lasty-q*y, y
    return (lastx, lasty, a)

#items=[(a1,n1)(a2,n2)(a3,n3)]
# x=a1%n1
# x=a2%n2
return x, n1*n2*n3
#def chinese_remainder_theorem(items):
def crt(items):
    N = 1
    for a, n in items:
        N *= n
    result = 0
    for a, n in items:
        m = N/n
        r, s, d = extended_gcd(n, m)
        if d != 1:
            raise "Input not pairwise co-prime"
        result += a*s*m
    return result % N, N

# given n=P1*P2
r = (P1-1)*(P2-1)
# given e (encryption key)
# e=65537 or 3 or 5 or 7 or 11 etc
d = int(gmpy.invert(e, r).digits()) # (decryption key)
# given cipher text ct
pt = pow(ct, e, n)
# given plain text pt
ct = pow(pt, d, n)

# to get public keys
# openssl rsa -pubin -in bob.rsa.pub -text -noout
# to factorize public keys
# yafu, then factor(N)

keys=[]

e=65537
C1 = base64.b64decode('DK9dt2MTybMqRz/N2RUMq2qauvqFIOnQ89mLjXY=')
C2 = base64.b64decode('AK/WPYsK5ECFsupuW98bCFKYUApgrQ6LTcm3KxY=')
C3 = base64.b64decode('CiLSeTUCCKkyNf8NVnifGKKS2FJ7VnWKnEdygXY=')

C1=bytes_to_long(C1)
#C1=0x0caf5db76313c9b32a473fcdd9150cab6a9abafa8520e9d0f3d98b8d76
N1=0x0d564b978f9d233504958eed8b744373281ed1418b29f1ecfa8093d8cf
#N1=359567260516027240236814314071842368703501656647819140843316303878351L
P1=17963604736595708916714953362445519L
P2=20016431322579245244930631426505729L

r=(P1-1)*(P2-1)
d=int(gmpy.invert(e, r).digits())
#M=pow(C1, d, N1)
#print M
#print my_parse_number(int(M))

keys.append((d,N1))

C2=bytes_to_long(C2)
#C2=0x00afd63d8b0ae44085b2ea6e5bdf1b085298500a60ad0e8b4dc9b72b16
N2=0x0a23370e7d0fb00232164ac6d642840fc54e9202433f927a60eb5adbd9
#N2=273308045849724059815624389388987562744527435578575831038939266472921L
P1=16514150337068782027309734859141427L
P2=16549930833331357120312254608496323L

r=(P1-1)*(P2-1)
d=int(gmpy.invert(e, r).digits())
#M=pow(C2, d, N2)
#print M
#print my_parse_number(int(M))

keys.append((d,N2))

C3=bytes_to_long(C3)
#C3=0x0a22d279350208a93235ff0d56789f18a292d8527b56758a9c47728176
N3=0x0c5b69e1979e541f85dacde2aa14d2722a846f41b3db83e667e3b3d11d
#N3=333146335555060589623326457744716213139646991731493272747695074955549L
P1=19193025210159847056853811703017693L
P2=17357677172158834256725194757225793L

r=(P1-1)*(P2-1)
d=int(gmpy.invert(e, r).digits())
#M=pow(C3, d, N3)
#print M
#print my_parse_number(int(M))

keys.append((d,N3))

print keys

ciphers=[C1, C2, C3]
for c in ciphers:
    for k in keys:
        print c
        print k
        M=pow(c, k[0], k[1])
        print M
        print long_to_bytes(int(M))

exit()


data=[(C1,N1), (C2,N2), (C3,N3)]
print data

x, n = chinese_remainder_theorem(data)

print x
print n

realnum = gmpy.mpz(x).root(17)[0].digits()
print realnum
print long_to_bytes(int(realnum))
