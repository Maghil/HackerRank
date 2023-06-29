def superReducedString(s):
    s=list(s)
    i=0
    while i<len(s)-1:
        if s[i]==s[i+1]:
            s.pop(i)
            s.pop(i)
            i=0
        else:
            i=i+1
    if len(s)==0:
        return("Empty String")
    else:
        return(''.join(s))