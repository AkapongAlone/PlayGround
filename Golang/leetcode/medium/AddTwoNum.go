package main

import (
	"fmt"
)

type ListNode struct {
	    Val int
	    Next *ListNode
	 }

// func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
// 	var ans *ListNode = &ListNode{Val: 0 ,Next:nil}	
// 	result1 := 0
//     swap1 := 0
//     swap2 := 0
// 	result2 := 0
// 	for  {                      //combine 2,4,3 to 243
// 		if l1 != nil {
// 		result1 = result1*10 + l1.Val
// 		l1 = l1.Next
//         continue
// 		}
// 		break
// 	}
//     for result1 != 0{
//         swap1 = (swap1 * 10) + (result %10)
//         result1 /= 10
//     }
// 	for {                       //combine 5,6,4 to 564
// 		if l2 != nil {
// 		result2 = result2*10 + l2.Val
// 		l2 = l2.Next
//         continue
// 		}
// 		break
// 	}
//     for result2 != 0{
//         swap2 = (swap2 * 10) + (result2 %10)
//         result2 /= 10
//     }
// 	sum := swap1 + swap2    //get sum is 807
// 	ans.Val = sum % 10          //assign first Val to ans
//     ans2 := ans                 //create ans2 to contain all ans series
// 	sum /=10
// 	for sum != 0 {
// 		if ans.Next == nil {ans.Next = &ListNode{Val: 0 ,Next:nil }}
// 		ans.Next.Val = sum % 10                                         //get 807 to 7,0,8
//         ans = ans.Next
// 		sum /=10
// 	}
// 	return ans2
// 	}

func main() {
	arr := []int{1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1}
	var n int64 = 0
	
	for _,v := range arr{
		n = n*10 + int64(v) 
		fmt.Println(n)
	}
}