package main

import (
	"fmt"
	"sync"
	// "time"
)



type ChopS struct{ sync.Mutex}

type philosopher struct {
	
	eatTimes map[string]int
	 LeftChop , RightChop *ChopS
	 sync.Mutex
	 }

func (p *philosopher)eat(ch chan int,wg *sync.WaitGroup,numPhilo int)  {
		defer wg.Done()
		defer p.Unlock()
		p.Lock()
		<- ch
		if p.eatTimes["remain"]!=0 {
		fmt.Println("start Eating by philo number: ",numPhilo + 1 )
		p.LeftChop.Lock()
		p.RightChop.Lock()
		p.eatTimes["remain"] -= 1
		p.LeftChop.Unlock()
		p.RightChop.Unlock()
		fmt.Println("finish Eating by philo number: ",numPhilo + 1 )
		}
}

func main() {
	var wg sync.WaitGroup
	allow := make(chan int , 2)
	chops := make([]*ChopS,5)
	for i:=0;i<5;i++{
		chops[i] = new(ChopS)
	}
	philo := make([]*philosopher,5)
	for i:=0;i<5;i++{
		philo[i] = &philosopher{eatTimes : map[string]int{"remain":3},LeftChop:chops[i],RightChop :chops[(i+1)%5]} //Each philosopher should eat only 3 times , There should be 5 philosophers sharing chopsticks, with one chopstick between each adjacent pair of philosophers.
	}
	for j:=0;j<15;j++{
		for i:=0;i<5;i++{
			k := (i+1)%5
			wg.Add(2)
			allow <- 1
			go philo[i].eat(allow,&wg,i)   //The host allows no more than 2 philosophers to eat concurrently.
			allow <- 1
			go philo[k].eat(allow,&wg,k)
		}
	}
	wg.Wait()
	
	
	// time.Sleep(1 * time.Second)
}