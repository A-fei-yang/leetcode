def lengthMaxString(s):
    hashtable=dict()
    n=len(s)
    maxlength=0
    pre=0
    back=0
    for i in range(n):
        if s[i] not in hashtable:
            hashtable[s[i]]=i
            pre = pre + 1
            maxlength=maxlength+1
        else:
            j=hashtable[s[i]]
            back=j+1

            for k in range(back,j+1):
                hashtable.pop(s[k])
            maxlength=max(maxlength,i-j)




