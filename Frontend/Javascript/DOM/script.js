// var a = document.querySelector('h1')

// function getRandomColor() {
// 	var letters = "0123456789ABCDEF"
// 	var color = "#";
// 	for (var i = 0;i<6;i++){
// 		color += letters[Math.floor(Math.random()*16)];
// 	}
// 	return color;
// }

// function changeHead() {
// 	a.style.color = getRandomColor();
// }

// setInterval("changeHead()",500)

var a = document.querySelector('#restart')
var blocks = document.querySelectorAll(".ttt")

a.addEventListener('click',function(){
	blocks.forEach(function(b) {
		b = b.querySelector("div")
		b.textContent = ""
	})
})

blocks.forEach(function (b) {
	b.addEventListener('click',function (){
		// console.log(b.textContent)
		if (b.textContent == ""){
			b1 = b.querySelector("div")
			b1.textContent = "X"
		}
		else if (b.textContent == "X"){
			b1 = b.querySelector("div")
			b1.textContent = "O"
		}
		else{
			b1 = b.querySelector("div")
			b1.textContent = ""
		}
	})
})