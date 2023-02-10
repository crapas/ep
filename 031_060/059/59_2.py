eng = list(range(65, 91)) + list(range(97, 123)) + [32, 46]
#eng = set(range(65,91)+range(97,123)+[32,46])
encrypted = [int(x) for x in open('cipher.txt').read().split(',')]
passwd = []
for i in range(3):
    enc3=[x for k,x in enumerate(encrypted) if k%3==i]
    tmpdic = {}
    for pw in range(97,123):
        tmpdic[pw] = len([x^pw for x in enc3 if x^pw in eng])
    passwd.append( max(tmpdic, key=tmpdic.get))

decrypted = [x^passwd[k%3] for k, x in enumerate(encrypted)]
print (passwd)
print (''.join([chr(x) for x in decrypted]))

print (sum(decrypted))
