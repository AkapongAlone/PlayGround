package divesite

import (
	"fmt"
	db "friendDive/orm"
	"net/http"
	"strconv"
	"strings"

	"github.com/gin-gonic/gin"
)

func GetSite(c *gin.Context) {
	var Site db.DiveSiteBody
	idParam := c.Param("id")
	id,err :=strconv.Atoi(idParam)
	if err != nil {
		c.JSON(http.StatusBadRequest,gin.H{
			"error":err.Error(),
		})
	}
	db.Db.First(&Site,id)
	TypeToSplit(&Site)
	if int(Site.ID) == id {
		c.JSON(http.StatusOK, gin.H{
		"data": Site,
	})
	} else {
		c.JSON(http.StatusOK, gin.H{
			"error":idParam + " id  not found",
		})
	}
	return
}

func TypeToSplit(context *db.DiveSiteBody){
	context.Overview.DiveTypeIn = SplitStr(context.Overview.DiveTypeOut)
	context.DiveSiteDetail.HighlightsIn = SplitStr(context.DiveSiteDetail.HighlightsOut)
	context.PhotoAlbumsIn = SplitStr(context.PhotoAlbumsOut)
}

func SplitStr(slice string) []string{
	fmt.Println(slice)
	res1 := strings.Split(slice, ",")
	return res1
}
