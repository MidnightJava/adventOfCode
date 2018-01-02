let b = c = h = 0;

b = 81
b*= 100
b+= 100000
//b = 108100
c = b
c+= 17000

//Brute force translation, used to derive faster solution
if (false) {
  let f = e = d = 0
  do {
    f = 1
    d = 2
    do {
      e = 2
      do {
        g = d
        g*= e
        g-= b
        //g = 0 = d*e -b  => f set to zero
        //Thus f = 0 when some combination of d and e has a product
        //equal to b, or when b is a composite number
        if (g == 0){
          f = 0;
        }
        e += 1
        g = e
        g-= b
      } while (g != 0)
      d+= 1
      g = d
      g-= b
    } while (g != 0)
    if (f == 0) {
      h+= 1
    }
    g = b
    g-= c
    b+= 17
  } while (g != 0)
}

function isPrime(n) {
   for (m = 2; m < n; m+= 1){
     if (n % m == 0) {
         return false;
      }
   }
   return true;
}

for (x = b; x <= c; x+= 17){
  if (!isPrime(x)) {
    h+= 1
  }
}
console.log(h)
