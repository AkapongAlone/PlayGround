package divesite

import (
	_ "errors"
	"fmt"
	_ "fmt"
	"net/http"
	"strings"

	db "friendDive/orm"

	"github.com/gin-gonic/gin"
)

func CreateSite(c *gin.Context) { // func Handler ให้ฟังชั่นนี้เป็น method ของ type RegisterHandler ที่จัดการ DB โดยค่าที่รับมาก็อยู่ใน context เพื่อที่จะทำทุกอย่างให้จบในฟังชั่นนี้
	var site db.DiveSiteBody
	if err := c.ShouldBindJSON(&site); err != nil { //check Context is ok?
		c.JSON(http.StatusBadRequest, gin.H{
			"error": err.Error(),
		})
		return
	}
	var IsExistName db.DiveSiteBody

	db.Db.Where("Name = ?", site.Name).First(&IsExistName)
	if IsExistName.ID > 0 {
		c.JSON(http.StatusBadRequest, gin.H{
			"error": "name Already Exists",
		})
		return
	}

	if !ValidateEnum(site.DiveTypeIn) {
		c.JSON(http.StatusBadRequest, gin.H{
			"error": "Not found dive type",
		})
		return
	}

	TypeToCombine(&site)

	createTable := db.Db.Create(&site) //Input Data to DB
	fmt.Println(site.DiveTypeIn)
	if err := createTable.Error; err != nil { //Check if error
		c.JSON(http.StatusBadRequest, gin.H{
			"error": err.Error(),
		})
		return
	}
	c.JSON(http.StatusCreated, gin.H{
		"ID":   site.ID,
		"User": site,
	})
}

type Check string

const (
	ScubaDivingOpenWater Check = "scubadivingopenwater"
	ScubaDivingAdvance   Check = "scubadivingadvance"
	TechnicalDiving      Check = "technicaldiving"
	FreedivingBasic      Check = "freedivingbasic"
	FreedivingAdvance    Check = "freedivingadvance"
	Snorkeling           Check = "snorkeling"
	Skindiving           Check = "skindiving"
)

func CheckEnum(s Check) string {
	switch s {
	case ScubaDivingOpenWater:
		return "nil"
	case ScubaDivingAdvance:
		return "nil"
	case TechnicalDiving:
		return "nil"
	case FreedivingBasic:
		return "nil"
	case FreedivingAdvance:
		return "nil"
	case Snorkeling:
		return "nil"
	case Skindiving:
		return "nil"
	}
	return "Not found dive type"
}

func ValidateEnum(payload []string) bool {
	for _, item := range payload {
		str := strings.ToLower(item)
		if err := CheckEnum(Check(str)); err != "nil" {
			return false
		}
	}
	return true
}

func TypeToCombine(context *db.DiveSiteBody) {
	context.Overview.DiveTypeOut = CombineStr(context.Overview.DiveTypeIn)
	context.Overview.DiveTypeIn = nil
	context.DiveSiteDetail.HighlightsOut = CombineStr(context.DiveSiteDetail.HighlightsIn)
	context.DiveSiteDetail.HighlightsIn =nil
	context.PhotoAlbumsOut = CombineStr(context.PhotoAlbumsIn)
	context.PhotoAlbumsIn = nil
}

func CombineStr(silce []string) string {
	strSil := silce
	silce = nil
	str := strings.Join(strSil, ",")
	// silce = append(silce, str)
	return str
}
