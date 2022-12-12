package main

func main() {
	
}
// pass All Test Case 90ms(Beats 23.85%) runtime use 6.5 MB (Beats 22.63%)
func lengthOfLongestSubstring(s string) int {
    if s == "" {return 0}
    var ans []byte
    var maxLen int = 1
    var index,start int
    for index != len(s) {
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

