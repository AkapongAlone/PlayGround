package main

import("fmt"
)

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



// To improve the performance of this code, there are a few things you can try.

// The first thing to try would be to optimize the Sort function. Right now, the function uses two nested loops, which means it has a time complexity of O(n^2) in the worst case. This is not very efficient, especially for large inputs.
// One way to improve the performance of this function would be to use a faster sorting algorithm, such as quicksort or mergesort, which have time complexities of O(n log n) in the average case. These algorithms are much faster than the simple sorting algorithm used in this code, and can handle larger inputs more efficiently.

// Another way to improve the performance of this code would be to use a binary search to find the median of the sorted array, rather than looping through the entire array to find it. This would have a time complexity of O(log n), which is much faster than the O(n) time complexity of the current code.

// Finally, you can also try to optimize the Swap and indexOf functions. These functions are currently not very efficient, as they use multiple loops and calls to len() to find the index of an element in the array. This can be improved by using a map or a hash table to store the indices of each element in the array, which would allow you to look up the index of an element in constant time.

// Overall, there are many ways to improve the performance of this code. By using a faster sorting algorithm, using a binary search to find the median, and optimizing the Swap and indexOf functions, you should be able to make this code run much faster.