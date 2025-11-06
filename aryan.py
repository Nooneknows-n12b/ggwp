s='aggsbaa'
freq={}
for ch in s:
    freq[ch]=freq.get(ch,0)+1
res=''
while (len(freq))!=0:
    max=0
    max_ch=''
    for ch in freq:
        if (freq[ch]>max):
            max=freq[ch]
            max_ch=ch
    res=res+(max_ch*max)
    del freq[max_ch]


print(res)