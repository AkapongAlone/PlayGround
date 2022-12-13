package main

import("fmt"
		"sort"
)

func main() {
	nums1 := []int{1,2}
	nums2 := []int{1,2}
	fmt.Println(findMedianSortedArrays(nums1,nums2)) 
}
// passed All cases
func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
    newArr := make([]int,len(nums1)+len(nums2))
	newArr = nums1
	newArr = append(newArr, nums2...)
	sort.Ints(newArr)
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

func isOdd(arr []int) bool {
	num:=len(arr)
	if num%2 == 0{
		return false
	}
	return true
}