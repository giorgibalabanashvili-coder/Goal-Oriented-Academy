//Default  პარამეტრი ფუნქციას საშუალებას აძლევს გამოიყენოს წინასწარ განსაზღვრული მნიშვნელობა.
// თუ ფასდაკლებას (discount) არ გადავცემთ, ის ავტომატურად იქნება 0
function calculateTotal(price, discount = 0) {
    return price - discount;
}
console.log(calculateTotal(100, 15)); 
console.log(calculateTotal(100));     

const info = (name, age) => `my name is ${name}, i'm ${age} years old`
info('luka')



//1.
sayHello(); 
function sayHello() {
    console.log("გამარჯობა!");
}

// 2. 
const sayGoodbye = function() {
    console.log("ნახვამდის!");
};
sayGoodbye(); 



//Scope  განსაზღვრავს კოდის რომელ ნაწილშია ესა თუ ის ცვლადი ხელმისაწვდომი 
