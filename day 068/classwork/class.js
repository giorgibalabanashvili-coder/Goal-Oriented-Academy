let age = 20; 

if (age >= 18) {
    console.log("სრულწლოვანი ხარ");
} else {
    console.log("არასრულწლოვანი ხარ");
}
   
let number = 7; 

if (number % 2 === 0) {
    console.log("ლუწი");
} else {
    console.log("კენტი");
}


let score = 85; 

if (score >= 90 && score <= 100) {
    console.log("A");
} else if (score >= 80 && score <= 89) {
    console.log("B");
} else if (score >= 70 && score <= 79) {
    console.log("C");
} else if (score >= 60 && score <= 69) {
    console.log("D");
} else if (score < 60) {
    console.log("F");
}

let purchaseAmount = 120; 
let finalPrice = purchaseAmount > 100 ? purchaseAmount * 0.9 : purchaseAmount;
console.log(finalPrice);


let a = 15;
let b = 25;
let max = a > b ? a : b;
console.log(max);