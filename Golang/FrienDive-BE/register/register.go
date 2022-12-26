package register

import (
	"net/http"

	db "friendDive/orm"

	"github.com/gin-gonic/gin"
	"golang.org/x/crypto/bcrypt"
)

func Register(c *gin.Context) { // func Handler ให้ฟังชั่นนี้เป็น method ของ type RegisterHandler ที่จัดการ DB โดยค่าที่รับมาก็อยู่ใน context เพื่อที่จะทำทุกอย่างให้จบในฟังชั่นนี้
	var user db.UserBody
	// handler := NewRegisterHandler(db.Db)
	if err := c.ShouldBindJSON(&user); err != nil { //check Context is ok?
		c.JSON(http.StatusBadRequest, gin.H{
			"error": err.Error(),
		})
		return
	}
	var IsExistUser db.UserBody

	db.Db.Where("Username = ?", user.Username).First(&IsExistUser)
	if IsExistUser.ID > 0 {
		c.JSON(http.StatusBadRequest, gin.H{
			"error": "user Exists",
		})
		return
	}

	encyptPass, _ := bcrypt.GenerateFromPassword([]byte(user.Password), 10)
	user.Password = string(encyptPass)
	createTable := db.Db.Create(&user)        //Input Data to DB
	if err := createTable.Error; err != nil { //Check if error
		c.JSON(http.StatusBadRequest, gin.H{
			"error": err.Error(),
		})
		return
	}
	c.JSON(http.StatusCreated, gin.H{
		"ID":   user.Model.ID,
		"User": user,
	})
}
