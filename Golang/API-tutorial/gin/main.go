package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

type Book struct {
	ID string `json:"id"`   //ใส่json ต่อท้ายเพื่อบอกให้รู้ว่าถ้าอ่านjsonจะอ่านยังไง
	Title  string `json:"title"`
	Author string `json:"author"`
}

var books = []Book{
	{ID: "1", Title: "Harry Potter", Author: "J. K. Rowling"},
	{ID: "2", Title: "The Lord of the Rings", Author: "J. R. R. Tolkien"},
	{ID: "3", Title: "The Wizard of Oz", Author: "L. Frank Baum"},
}


func main() {
	r := gin.New()
	
	r.GET("/", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"message": "Hello World!",
		})
	})
	r.GET("/books", func(c *gin.Context) {
		c.JSON(http.StatusOK, books)
	})
	

	r.POST("/books", addBookHandler)

	r.DELETE("/books/:id",deleteBooksHandler )

	r.Run()
}

func listBookHandler(c *gin.Context)

func addBookHandler(c *gin.Context) {
	var book Book

	if err:=c.ShouldBindJSON(&book); err != nil{
		c.JSON(http.StatusBadRequest,gin.H{
			"Error":err.Error(),
		})
		return
	}
	books = append(books,book)
	c.JSON(http.StatusCreated,book)
}

func deleteBooksHandler(c *gin.Context) {
	id := c.Param(("id"))

	for index, item := range books {
		if id == item.ID {
			books = append(books[:index],books[index+1:]...)
			break
		}
	}
	c.Status(http.StatusNoContent)
}

