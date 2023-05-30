// var lb = parseFloat(prompt("Enter the weight in pounds (lb)"));
// var kg = lb*0.454
// alert("The weight in kgs is "+kg);
// console.log("Conversion Completed")

var roster = []

var ans = prompt("Would you like to start the web roster app y/n")

if (ans == 'y'){
	var a;
	while (a != "quit"){
		a = prompt("Please select an action: add, remove, display, or quit")
		if (a == 'add'){
			var name = prompt("What name would you like to add?")
			roster.push(name)
		} 
		else if (a == 'remove'){
			var name = prompt("What name would you like to remove?");
			var idx = roster.indexOf(name);
			if (idx >= 0){
				roster.splice(idx,1);
			}
			else{
				alert("Not Found :(")
			}
		}
		else if (a == 'display'){
			console.log(roster)
		}
		else if(a == "quit"){
			break;
		}
	}
}
alert("Thanks for using the Web App! Please refresh the page to start over.")
