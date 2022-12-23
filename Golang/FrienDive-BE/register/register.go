package register

import (
	"net/http"

	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
	"golang.org/x/crypto/bcrypt"
)

type RegisterBody struct {
	gorm.Model
	Username string `json:"username"`
	Password string `json:"password"`
	Fullname string `json:"fullname"`
	Avatar	string	`json:"avatar"`
}

type RegisterHandler struct {
	db	*gorm.DB
}

func NewRegisterHandler(db *gorm.DB) *RegisterHandler{
	return &RegisterHandler{db}  
}

func (re *RegisterHandler) Register(c *gin.Context)  {           // func Handler ให้ฟังชั่นนี้เป็น method ของ type RegisterHandler ที่จัดการ DB โดยค่าที่รับมาก็อยู่ใน context เพื่อที่จะทำทุกอย่างให้จบในฟังชั่นนี้
	var user RegisterBody
	if err := c.ShouldBindJSON(&user); err != nil {      //check Context is ok?
		c.JSON(http.StatusBadRequest, gin.H{
			"error":err.Error(),
		})
		return
	}
	var IsExcitUser RegisterBody
	re.db.Where("username = ?", user.Username).First(&IsExcitUser)
	if IsExcitUser.ID > 0 {
		c.JSON(http.StatusBadRequest,gin.H{
			"error":"user Exists",
		})
		return
	}

	encyptPass,_ := bcrypt.GenerateFromPassword([]byte(user.Password),10)
	user.Password = string(encyptPass)
	createTable := re.db.Create(&user)   //Input Data to DB
	if err := createTable.Error; err != nil {   //Check if error
		c.JSON(http.StatusBadRequest, gin.H{
			"error":err.Error(),
		})
		return
	}
	c.JSON(http.StatusCreated,gin.H{
		"ID":user.Model.ID,
		"User":user,
	})
}