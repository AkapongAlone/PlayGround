package orm

import (
	"fmt"

	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

var Db *gorm.DB
var err error

type UserBody struct {
	gorm.Model
	Username string `json:"username" binding:"required"`
	Password string `json:"password" binding:"required"`
	Fullname string `json:"fullname" binding:"required"`
	Avatar   string `json:"avatar" binding:"required"`
}


func InitDB() {
	
	// dsn := os.Getenv("DB_CONN")
	Db, err = gorm.Open(sqlite.Open("testDB"), &gorm.Config{})
	if err != nil {
		panic("failed to connect database")
	}
	Db.AutoMigrate(&UserBody{})
	fmt.Println("Db connect",)
	
}
