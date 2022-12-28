package login

import (
	"net/http"

	db "friendDive/orm"

	"github.com/gin-contrib/sessions"
	"github.com/gin-gonic/gin"
)

func Logout(c *gin.Context) {
	// Clear the session data
	session := sessions.Default(c)
	CurUser := session.Get("user")
	var user db.UserBody
	db.Db.Where("username = ?", CurUser.(string)).First(&user)
	user.Token = ""
	db.Db.Save(&user)
	session.Clear()
	session.Save()

	// Redirect the user to the login page
	c.Redirect(http.StatusFound, "/login")
}
