/* a = 2.0 is var a: Double = 2.0
   b = 5.0 is var b: Double = 5.0
   c = 3.0 is var c: Double = 3.0
   y = ax² + bx + c is
var y: Double= a*(x*x) + b*x + c
*/
var a: Double = 2.0
var b: Double = 5.0
var c: Double = 3.0
/* For y = 0 is x = (-b +- √(b² - 4ac)) / 2a.
root = √(b² - 4ac) is
var root: Double = (b*b - 4*a*c).squareRoot()
x = (-b +- √(b² - 4ac)) / 2a is
var root1: 
  Double = (-b + root) / (2*a) and 
var root2: 
  Double = (-b - root) / (2*a) */
var root: Double = (b*b - 4*a*c).squareRoot()
/* root = √(b² - 4ac) */
var root1: Double = (-b + root) / (2*a)
/* x = (-b + √(b² - 4ac)) / 2a */
var root2: Double = (-b - root) / (2*a)
/* x = (-b - √(b² - 4ac)) / 2a */

// prints solution
print("Root 1 is \(root1).")
print("Root 2 is \(root2).")