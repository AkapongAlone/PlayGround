package main

func main() {
	
}

func lengthOfLongestSubstring(s string) int {
    if s == "" {return 0}
    var ans []byte
    var maxLen int = 1
    var index,start int
    lenght := len(s)
    for lenght!= 0 {
        if index >= len(s) {break}
        character := s[index]
        if !isInArr(ans,character) {
            ans = append(ans,character)
            index ++
            continue
            }
        if len(ans) > maxLen {maxLen = len(ans)}
        ans = nil
        s = s[start+1:]
        index = 0
        lenght --      
}
    if len(ans) > maxLen {maxLen = len(ans)}
    return maxLen
}

func isInArr(s []byte,sub byte) bool {
    for _,char := range s {
        if char == sub { return true }
    }
    return false
}

