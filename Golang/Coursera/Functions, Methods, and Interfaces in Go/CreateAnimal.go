package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type Animal interface {
	Eat()
	Move()
	Speak()
}

type Cow struct{
	eat,move,sound string
}

type Bird struct{
	eat,move,sound string
}

type Snake struct{
	eat,move,sound string
}
func (cow *Cow)Eat(){
	fmt.Println("I eat grass")
}

func (bird *Bird)Eat(){
	fmt.Println("I eat worms")
}

func (snake *Snake)Eat(){
	fmt.Println("I eat mice")
}

func (cow *Cow) Move(){
	fmt.Println("I move walk")
}

func (snake *Snake) Move(){
	fmt.Println("I move slither")
}

func (bird *Bird) Move(){
	fmt.Println("I move fly")
}
func (cow *Cow) Speak(){
	fmt.Println("I speak moo")
}
func (bird *Bird) Speak(){
	fmt.Println("I speak peep")
}
func (snake *Snake) Speak(){
	fmt.Println("I speak hass")
}

func callAnimal(animal Animal,info string) {
		switch strings.ToLower(info){
			case "eat" : 
			animal.Eat()
			case "speak":
				animal.Speak()
			case "move":
				animal.Move()
			default : fmt.Println("Out of Function")
	}

}

func main(){
	
	var cow,bird,snake Animal
	var cow1 *Cow
	var bird1 *Bird
	var snake1 *Snake

	cow = cow1
	bird = bird1
	snake = snake1
	scanner := bufio.NewScanner(os.Stdin)
	allAnimal := map[string]string{"cow":"cow", "bird":"bird", "snake":"snake"}
	for {
		fmt.Print(">")
		fmt.Println("Insert newanimal or query or pass X to exit") //Ex Input in format "newanimal dog cow","query bird eat"
		scanner.Scan()
		userInput:=scanner.Text()
		splitInput := strings.Split(userInput," ")
		switch splitInput[0]{
		case "X":break
		case "newanimal":
			allAnimal[splitInput[1]] = splitInput[2]
			fmt.Println("Create New Animal!!")
		case "query":
			typeAni,ok := allAnimal[splitInput[1]]
			if ok {
				info := splitInput[2]
				switch typeAni{
				case "cow":
					callAnimal(cow,info)
				case "bird":
					callAnimal(bird,info)
				case "snake":
					callAnimal(snake,info)
				}
			} else {fmt.Println("Not found animal's name")}
			
		} }
}