package main

import ("fmt"
	"bufio"
	"os"
	"encoding/json"
)

type Map map[string] string

func main()  {
	scanner := bufio.NewScanner(os.Stdin)
	fmt.Println("insert Your name")
	scanner.Scan()
	name := scanner.Text()
	fmt.Println("insert Your email")
	scanner.Scan()
	email := scanner.Text()
	data := Map{"name":name,"email":email}
	dataJson,err := json.Marshal(data)
	if err == nil {
		fmt.Println(string(dataJson))
	} else {
		fmt.Println(err)
	}
}
