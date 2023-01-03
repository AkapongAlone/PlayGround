package auth

import (
	"fmt"
	"net/http"
	"strings"

	db "friendDive/orm"
	"os"

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
		// refreshToken(&tokenString)
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

		// if claims, ok := token.Claims.(jwt.MapClaims); ok && token.Valid {
		// 	// Check the expiry time
		// 	expiry, ok := claims["exp"].(float64)
		// 	if !ok {
		// 		ctx.AbortWithStatus(http.StatusBadRequest)
		// 		return
		// 	}
		// 	expiryTime := time.Unix(int64(expiry), 0)
		// 	if time.Now().After(expiryTime) {
		// 		fmt.Println("JWT has expired")
		// 		return
		// 	}

		// 	fmt.Println("JWT is valid and has not expired")
		// } else {
		// 	ctx.AbortWithStatus(http.StatusUnauthorized)
		// 	return
		// }

		ctx.Next()
	}
}

func refreshToken(Token *string) {
	var token db.UserBody
	db.Db.Where("token = ?", Token).First(&token)
	if token.ID != 0 {
		NewToken, _ := GenToken(os.Getenv("SIGN"))
		token.Token = NewToken
		db.Db.Save(&token)
		*Token = NewToken
	}

}
