package main

import  ("fmt" 
	"strconv" 
	"strings"
	"sort")

func main (){
	sil := make([]int, 3)
	for {
		var userInput string
		fmt.Println("Please Insert Integer, Pass X to close")
		fmt.Scan(&userInput)
		if strings.ToUpper(userInput) == "X"{break}
		convstr, err := strconv.Atoi(userInput)
		if err != nil {
			fmt.Println("You don't insert the integer")
			continue
		}
		sil = append(sil,convstr)
		sort.Ints(sil)
		fmt.Println(sil)
		
	}
	
}