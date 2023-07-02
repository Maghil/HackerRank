def pangrams(s):
    hash_map=set()
    for i in s:
        if i.isalpha():
            hash_map.add(ord(i.lower()) % 26)
    if len(hash_map) == 26:
        return "pangram"
    return "not pangram"