package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"sync"
)

// create each array
func createSubArray(arr []int,size ,start,end int) []int{
	newArr := make([]int,size)
	for i:=0; start < end; start++ {
		newArr[i] = arr[start]
		i++ 
	}
	return newArr
}


// createArray is function to create partition the array into 4 parts and Each partition are approximately equal size
func createArray(splitInput []int) ([4][]int) {
	var arrayOfSlice [4][]int
	numberSize := len(splitInput) / 4
	numberSize2 := len(splitInput) % 4
	start := 0
	end := numberSize
	switch numberSize2{
		case 0 : 
		for i:=0;i<4;i++{
			arrayOfSlice[i] = createSubArray(splitInput,numberSize,start,end)
			start += numberSize
			end += numberSize
		}
		case 1 : 
		for i:=0;i<4;i++{
			if i == 3 {
				arrayOfSlice[i] = createSubArray(splitInput,numberSize+1,start,end+1)
				break
			}
			arrayOfSlice[i] = createSubArray(splitInput,numberSize,start,end)
			end += numberSize
			start += numberSize
		}
		case 2 : 
		for i:=0;i<4;i++{
			if i > 1 {
				end ++
				arrayOfSlice[i] = createSubArray(splitInput,numberSize+1,start,end)
				start += numberSize + 1 
				end += numberSize 
				continue
			}
			arrayOfSlice[i] = createSubArray(splitInput,numberSize,start,end)
			end += numberSize
			start += numberSize
		}
		case 3 : 
		for i:=0;i<4;i++{
			
			if i > 0 {
				end ++
				arrayOfSlice[i] = createSubArray(splitInput,numberSize+1,start,end)
				start += numberSize + 1 
				end += numberSize 
				continue
			}
			arrayOfSlice[i] = createSubArray(splitInput,numberSize,start,end)
			end += numberSize
			start += numberSize
		}
	}
	return arrayOfSlice
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

func Swap(sil []int,index int){
	fistVal := sil[index]
	nextVal := sil[index+1] 
	sil[index + 1] = fistVal
	sil[index] = nextVal
}

func BubbleSort(userInput []int,wg *sync.WaitGroup)  {
	index := 0
	for index != len(userInput) - 1{
			if userInput[index] > userInput[index +1 ]{
				Swap(userInput,index)
				index = 0
				continue
			}
			index++
		}
	wg.Done()
	}

//check if number in array 
func contains(slice []int, item int) bool {
		set := make(map[int]int, len(slice))
		for _, s := range slice {
			set[s] = 0
		}
	
		_, ok := set[item] 
		return ok
}
	
//check if can add num to new array
func canAdd(exceptVal,minVal int,newArr []int,arr ...[]int) bool{
	addNum := false
	for _,value := range arr{
		for _,val2 := range value{
		if contains(newArr,val2){ continue }
		if val2 <= minVal  {
			  minVal = val2
			  addNum = true
		  }
		}
  }
  return addNum
}

//find min and max of user input
func FindMin(arr ...[]int) (int,int) {
	var min,max int
	min = arr[0][0]
	max = arr[0][0]
	for _,value := range arr{
		for _,val2 := range value{
		  if val2 <= min {
			  min = val2
		  }
		  if val2 >= max {max = val2}
		}
  }
  return min,max
}

//Merge all sub array
func MergeArr(arr ...[]int) []int {
	size := 0
	for i := range arr{
		size += len(arr[i])
	}
	newArr := make([]int,size)
	minVal,Max := FindMin(arr...)
	var exceptVal int
	count := 0
	for count <  len(newArr){
		if canAdd(exceptVal,minVal,newArr , arr...) {
			newArr[count] = minVal
			exceptVal = minVal
			count++
		}
		minVal ++
		if minVal > Max {
			newArr = newArr[:count]
			break}
	}
	return newArr
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	fmt.Printf("Please enter the value: ")
	scanner.Scan()
	userInput := scanner.Text()
	splitInput := strings.Split(userInput," ")
	intInput := ConvstrToInt(splitInput)
	Array := createArray(intInput)
	arr1 := Array[0]
	arr2 := Array[1]
	arr3 := Array[2]
	arr4 := Array[3]
	var wg sync.WaitGroup
	fmt.Println("These array will sort")
	fmt.Println(arr1,arr2,arr3,arr4)
	wg.Add(4)
	go BubbleSort(arr1,&wg)
	go BubbleSort(arr2,&wg)
	go BubbleSort(arr3,&wg)
	go BubbleSort(arr4,&wg)
	wg.Wait()
	fmt.Println("sorted sub array")
	fmt.Println(arr1,arr2,arr3,arr4)
	result := MergeArr(arr1,arr2,arr3,arr4)
	fmt.Println("Merge Array that sorted")
	fmt.Println(result)
}

