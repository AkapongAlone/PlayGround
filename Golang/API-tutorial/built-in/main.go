package main

import (
	"encoding/json"
	"fmt"
	"strconv"
	"strings"

	// "fmt"
	"io/ioutil"
	"log"
	"net/http"
	// "time"
)

var member []player

func init() {
	
	err := json.Unmarshal([]byte(`[{"ID":1,"Name":"Aek","Skill":"S","Match":0}]`),&member)
	if err != nil{
		log.Fatal(err)
	}
}

type player struct {
	ID		int		`json:"id"`
	Name	string  `json:"name"`
	Skill	string	`json:"skill"`
	Match	int		`json:"match"`
}

func eachMemberHandler(w http.ResponseWriter, r *http.Request) {
	urlPathSegment := strings.Split(r.URL.Path,"member/")
	ID,err := strconv.Atoi(urlPathSegment[len(urlPathSegment) -1])
	if err != nil {
		log.Print(err)
		w.WriteHeader(http.StatusNotFound)
		return
	}
	play, index := findId(ID)
	if play == nil {
		http.Error(w, fmt.Sprintf("not found this id %d",index),http.StatusNotFound)
		return
	}
	switch r.Method{
	case http.MethodGet:
		playJson, err := json.Marshal(play)
		if err != nil {
			w.WriteHeader(http.StatusInternalServerError)
			return
		}
		w.Header().Set("Context-Type","application/json")
		w.Write(playJson)
	case http.MethodPut:
		var editPlay player
		byteBody, err := ioutil.ReadAll(r.Body)
		if err != nil {
			w.WriteHeader(http.StatusBadRequest)
			return
		}
		err = json.Unmarshal(byteBody,&editPlay)
		if err != nil {
			w.WriteHeader(http.StatusBadRequest)
			return
		}
		member[ID] = editPlay
		w.WriteHeader(http.StatusAccepted)
		return
	default:
		w.WriteHeader(http.StatusMethodNotAllowed)
	}
}


func memberHandler(w http.ResponseWriter, r *http.Request) {
	memberJson, err := json.Marshal(member)
	switch r.Method{
	case http.MethodGet :
		if err != nil { 
			http.Error(w,err.Error(),http.StatusInternalServerError)
			return
		}
		w.Header().Set("Context-Type","application/json")
		w.Write(memberJson)
	case http.MethodPost:
		var newPlayer player
		Bodybyte, err:= ioutil.ReadAll(r.Body)
		if err != nil {
			w.WriteHeader(http.StatusBadRequest)
			return
		}
		err =json.Unmarshal(Bodybyte,&newPlayer)
		if err != nil{
			w.WriteHeader(http.StatusBadRequest)
			return
		}
		if newPlayer.ID != 0 {
			w.WriteHeader(http.StatusBadRequest)
			return
		}
		newPlayer.ID = getId()
		member = append(member, newPlayer)
		w.WriteHeader(http.StatusAccepted)
		return
	}
}

func findId(id int)(*player,int){
	for i, v := range member {
		if v.ID == id {
			return &v,i
		}
	}
	return nil,0
}

func getId()int{
	curId := -1
	for _,item :=range member{
		if item.ID > curId {
			curId = item.ID
		}
	}
	return curId + 1
}

func middleWareHandler(handler http.Handler) http.Handler{
	return http.HandlerFunc(func(w http.ResponseWriter,r *http.Request) {
			w.Header().Add("Access-Control-Allow-Origin","*")
			w.Header().Add("Access-Control-Allow-Methods","POST,GET,OPTIONS,PUT,DELETE")
			w.Header().Add("Access-Control-Allow-Headers","Accept,Context-Type,Content-Length,Authorization,X-O")


			handler.ServeHTTP(w,r)
	})
}

func main() {
	eachMem := http.HandlerFunc(eachMemberHandler)
	mem := http.HandlerFunc( memberHandler)
	http.Handle("/member/",eachMem)
	http.Handle("/member",mem)
	
	http.ListenAndServe(":8080", nil)
}