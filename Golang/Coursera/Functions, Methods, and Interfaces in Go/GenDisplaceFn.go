package main

import (
	"fmt"
)

func GenDisplaceFn(a,o_v,o_s float64) func(float64) float64 {
	fn := func (time float64) float64 {
		s := (0.5 * a * time * time) + (o_v * time) + o_s
		return s
	}
	return fn
}

func main (){
	var a,v,s,t float64
	fmt.Println("Insert accurate")
	fmt.Scan(&a)
	fmt.Println("Insert velocity")
	fmt.Scan(&v)
	fmt.Println("Insert origin distant")
	fmt.Scan(&s)
	fn := GenDisplaceFn(a,v,s)
	fmt.Println("Insert time")
	fmt.Scan(&t)
	fmt.Print(" displacement travelled after time = ")
	fmt.Println(fn(t))
}