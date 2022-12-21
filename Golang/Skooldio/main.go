package main

import (
	"context"
	"fmt"
	"log"
	"net/http"
	"os"
	"os/signal"
	"syscall"
	"time"
	"todo/auth"
	"todo/todo"

	"github.com/gin-gonic/gin"
	"github.com/joho/godotenv"
	"golang.org/x/time/rate"
	"gorm.io/driver/mysql"
	// "gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

var (
	buildcommit = "dev"
	buildtime = time.Now().String()
)


func main() {
	// _, err := os.Create("/tmp/live")
	// if err != nil{
	// 	log.Fatal(err)
	// }
	// defer os.Remove("/tmp/live")
	err := godotenv.Load("local.env")
	if err != nil {
		log.Panicln("consider env var")
	}

	dsn := os.Getenv("DB_CONN")
	db, err := gorm.Open(mysql.Open(dsn), &gorm.Config{})
	if err != nil {
		panic("failed to connect database")
	}
	db.AutoMigrate(&todo.Todo{})
	r := gin.Default()
	r.GET("/healthz", func(ctx *gin.Context) {
		ctx.Status(200)
	})

	r.GET("/x", func(ctx *gin.Context) {
		ctx.JSON(200,gin.H{
			"buildcommit" : buildcommit,
			"buildtime" : buildtime,
		})
	})
	r.GET("/limitz",limitHandler)
	handleTodo := todo.NewTodoHandler(db)
	r.GET("/tokenz",auth.AccessToken(os.Getenv("SIGN")))  //Middle Ware and Configuration
	
	protected := r.Group("",auth.Protect([]byte(os.Getenv("SIGN")))) //Middle Ware and Configuration
	protected.POST("/todos",handleTodo.NewTask)
	
	ctx, stop := signal.NotifyContext(context.Background(),syscall.SIGINT,syscall.SIGTERM)
	defer stop()

	s := &http.Server{
		Addr:		":" + os.Getenv("PORT"),
		Handler:	r,
		ReadTimeout:	10 * time.Second,
		WriteTimeout: 10 * time.Second,
		MaxHeaderBytes: 1 << 20,
	}

	go func ()  {
		if err := s.ListenAndServe();err != nil && err != http.ErrServerClosed {
			log.Fatalf("Listen: %s\n", err)
		}
	}()

	<-ctx.Done()
	stop()
	fmt.Println("Shutting down gracefully, press Ctrl + c again to force")

	timeoutCtx,cancel := context.WithTimeout(context.Background(),5 * time.Second)
	defer cancel()

	if err:= s.Shutdown(timeoutCtx); err != nil {
		fmt.Println(err)
	}

	

	
}

var limiter = rate.NewLimiter(5,5)

func limitHandler(c *gin.Context) {
	if !limiter.Allow() {
		c.AbortWithStatus(http.StatusTooManyRequests)
		return
	}
	c.JSON(200,gin.H{
		"message":"pong",
	})
}
