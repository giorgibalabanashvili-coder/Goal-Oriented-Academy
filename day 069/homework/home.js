function getPercentageDecl(num) {
    if (num < 100) {
        return num * 0.10; 
    } else if (num < 200) {
        return num * 0.20; 
    } else {
        return num * 0.30; 
    }
}

const getPercentageExpr = function(num) {
    if (num < 100) {
        return num * 0.10;
    } else if (num < 200) {
        return num * 0.20;
    } else {
        return num * 0.30;
    }
}

const getPercentageArrow = (num) => {
    if (num < 100) return num * 0.10;
    if (num < 200) return num * 0.20;
    return num * 0.30;
}



setTimeout(function() {
    console.log("ეს ტექსტი გამოჩნდება 2 წამში");
}, 2000)



function sayHello(name) { 
    console.log("გამარჯობა " + name);
}

sayHello("გიორგი"); 


//პარამეტრი-ეს არის ცვლადის სახელი რომელსაც მივუთითებთ ფუნქციის შექმნისას
//არგუმენტი-ეს არის რეალური მნიშვნელობა რომელსაც ფუნქციას გადავცემთ მისი გამოძახებისას

//default-პარამეტრი საშუალებას გვაძლევს პარამეტრს წინასწარ მივანიჭოთ საწყისი მნიშვნელობა.

function greetUser(username = "სტუმარო") {
    console.log("მოგესალმებით, " + username);
}
greetUser("ანი");
greetUser();      


const isGreaterThanTen = num => num > 10;
console.log(isGreaterThanTen(15));
console.log(isGreaterThanTen(5));  