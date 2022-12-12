package main

import (
	"fmt"
)

type ListNode struct {
	Val  int
	Next *ListNode
}
//  pass All Test Case 7ms(Beats 95.69%) runtime use 4.5 MB (Beats 78.9%)
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    var ans *ListNode = &ListNode{Val: 0 ,Next:nil}	
	ans2 := ans 
    var carry int

	for l1 != nil || l2 != nil {
		sum := 0
		if l1 != nil {
			sum += l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			sum += l2.Val
			l2 = l2.Next
		}
		if carry > 0 {
			sum += carry
			ans.Val = sum % 10
            carry = sum / 10
            if l1 == nil && l2 == nil {
                if carry > 0 {ans.Next = &ListNode{Val: carry ,Next:nil }}
			break}
            ans.Next = new(ListNode)
		    ans = ans.Next
            continue
		}
        carry = sum / 10
        ans.Val = sum % 10
		if l1 == nil && l2 == nil {
			if carry > 0 {ans.Next = &ListNode{Val: carry ,Next:nil }}
			break}
		ans.Next = new(ListNode)
		ans = ans.Next
	}
	return ans2	
}




// 1565 / 1568 testcases passed
// func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
//     var ans *ListNode = &ListNode{Val: 0 ,Next:nil}	
    
//     convertToNum := func(ln *ListNode)int {
//         result1 := 0
//         swap1 := 0
//         count := 0
//         countZero := 0
//         for  {                      //combine 2,4,3 to 243
// 		if ln != nil {
// 		result1 = result1*10 + ln.Val
//         if (count == countZero) && (result1*10 + ln.Val == 0) {
//             countZero++
//         }
// 		ln = ln.Next
//         count ++
//         continue
// 		}  
//         count = 0
// 		break
// 	}
//     for result1 != 0{
//         swap1 = (swap1 * 10) + (result1 %10)   //swap to 342
//         result1 /= 10
//     }
//     for countZero > 0{                          //case leading by zero
//         swap1 *= 10
//         countZero --
//     }
//     return swap1
//     }
	
//     // ans.Val = convertToNum(l2)
	
// 	sum := convertToNum(l1) +convertToNum(l2)   //get sum is 807
//     ans.Val = sum % 10          //assign first Val to ans
//     ans2 := ans                 //create ans2 to contain all ans series
// 	sum /=10
// 	for sum != 0 {
// 		if ans.Next == nil {ans.Next = &ListNode{Val: 0 ,Next:nil }}
// 		ans.Next.Val = sum % 10                                         //get 807 to 7,0,8
//         ans = ans.Next
// 		sum /=10
// 	}
// 	return ans2
// }

// func main() {
// 	arr := []int{1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1}
// 	var n int64 = 0

// 	for _, v := range arr {
// 		n = n*10 + int64(v)
// 		fmt.Println(n)
// 	}
// }
