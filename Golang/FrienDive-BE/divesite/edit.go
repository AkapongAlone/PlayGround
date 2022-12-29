package divesite

import (
	db "friendDive/orm"
	"net/http"

	"github.com/gin-gonic/gin"
)

func EditSite(c *gin.Context) {
	var Site db.DiveSiteBody
	if err := c.ShouldBindJSON(&Site); err != nil { //check Context is ok?
		c.JSON(http.StatusBadRequest, gin.H{
			"error": err.Error(),
		})
		return
	}
	id := c.Param("id")

	var beforeEdit db.DiveSiteBody
	db.Db.Where("id = ?", id).First(&beforeEdit)

	db.Db.Model(&beforeEdit).Updates(Site)
	c.JSON(http.StatusOK, gin.H{
		"data": Site,
	})
	return
}
