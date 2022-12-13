package main

import("fmt")

func main() {
	nums1 := []int{1,3,4,5,6,7,8}
	nums2 := []int{2}
	fmt.Println(findMedianSortedArrays(nums1,nums2)) 
}
// 2072 / 2094 testcases passed
func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
    newArr := make([]int,len(nums1)+len(nums2))
	newArr = nums1
	newArr = append(newArr, nums2...)
	sortArr(newArr)
	if isOdd(newArr) {
		index := len(newArr)/2
		return float64(newArr[index])
	}
	index := len(newArr)/2
	num1 := newArr[index-1]
	num2 := newArr[index] 
	fmt.Println(num1,num2)
	ans := (float64(num1)+float64(num2) )/2
	return ans
     
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