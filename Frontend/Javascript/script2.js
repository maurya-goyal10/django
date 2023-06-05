var a = prompt("Enter the full name")
var b = a.split(" ")

var age = parseInt(prompt("Enter the age: "))

var height = parseFloat(prompt("Enter the height: "))

var pet = prompt("Enter the pet name")
var l = pet.length

// console.log(b[0][0]+b[1][0])
if (b[0][0]>='A' && b[0][0]<='Z' && b[1][0]>='A' && b[1][0]<='Z' && age >= 20 && age <= 30 && height >= 170 
&& pet[l-1] == 'y'){
	console.log("Spy detected")
} 
else{
	console.log("WELCOME")
}