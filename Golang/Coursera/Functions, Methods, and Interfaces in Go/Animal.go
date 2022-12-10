package main

import ("fmt"
		"bufio"
		"os"
		"strings"
)

type Animal struct {
	food string
	move string
	sound string
}

func (a *Animal) Eat(){
	fmt.Println(a.food)
}

func (a *Animal) Move(){
	fmt.Println(a.move)
}

func (a *Animal) Speak(){
	fmt.Println(a.sound)
}

func main(){
	scanner := bufio.NewScanner(os.Stdin)
	cow := Animal{food:"grass",move:"walk",sound:"moo"}
	bird := Animal{"worms","fly","peep"}
	snake := Animal{"mice","slither","hsss"}
	for {
		fmt.Print(">")
		fmt.Println("Insert animal info(name function) or pass X to exit") //Ex Input in format "cow eat"
		scanner.Scan()
		userInput:=scanner.Text()
		if userInput == "X" {break}
		splitInput := strings.Split(userInput," ")
		switch strings.ToLower(splitInput[0]) {
		case "cow":
			switch strings.ToLower(splitInput[1]){
			case "eat" : 
			fmt.Print("I eat ")
			cow.Eat()
			case "speak":
				fmt.Print("I speak ")
				cow.Speak()
			case "move":
				fmt.Print("I move ")
				cow.Move()
			default : fmt.Println("Out of Function")
			}
		case "bird":
			switch strings.ToLower(splitInput[1]){
			case "eat" : 
			fmt.Print("I eat ")
			bird.Eat()
			case "speak":
				fmt.Print("I speak ")
				bird.Speak()
			case "move":
				fmt.Print("I move ")
				bird.Move()
			default : fmt.Println("Out of Function")
			}
		case "snake":
			switch strings.ToLower(splitInput[1]){
			case "eat" : 
			fmt.Print("I eat ")
			snake.Eat()
			case "speak":
				fmt.Print("I speak ")
				snake.Speak()
			case "move":
				fmt.Print("I move ")
				snake.Move()
			default : fmt.Println("Out of Function")
			}
		default : fmt.Println("Out of Name")
		}  
	}
}