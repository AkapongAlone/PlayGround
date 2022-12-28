package drivesite

import (
	
	"net/http"

	"github.com/gin-gonic/gin"

	db "friendDive/orm"
)



// func CreateDriveSite

func GetAllDiveSite(c *gin.Context) {
	
	var AllDS []db.DriveSiteBody
	db.Db.Find(&AllDS)
	c.JSON(http.StatusOK, gin.H{
		"data": AllDS,
	})
	return
}