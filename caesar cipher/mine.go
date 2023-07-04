func caesarCipher(s string, k int32) string {
    var output = ""
    var caesar_ascii rune
    var chr string
    for _,char := range s{
        chr = string(char)
        if(unicode.IsLetter(char)){
            caesar_ascii = char+(k%26)
            if(unicode.IsLower(char)){
                if caesar_ascii > 122{
                    caesar_ascii-=26
                }
            }else{
                if caesar_ascii > 90{
                    caesar_ascii-=26
                }
            }
            chr = string(caesar_ascii)
        }
        output+= chr
    }
    return output