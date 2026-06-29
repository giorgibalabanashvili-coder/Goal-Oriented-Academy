let names=["giorgi","luka","nika"]

names.push("vano")

names.pop()

names.unshift(gela)

names.shift()

console.log(names)


let fruits=["apple","peach","watermelon"]
let vegetariable = ["cucumber","tomato","banana"]
console.log(fruits.concat(vegetariable))


let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let slicedNumbers = numbers.slice(3, 7);

console.log(slicedNumbers)
console.log(numbers)



let cart = [];

cart.push("milk", "bread", "cheese");

cart.shift();

cart.unshift("coffe");

cart.pop();
console.log(cart);



let favoriteMovies = ["Inception", "Interstellar", "The Dark Knight"];
let newMovies = ["Dune", "Oppenheimer"];

let Movies = favoriteMovies.concat(newMovies);

let topThreeMovies = Movies.slice(0, 3);

console.log( Movies);
console.log(topThreeMovies);

