package divesite

import (
	
	"net/http"

	"github.com/gin-gonic/gin"

	db "friendDive/orm"
)

func GetAllDiveSite(c *gin.Context) {
	
	var AllDS []db.DiveSiteBody
	db.Db.Find(&AllDS)
	for _,v := range AllDS{
		TypeToSplit(&v)
	}
	c.JSON(http.StatusOK, gin.H{
		"data": AllDS,
	})
	return
}

