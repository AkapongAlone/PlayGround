package orm

import (
	"fmt"
	"os"
	
	"gorm.io/driver/postgres"
	_"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

var Db *gorm.DB
var err error

type UserBody struct {
	gorm.Model
	Username string `json:"username" binding:"required"`
	Password string `json:"password" binding:"required"`
	Fullname string `json:"fullname" `
	Avatar   string `json:"avatar" `
	Skill    string `json:"skill"`
	Token    string `json:"token"`
}

type DiveSiteBody struct {
	gorm.Model
	Name       string `json:"name" binding:"required"`
	DivingType string `json:"divingtype" binding:"required"`
	Level      string `json:"level" binding:"required"`
	Rate       int    `json:"rate" `
	LocationBody
	DiveSiteDetail
	PhotoAlbumsIn []string `gorm:"type:text[]" json:"photos" `
	PhotoAlbumsOut	string
}

type LocationBody struct {
	Country   string
	Province  string
	Latitude  string
	Longitude string
}

type DiveSiteDetail struct {
	Introduction string
	Overview
	HighlightsIn  []string  `gorm:"type:text[]" json:"highlights" `
	HighlightsOut	string
}



type Overview struct {
	MaxDeep     int
	AverageDeep int
	DiveTypeIn   []string  `gorm:"type:text[]" json:"divetype" `
	DiveTypeOut	string
}


type ReportBody struct {
	Reason        string
	SpecifyReason string
}

func InitDB() {

	dsn := os.Getenv("DB_CONN")
	Db, err = gorm.Open(postgres.Open(dsn), &gorm.Config{})
	if err != nil {
		panic("failed to connect database")
	}
	Db.AutoMigrate(&UserBody{})
	Db.AutoMigrate(&DiveSiteBody{})
	fmt.Println("Db connect")

}
