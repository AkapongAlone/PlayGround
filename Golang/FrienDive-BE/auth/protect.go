package auth

import (
	"fmt"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
	"github.com/golang-jwt/jwt/v4"
)

func Protect(signature []byte) gin.HandlerFunc {
	return func(ctx *gin.Context) {

		var tokenString string
		if auth := ctx.Request.Header.Get("Authorization"); auth != "" {
			tokenString = strings.TrimPrefix(auth, "Bearer ")
		} else if cookie, err := ctx.Cookie("jwt"); err == nil {
			tokenString = cookie
		} else {
			ctx.AbortWithStatus(http.StatusUnauthorized)
			return

		}
		
		_, err := jwt.Parse(tokenString, func(t *jwt.Token) (interface{}, error) {
			if _, ok := t.Method.(*jwt.SigningMethodHMAC); !ok {
				return nil, fmt.Errorf("Unexpected signing")
			}
			return signature, nil
		})

		if err != nil {
			ctx.AbortWithStatus(http.StatusUnauthorized)
			return
		}
		ctx.Next()
	}
}
