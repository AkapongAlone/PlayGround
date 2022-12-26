package read

import (
	db "friendDive/orm"
	"net/http"

	"github.com/gin-gonic/gin"
)

func ReadAll(c *gin.Context) {
	var Alluser []db.UserBody
	db.Db.Find(&Alluser)
	c.JSON(http.StatusOK, gin.H{
		"data": Alluser,
	})
	return
}
