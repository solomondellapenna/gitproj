package main

import (
	"fmt"
)

func RemoveChar(word string) string {
	var a = string(word[1])
	return a
}

func main() {
	fmt.Print(RemoveChar("help"))
}
