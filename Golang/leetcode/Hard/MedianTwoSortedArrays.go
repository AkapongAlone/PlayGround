package main

import("fmt")

func main() {
	nums1 := []int{1,2}
	nums2 := []int{1,2}
	fmt.Println(findMedianSortedArrays(nums1,nums2)) 
}
// 2083 / 2094 testcases passed
func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
    newArr := make([]int,len(nums1)+len(nums2))
	newArr = nums1
	newArr = append(newArr, nums2...)
	Sort(newArr)
	if isOdd(newArr) {
		index := len(newArr)/2
		return float64(newArr[index])
	}
	index := len(newArr)/2
	num1 := newArr[index-1]
	num2 := newArr[index] 
	// fmt.Println(num1,num2,newArr)
	ans := (float64(num1)+float64(num2) )/2
	return ans
     
}

func Swap(index,target int,arr []int) {
	// fmt.Println(arr[index],arr[target])
	start := arr[index]
	arr[index] = arr[target]
	arr[target] = start
}

func Sort(arr []int) {
	fmt.Println(arr)
	for index,val := range arr{
		for index2,val2 := range arr{
			
			if index >= index2 {continue}
			if val > val2 {
				Swap(indexOf(val,arr,index),indexOf(val2,arr,index2),arr)}
				fmt.Println(arr)
		}
	}
}
func indexOf(element int, data []int,start int) (int) {
	for start <= len(data) {
		v := data[start]
		if element == v {
			return start
		}
		start ++
	}
	return -1    //not found.
 }
func sortArr(arr []int) {
	count := 0
	for count < len(arr) -1{
		fmt.Println(count)
		if arr[count] > arr[count+1]{
			start := arr[count+1]
			arr[count+1] = arr[count]
			arr[count] = start
			count = 0
			continue
		}
		count ++
	}
	fmt.Println(arr)
}

func isOdd(arr []int) bool {
	num:=len(arr)
	if num%2 == 0{
		return false
	}
	return true
}