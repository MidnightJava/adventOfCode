
let TARGET = '360781'
let tlist = [3,6,0,7,8,1]

let recipes = [3,7]
let current = [0,1]


let done = false
let ntarget = TARGET
let start_time = new Date().getTime()
while (!done) {
	let n = recipes[current[0]] + recipes[current[1]];
	let n_digits = n.toString();

	n_digits.split('').forEach( c => {
		recipes.push(parseInt(c));
		if (c === ntarget[0]) {
			ntarget = ntarget.slice(1);
			if  (ntarget.length === 0) {
				console.log(`part 2: ${recipes.length - tlist.length}  time: ${(new Date().getTime() - start_time) / 1000} sec`);
				done = true;
			}
		} else {
			ntarget = TARGET;
		}
	});

	current[0] = (current[0] + 1 + recipes[current[0]]) % recipes.length;
	current[1] = (current[1] + 1 + recipes[current[1]]) % recipes.length;
	
}
