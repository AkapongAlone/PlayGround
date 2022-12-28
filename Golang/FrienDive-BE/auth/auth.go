package auth

import (
	"time"
	
	"github.com/golang-jwt/jwt/v4"
)

func GenToken(signature string) (string,error){
	token := jwt.NewWithClaims(jwt.SigningMethodHS256, &jwt.StandardClaims{
		ExpiresAt: time.Now().Add(5 * time.Hour).Unix(),
	})
	sign, err := token.SignedString([]byte(signature))
	if err != nil {
		return "",err
		}
	return sign, nil
	}
