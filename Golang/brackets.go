package main

import "fmt"



func main() {
	var input int
	fmt.Print("Введите число: ")
	fmt.Scanln(&input)


  

	bracket(input)



	// if 1 ["()"]
	// if 3 ["((()))","(()())","(())()","()(())","()()()"]
  // 1.1.1.0 / 1.2.0 / 1.1.0 + 1.0 / 1.0 + 1.1.0 / 3.0
	// aaabbb ( aababb ) {  aabbab abaabb  } ababab
	// 000111 001011 001101 010011 010101
	// (()()()) 0010101011
	// a( a or b) if b -> a  --- aba
	//  a if a --- aa(a or b)
	// aa if a --- aaa( a or b) x input -----> 00 if 0 --- 000 ( 0 or 1 )
	// a****b
	// 
}

func bracket( input int) {
	var a string = "("
	var b string = ")"
	var i int = input

  for i > 0 {
		
		i--
	}

	fmt.Println("")

	i = input
	for i > 0 {
		fmt.Print( a )
		i--
	}
		i = input
	for i > 0 {
		fmt.Print( b )
		i--
	}
	fmt.Println("")
}
