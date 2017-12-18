var idx = 0

var l = 0
var start = Date.now();
step = 386
for (i = 0; i <100e3; i++){
	let ol = l
	if (l != 0) {
		idx = (step + 1) % l
  }
	let count = 0
	while (idx != 0) {
		l+= 1
		idx = (idx + step + 1) % l
		count +=1
  }
	if (l == 0) {
		l =  1
	} else{
		l = (count % l) + 1 + ol
  }
}
console.log(l-1 +  " " + ol)
console.log(Date.now() - start);
