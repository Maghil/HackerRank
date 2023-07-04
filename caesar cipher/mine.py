def caesarCipher(s, k):
    s=list(s)
    for i in range(len(s)):
        if s[i].isalpha():
            caesar_ascii = ord(s[i])+(k%26)
            if s[i].islower():
                if caesar_ascii > 122:
                    caesar_ascii-=26
            else:
                if caesar_ascii > 90:
                    caesar_ascii-=26
            s[i]=chr(caesar_ascii)
        print("".join(s))
    return ''.join(s)