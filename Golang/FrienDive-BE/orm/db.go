package orm

import (
	"fmt"
	_ "os"

	// "gorm.io/driver/postgres"
	"gorm.io/driver/sqlite"
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
	DivingType string `json:"diveType" binding:"required"`
	Level      string `json:"level" binding:"required"`
	CreateAt   string `json:"created" binding:"required"`
	LastUpdate string `json:"latest" `
	Rate       int    `json:"username" `
	LocationBody
	DiveSiteDetail
	PhotoAlbums []string `gorm:"type:text[]" json:"photos" `
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
	Highlights  []string  `gorm:"type:text[]" json:"highlights" `
}

type Check int

type Overview struct {
	MaxDeep     int
	AverageDeep int
	// DriveType   []int
}

const (
	ScubaDivingOpenWater Check = iota
	ScubaDivingAdvance
	TechnicalDiving
	FreedivingBasic
	FreedivingAdvance
	Snorkeling
	Skindiving
)

func (s Check) String() string {
	switch s {
	case ScubaDivingOpenWater:
		return "ScubaDivingOpenWater"
	case ScubaDivingAdvance:
		return "ScubaDivingAdvance"
	case TechnicalDiving:
		return "TechnicalDiving"
	case FreedivingBasic:
		return "FreedivingBasic"
	case FreedivingAdvance:
		return "FreedivingAdvance"
	case Snorkeling:
		return "Snorkeling"
	case Skindiving:
		return "Skindiving"
	}
	return "unknown"
}



type ReportBody struct {
	Reason        string
	SpecifyReason string
}

func InitDB() {

	// dsn := os.Getenv("DB_CONN")
	Db, err = gorm.Open(sqlite.Open("testDB"), &gorm.Config{})
	if err != nil {
		panic("failed to connect database")
	}
	Db.AutoMigrate(&UserBody{})
	Db.AutoMigrate(&DiveSiteBody{})
	fmt.Println("Db connect")

}
