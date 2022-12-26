package read

import (
	db "friendDive/orm"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
)

func ReadId(c *gin.Context) {
	var User db.UserBody
	idParam := c.Param("id")
	id,err :=strconv.Atoi(idParam)
	if err != nil {
		c.JSON(http.StatusBadRequest,gin.H{
			"error":err.Error(),
		})
	}
	db.Db.First(&User,id)
	if int(User.ID) == id {
		c.JSON(http.StatusOK, gin.H{
		"data": User,
	})
	} else {
		c.JSON(http.StatusOK, gin.H{
			"error":idParam + " id  not found",
		})
	}
	return
}
