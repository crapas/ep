import math

def dupdigit(n):
    n_str = str(n)
    n_len = len(n_str)
    for c in n_str:
        if n_len - 1 != len(n_str.replace(c, '')):
            return True
    return False

def is_palindromic(w):
    if w == w[::-1]:
        return True

def is_anagram(w1, w2):
    c1 = [c for c in w1]
    c2 = [c for c in w2]
    if sorted(c1) == sorted(c2):
        return True
    else:
        return False

with open("words.txt", "r") as rp:
    words = rp.read().strip().replace('"', '').split(',')
#print(words)

word_by_len = {}
for word in words:
    w_len = len(word)
    if w_len in word_by_len:
        word_by_len[w_len].append(word)
    else:
        word_by_len[w_len] = [word]
    


anagrams = []

for k, v in word_by_len.items():
    for i in range(len(v)):
        for j in range(i + 1, len(v)):
            if is_anagram(v[i], v[j]):
                #print(v[i], v[j])
                anagrams.append((v[i], v[j]))

#print(len(anagrams))

keys = word_by_len.keys()
max_digit = max(keys)    
print(max_digit)

max_digit = 9

anagrams_by_len = {}
for anagram in anagrams:
    anagram_len = len(anagram[0])
    if anagram_len in anagrams_by_len:
        anagrams_by_len[anagram_len].append(anagram)
    else:
        anagrams_by_len[anagram_len] = [anagram]

for k, v in anagrams_by_len.items():
    print(k, len(v))

#print(anagrams_by_len[9])

#CDEINORTU
#INTRODUCE
#REDUCTION

i = 1
sn_list = []
while True:
    sn = i ** 2
    sn_len = math.ceil(math.log10(sn + 1))
    if sn_len > max_digit:
        break
    if sn_len == 9:
        if not dupdigit(sn):
            sn_list.append(sn)
    i += 1

print(len(sn_list))

print(sn_list)
anagram_list = []
for i in range(0, len(sn_list)):
    for j in range(i + 1, len(sn_list)):
        if is_anagram(str(sn_list[i]), str(sn_list[j])):
            anagram_list.append((str(sn_list[i]), str(sn_list[j])))

print(anagram_list)


def compacheck(str1, str2):
    c1_1 = str1[3] + str1[8] + str1[5] + str1[6] + str1[7] + str1[2] + str1[0] + str1[4] + str1[1]
    c1_2 = str1[6] + str1[8] + str1[5] + str1[0] + str1[7] + str1[2] + str1[3] + str1[4] + str1[1]

    if c1_1 == str2 or c1_2 == str2:
        return True
    else:
        return False
#for k, v in sn_by_length.items():
#    print(k, len(v))

maxv = 0
check2 = []
for anagram in anagram_list:
    print(anagram)
    if compacheck(anagram[0], anagram[1]):
        print("OK")
        check2.append(anagram)
        a = int(anagram[0])
        b = int(anagram[1])
        maxv = max(maxv, a, b)

print(maxv)
'''
num_anagrams = []



x = 0
for k, v in sn_by_length.items():
    print("~~~", k)
    if k != 9:
        continue
    print(k)
    for i in range(len(v)):
        for j in range(i + 1, len(v)):
            if is_anagram(str(v[i]), str(v[j])):
                #print(v[i], v[j])
                num_anagrams.append((v[i], v[j]))
                x += 1
                print("ANAGRAM %d Added" % x)

checked = []
for anagram in num_anagrams:
    if dupdigit(anagram[0]):
        continue
    checked.append(anagram)

result = 0
for check in checked:
    if result < max(check[0], check[1]):
        result = max(check[0], check[1])

print("result : ", result)
'''