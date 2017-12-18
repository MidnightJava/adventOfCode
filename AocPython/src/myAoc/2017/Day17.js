var l = []
var idx = 0
step = 386
for (i = 0; i < 2018; i++) {
	if (i != 0) {
		idx = (idx + step + 1) % l.length
  }
	l.splice(idx, 0, i)
}
console.log("Part 1:"+ l[(idx + 1) % l.length])

idx = 0
l = 0
var ol

start = Date.now();
while (l <= 50000000) {
	ol = l
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
	}
	else  {
		l = (count % l) + 1 + ol
	}
}
console.log("Part 2:" + " " + (ol - 1) + " (Time:" + (Date.now() - start) / 1000 + " sec)")
