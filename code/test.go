package main

import "fmt"

func main() {
	v := "hello"
	fmt.Printf("%v", map[string]string{"key1": fmt.Sprintf("%s-%d", v, 4)})
}
