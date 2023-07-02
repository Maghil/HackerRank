import string

def pangrams(s):
    s=s.lower()
    for i in string.ascii_lowercase:
        if i not in s:
            return "not pangram"
    else:
        return "pangram"