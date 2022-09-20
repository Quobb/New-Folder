var Kelvin = 1000;
//stored 293 to the variable kelvin
var Celsius = Kelvin - 273;
var Newton = Celsius * (33 / 100);
//converting Kelvin to Celsuis
var newton = Math.floor(Newton)
var Fahrenheit = Celsius * (9 / 5) + 32;
//rounding of Fahrenheit
var fahrenheit = Math.floor(Fahrenheit);
//saving the rounded variable into another variable 
console.log(`The temperature is ${fahrenheit} degrees Fahrenheit`);
console.log(`The newton is ${newton} `)