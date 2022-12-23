package readall

import (
	"friendDive/register"
	"net/http"

	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
)

type RegisterHandler struct {
	db	*gorm.DB
}

func NewRegisterHandler(db *gorm.DB) *RegisterHandler{
	return &RegisterHandler{db}  
}

func (db *RegisterHandler)ReadAll(c *gin.Context){
	var Alluser	[]register.RegisterBody
	db.db.Find(&Alluser)
	c.JSON(http.StatusOK,gin.H{
		"data":Alluser,
	})
	return
}