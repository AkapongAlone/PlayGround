package main

import (
    "bufio"
    "fmt"
    "log"
    "os"
	"strings"
)

type strField struct {
	kuy []string
}

type Name struct  {
	fname string 
	lname string
}

func main(){
	userScanner := bufio.NewScanner(os.Stdin)
	fmt.Println("Insert path of file")
	userScanner.Scan()
	path := userScanner.Text()
	f, err := os.Open(path)

    if err != nil {
        log.Fatal(err)
    }

    defer f.Close()

    scanner := bufio.NewScanner(f)
	var result []Name
    for scanner.Scan() {
        fullName := (scanner.Text())
		arrFullName := strings.Fields(fullName)
		// Fields splits the string s around each instance of one or more consecutive white space characters,
		//  as defined by unicode.IsSpace, returning a slice of substrings of s or an empty slice if s contains only white space.
		if (len(arrFullName[0])>20 || len(arrFullName[1]) >20 )  {
			fmt.Println("Name too long Skip this line")
			continue}
		name := Name{arrFullName[0],arrFullName[1]}
		result = append(result, name)
    }
	fmt.Println(result)

    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }
}