import sys
m_key = 4503599627370517
en = 1504170715041707
last = sys.maxsize
m_v = 0
seq = []
i = 0
while True:
    m_v = (m_v + en) % m_key
    if m_v < last:
        last = m_v
        seq.append(last)
        print(last, i, sum(seq))
    i += 1

#for i in range(1, 10):
#    candidate = i * en 
#    mod_c = candidate % m_key
#    div_c = candidate // m_key
#    print(i, candidate, mod_c, div_c)

