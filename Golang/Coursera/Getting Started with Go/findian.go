package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"unicode"
)

func main() {
	var str string
	fmt.Printf("Please enter string\n")
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	str = scanner.Text()
	fmt.Println(findian(str))
}

func findian(str string) string{
	trimAllSpace := func(r rune) rune {
		if unicode.IsSpace(r) {
			return -1
		}
		return r
	}
	str = strings.Map( trimAllSpace ,str)
	str = strings.ToLower(str)
	if strings.HasPrefix(str,"i") && strings.HasSuffix(str,"n") && strings.ContainsAny(str,"a") {
		return ("Found!")
	}
	return ("Not Found!")
}

