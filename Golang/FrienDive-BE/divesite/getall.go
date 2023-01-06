package divesite

import (
	"fmt"
	"net/http"

	"github.com/gin-gonic/gin"

	db "friendDive/orm"
)

func GetAllDiveSite(c *gin.Context) {
	
	var AllDS []db.DiveSiteBody
	db.Db.Find(&AllDS)
	for i,v := range AllDS{
		TypeToSplit(&v)
		AllDS[i] = v
		
	}
	fmt.Println(AllDS[0])
	c.JSON(http.StatusOK, gin.H{
		"data": AllDS,
	})
	return
}

