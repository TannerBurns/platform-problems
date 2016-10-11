#!/usr/bin/python
# -*- coding: utf-8 -*-

f=open('encrypted.txt')
ct=f.read()
# remove new line at end
ct=ct[0:len(ct)-1]
ct=ct.decode('hex')
tl=len(ct)

# find the shifting and the max repeating
print '###### find repeating pattern ######'
rpcnt={}
rpmax={}
for shft in range(5,16):
    rpcnt[shft]=0
    rpmax[shft]=''
    rpt=''
    for i in range(0,tl-20):
        if ct[i]==ct[i+shft]:
            rpcnt[shft] += 1
            rpt += ct[i]
        else:
            if len(rpt) > len(rpmax[shft]):
                rpmax[shft] = rpt
            rpt=''
    print shft, rpcnt[shft], rpmax[shft].encode('hex')

# guess key length is 8
keysize=8

# regroup ciper text
ctg={}
for i in range(0,keysize):
    ctg[i]=''
    for j in range(i,tl,keysize):
        ctg[i]+=ct[j]
        
# 1-gram each group
ctgf={}
for i in range(0,keysize):
    ctgf[i]={}
    for c in ctg[i]:
        if c in ctgf[i]:
            ctgf[i][c]+=1
        else:
            ctgf[i][c]=1

# analyze each group
print '###### crack each group ######'
ptg={}
for i in range(0,keysize):
    maxc=''
    maxk=0
    for k in ctgf[i]:
        if ctgf[i][k] > maxk:
            maxk=ctgf[i][k]
            maxc=k
    # assume ' ' is the most frequent char
    xk = ord(maxc) ^ ord(' ')
    ptg[i]=''
    for c in ctg[i]:
        ptg[i] += chr(ord(c)^xk)
    print i, ptg[i]

# put plaintext together
pt=''
for i in range(0,len(ptg[0])):
    for j in range(0,keysize):
        if i<len(ptg[j]):
            pt += ptg[j][i]

print '###### cracked ######'
print pt
