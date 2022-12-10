package main

import (
	"fmt"
	"time"
)


func run1(){
	for i:=0;i < 100;i++ {
		fmt.Println("run1")
	}
}

func run2()  {
	for i:=0;i < 100;i++ {
		fmt.Println("run2")
	}
}

func main() {
	go run1()   //create go routine
	go run2()   //create go routine
	time.Sleep(1 * time.Second)
	
}

//if run this script you will see it's don't print the same output every time you will see 2 Goroutine are interleaving and can't be predicted that is a race condition


