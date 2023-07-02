type void struct{}
var member void

func pangrams(s string) string {
    s = strings.ToLower(s)

    alphabets := make(map[rune]void)
    for _, char := range s{
        if char >= 'a' && char <= 'z' {
            alphabets[char] = member
        }
    }
    if len(alphabets) == 26{
        return "pangram"
    }else{
        return "not pangram"
    }
}