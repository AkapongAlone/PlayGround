package login

import (
	"net/http"

	db "friendDive/orm"

	_"github.com/gin-contrib/sessions"
	"github.com/gin-gonic/gin"
)

func Logout(c *gin.Context) {
	
	var login LoginBody
	if err := c.ShouldBindJSON(&login); err != nil {
		c.JSON(http.StatusBadRequest,gin.H{
			"error":err.Error(),
		})
		return
	}

	var HaveUser db.UserBody
	db.Db.Where("username = ?", login.Username).First(&HaveUser)

	
	HaveUser.Token = ""
	db.Db.Save(&HaveUser)
	
}
