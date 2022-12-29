package divesite

import (
	db "friendDive/orm"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
)

func GetSite(c *gin.Context) {
	var Site db.DiveSiteBody
	idParam := c.Param("id")
	id,err :=strconv.Atoi(idParam)
	if err != nil {
		c.JSON(http.StatusBadRequest,gin.H{
			"error":err.Error(),
		})
	}
	db.Db.First(&Site,id)
	if int(Site.ID) == id {
		c.JSON(http.StatusOK, gin.H{
		"data": Site,
	})
	} else {
		c.JSON(http.StatusOK, gin.H{
			"error":idParam + " id  not found",
		})
	}
	return
}
