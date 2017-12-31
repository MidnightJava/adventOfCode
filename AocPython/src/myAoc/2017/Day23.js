let b = c = h = 0;

b = 81
b*= 100
b+= 100000
//b = 108100
c = b
c+= 17000

function isPrime(n) {
   for (m = 2; m < n; m+= 1){
     if (n % m == 0) {
         return false;
      }
   }
   return true;
}

for (x = b; x <= b + 17000; x+= 17){
  if (!isPrime(x)) {
    h+= 1
  }
}
console.log(h)
