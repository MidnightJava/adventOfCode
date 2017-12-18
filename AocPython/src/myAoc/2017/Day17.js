var step = 386

var l = []
var idx = 0

var now = Date.now();

for (i = 0; i < 50e6; i++) {
	if (i != 0) {
		idx = (idx + step + 1) % l.length
  }
	l.splice(idx, 0, i)

 	// print abs(len(l) - idx)
 	// print l[(l.index(0) + 1) % len(l)]
 	// print i, l[0]
	if (i == 2017) {
		console.log("Part 1:"+ l[(idx + 1) % l.length])
    console.log("Time: " + (Date.now() - now) / 1000)
  }
  // if (i % 1e6 == 0) {
  //   console.log(i)
  // }
}
 	// 	break
 	// if i % 100000 == 0:
 	// 	print i

console.log("Part 2:", l[(l.indexOf(0) + 1) % l.length])
console.log("Time: " + (Date.now() - now) / 1000)
