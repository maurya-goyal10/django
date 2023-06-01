var p1 = prompt("Player 1, Enter your name you will be blue");
var p2 = prompt("Player 2, Enter your name you will be red");

var arr = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]];
var chance = 0;
var gameover = false;
$("#chance").text(p1+": it is your turn, please pick a column to drop your blue chip")

// function rr(val){
// 	if 
// }

function checkArr(arr){
	for (var i=0;i<5;i++){
		for (var j = 0;j<4;j++){
			if (arr[i][j] != 0 && arr[i][j] == arr[i][j+1] && arr[i][j+1] == arr[i][j+2] && arr[i][j+2] == arr[i][j+3]){
				return arr[i][j] == 'b' ? p1 : p2;
			}
		}
	}
	for (var i=0;i<2;i++){
		for(var j=0;j<7;j++){
			if(arr[i][j] != 0 && arr[i][j] == arr[i+1][j] && arr[i+1][j] == arr[i+2][j] && arr[i+2][j] == arr[i+3][j]){
				return arr[i][j] == 'b' ? p1 : p2;
			}
		}
	}
	for (var i=4;i>2;i--){
		for(var j=0;j<4;j++){
			if((arr[i][j] != 0 && arr[i][j] == arr[i-1][j+1] && arr[i-1][j+1] == arr[i-2][j+2] && arr[i-2][j+2] == arr[i-3][j+3])){
				return arr[i][j] == 'b' ? p1 : p2;
			}
		}
	}
	for (var i=0;i<2;i++){
		for (var j=0;j<4;j++){
			if(arr[i][j] != 0 && arr[i][j] == arr[i+1][j+1] && arr[i+1][j+1] == arr[i+2][j+2] && arr[i+2][j+2] == arr[i+3][j+3]){
				return arr[i][j] == 'b' ? p1 : p2;
			}
		}
	}
	return null;
}


$(".r").click(function (){
	var row = $(this).attr('class').split(" ")[1];
	var i = -1;
	while(i >= -5 && !gameover){
		if ($("."+row).eq(i).attr('class').split(" ")[0] == 'r'){
			$("."+row).eq(i).removeClass('r');
			if(chance%2 == 0){
				$("."+row).eq(i).addClass('cb');
				arr[i+5][parseInt(row[1])-1] = 'b'
			}
			else{
				$("."+row).eq(i).addClass('cr');
				arr[i+5][parseInt(row[1])-1] = 'r'
			}
			chance++;
			if (chance%2 == 0){
			$("#chance").text(p1+": it is your turn, please pick a column to drop your blue chip")
			}
			else{
				$("#chance").text(p2+": it is your turn, please pick a column to drop your red chip")
			}
			if (checkArr(arr) != null){
				$("#chance").text(checkArr(arr)+" won the game, refresh to start again!");
				gameover = true;
			}
			break;

		}
		i--;
	}
})