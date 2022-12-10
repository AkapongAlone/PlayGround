package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	fmt.Println("Insert 10 integer")
	scanner.Scan()
	userInput := strings.Fields(scanner.Text())
	intUserInput := ConvstrToInt(userInput)
	BubbleSort(intUserInput)
	fmt.Println(intUserInput)
	
}

func ConvstrToInt (sil []string) [] int{
	var silInt []int
	for index := range sil{
		numStr := sil[index]
		number,err := strconv.Atoi(numStr)
		if err != nil {continue}
		silInt = append(silInt, number)
	}
	return silInt
}

func IndexOfSilce(sil []int,str int) int{
	for index, value := range sil{
		if value == str { return index}
	}
	return -1
}

func Swap(sil []int,index int){
	fistVal := sil[index]
	nextVal := sil[index+1] 
	sil[index + 1] = fistVal
	sil[index] = nextVal
}

func BubbleSort(userInput []int)  {
	index := 0
	for index != len(userInput) - 1{
			if userInput[index] > userInput[index +1 ]{
				Swap(userInput,index)
				index = 0
				continue
			}
			index++
		}
	}
	
