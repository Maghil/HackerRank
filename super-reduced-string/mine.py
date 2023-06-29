def superReducedString(s):
    duplicate_present = True
    while(duplicate_present and len(s)>0):
        starting_character = s[0]
        duplicate_indices_temp = [0]
        duplicate_indices = []
        for i in range(1,len(s)):
            if s[i] == starting_character:
                duplicate_indices_temp.append(i)
            if s[i] != starting_character or i== len(s)-1:
                if len(duplicate_indices_temp) % 2 != 0:
                    duplicate_indices_temp.pop()
                duplicate_indices = duplicate_indices + duplicate_indices_temp
                starting_character=s[i]
                duplicate_indices_temp = [i]
        if len(duplicate_indices) == 0:
            duplicate_present = False
        else:
            for i in reversed(duplicate_indices):
                s = s[:i] + s[i + 1:]
    if len(s) != 0:
        return s
    else:
        return "Empty String"