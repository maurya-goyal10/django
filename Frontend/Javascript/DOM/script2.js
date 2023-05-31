var one = document.querySelector("h1#one")
var two = document.querySelector("h1#two")
var three = document.querySelector("h1#three")

one.addEventListener('mouseover',function(){
	one.textContent = "Mouse over me!";
	one.style.color = 'red';
})

one.addEventListener('mouseout',function(){
	one.textContent = "Hover over me!";
	one.style.color = "black";
})

two.addEventListener('click',function(){
	if (two.textContent == "already been clicked :("){
		two.textContent = "Cick Me !!";
		two.style.color = 'black'
	}
	else {
		two.textContent = "already been clicked :(";
		two.style.color = 'blue';
	}
})

three.addEventListener('dblclick',function(){
	three.textContent = "clicked twice";
	three.style.color = 'pink';
})