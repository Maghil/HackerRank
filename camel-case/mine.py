def camelcase(s):
    words= [char for char in s if ord(char) >= 65 and ord(char) <= 90 ]
    return len(words)+1