package main

import (
	"context"
	"fmt"
	"friendDive/auth"
	"friendDive/login"
	"friendDive/read"
	Register "friendDive/register"
	"log"
	"net/http"
	"os"
	"os/signal"
	"syscall"
	"time"

	db "friendDive/orm"

	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
	"github.com/joho/godotenv"
)

func main() {
	err := godotenv.Load("local.env")
	if err != nil {
		log.Panicln("consider env var")
	}

	db.InitDB()
	
	r := gin.Default()
	r.GET("/healthz", func(ctx *gin.Context) {
		ctx.Status(200)
	})

	config := cors.DefaultConfig()
	config.AllowOrigins = []string{"http://google.com"}
	r.Use(cors.New(config))

	r.POST("/register", Register.Register)
	r.POST("/login", login.Login)

	protected := r.Group("/users", auth.Protect([]byte(os.Getenv("SIGN"))))
	protected.GET("/readall", read.ReadAll)
	protected.GET("/read/:id",read.ReadId)
	ctx, stop := signal.NotifyContext(context.Background(), syscall.SIGTERM, syscall.SIGINT) //ตัวรับสัญญานว่ามีการสั่งหยุดไหม
	defer stop()

	serverInstant := &http.Server{
		Addr:           ":" + os.Getenv("PORT"),
		Handler:        r,
		ReadTimeout:    10 * time.Second,
		WriteTimeout:   10 * time.Second,
		MaxHeaderBytes: 1 << 20,
	}

	go func() {
		if err := serverInstant.ListenAndServe(); err != nil && err != http.ErrServerClosed {
			log.Fatalf("Listen: %s\n", err)
		}
	}()
	<-ctx.Done()
	stop()
	fmt.Println("Shutting down gracefully, press Ctrl + c again to force")

	timeoutCtx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	if err := serverInstant.Shutdown(timeoutCtx); err != nil {
		fmt.Println(err)
	}
}
