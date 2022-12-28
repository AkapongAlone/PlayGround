package drivesite

import (
	db "friendDive/orm"
	"net/http"

	"github.com/gin-gonic/gin"
)

func ReadId(c *gin.Context) {
	var Site db.DriveSiteBody
	name := c.Param("name")
	db.Db.First(&Site, name)
	if (Site.Name) == name {
		c.JSON(http.StatusOK, gin.H{
			"data": Site,
		})
	} else {
		c.JSON(http.StatusOK, gin.H{
			"error": name + " id  not found",
		})
	}
	return
}
