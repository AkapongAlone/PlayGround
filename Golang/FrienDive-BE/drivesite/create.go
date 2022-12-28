package drivesite

import (
	"net/http"

	db "friendDive/orm"

	"github.com/gin-gonic/gin"
	
)

func Register(c *gin.Context) { // func Handler ให้ฟังชั่นนี้เป็น method ของ type RegisterHandler ที่จัดการ DB โดยค่าที่รับมาก็อยู่ใน context เพื่อที่จะทำทุกอย่างให้จบในฟังชั่นนี้
	var site db.DriveSiteBody
	// handler := NewRegisterHandler(db.Db)
	if err := c.ShouldBindJSON(&site); err != nil { //check Context is ok?
		c.JSON(http.StatusBadRequest, gin.H{
			"error": err.Error(),
		})
		return
	}
	var IsExistName db.DriveSiteBody

	db.Db.Where("Username = ?", site.Name).First(&IsExistName)
	if IsExistName.ID > 0 {
		c.JSON(http.StatusBadRequest, gin.H{
			"error": "name Already Exists",
		})
		return
	}

	
	createTable := db.Db.Create(&site)        //Input Data to DB
	if err := createTable.Error; err != nil { //Check if error
		c.JSON(http.StatusBadRequest, gin.H{
			"error": err.Error(),
		})
		return
	}
	c.JSON(http.StatusCreated, gin.H{
		"ID":   site.Model.ID,
		"User": site,
	})
}
