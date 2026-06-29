//ფუნქცია გამოიზენება კოდის გარკვეული ბლოკის დასაჯგუფებლად
//ფუნქციის შესაქმნელად js ში გამოიყენება function keyword ი
function Sum(a, b) {
    let sum = a + b;
    console.log(sum);
}
Sum(5, 7);   
//return აბრუნებს მნიშვნელობას

function isGreaterThanTen(number) {
    if (number > 10) {
        return true;
    } else {
        return false;
    }
}

let result1 = isGreaterThanTen(15);
let result2 = isGreaterThanTen(4);
console.log(result1); 
console.log(result2); 