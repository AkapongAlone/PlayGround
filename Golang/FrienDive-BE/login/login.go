package login

import (
	"log"
	"net/http"
	"os"

	"friendDive/auth"
	"friendDive/register"
	"github.com/gin-gonic/gin"
	"github.com/joho/godotenv"
	"golang.org/x/crypto/bcrypt"
	"gorm.io/gorm"
)

type LoginBody struct {
	gorm.Model
	Username string `json:"username" binding:"required"`
	Password string `json:"password" binding:"required"`
}

type LoginDbHandler struct {
	db	*gorm.DB
}

func NewLoginHandler(db *gorm.DB) *LoginDbHandler{
	return &LoginDbHandler{db}  
}

func (db *LoginDbHandler)Login (c *gin.Context){
	var login LoginBody
	if err := c.ShouldBindJSON(&login); err != nil {
		c.JSON(http.StatusBadRequest,gin.H{
			"error":err.Error(),
		})
		return
	}

	var HaveUser register.RegisterBody
	db.db.Where("username = ?", login.Username).First(&HaveUser)
	if HaveUser.ID == 0 {
		c.JSON(http.StatusBadRequest,gin.H{
			"error":"user not Exists",
		})
		return
	}
	err := bcrypt.CompareHashAndPassword([]byte(HaveUser.Password),[]byte(login.Password))
	if err == nil {

		err := godotenv.Load("local.env")
		if err != nil {
			log.Panicln("consider env var")
		}
		token,_ := auth.GenToken(os.Getenv("SIGN"))
		c.Request.Header.Add("Authorization", token)
		c.Header("Authorization",token)
		c.JSON(http.StatusOK, gin.H{
			"status":"Success",
		})

	} else {
		c.JSON(http.StatusOK, gin.H{
			"status":"error check username or password",
		})
	}
	return
}