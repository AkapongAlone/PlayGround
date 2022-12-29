package divesite

import (
	
	"net/http"

	"github.com/gin-gonic/gin"

	db "friendDive/orm"
)



// func Createdivesite

func GetAllDiveSite(c *gin.Context) {
	
	var AllDS []db.DiveSiteBody
	db.Db.Find(&AllDS)
	c.JSON(http.StatusOK, gin.H{
		"data": AllDS,
	})
	return
}