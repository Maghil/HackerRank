def hackerrankInString(s):
    pattern=['h','a','c','k','e','r','r','a','n','k']
    index=0
    while (len(pattern) != 0) and len(s) > index:
        for char in s[index:]:
            index+=1
            if pattern[0] == char:
                pattern.pop(0)
                break
    if len(pattern) == 0:
        return "YES"
    else:
        return "NO"