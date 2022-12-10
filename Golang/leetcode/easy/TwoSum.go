package main

import ("fmt")

func twoSum(nums []int, target int) []int {
    aws := make([]int,2)
    for index,value := range nums{
        for index2,value2 := range nums{
            if index == index2 {continue}
            if value + value2 == target {
                aws[0] = index
                aws[1]= index2
                return aws
            }
        }
    }
    return aws    
}

func main() {
	nums := []int{2,7,11,15}
	aws := twoSum(nums,9)
	fmt.Println(aws)
}