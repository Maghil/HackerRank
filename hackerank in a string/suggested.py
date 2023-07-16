def hackerrankInString(s):
    hr = 'hackerrank'
    j = 0
    for i in s:
        if i == hr[j] :
            j += 1
        if j == len(hr) :
            break
    return 'YES' if j==len(hr) else 'NO'