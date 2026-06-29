let number = 15;

if (number % 2 === 0) {
    console.log('even');
} else {
    console.log('odd');
}

let number = 15;

if (number % 3 === 0 && number % 5 === 0) {
    console.log('ეს რიცხვი არის 3-ის და 5-ის ჯერადი');
} else if (number % 3 === 0 || number % 5 === 0) {
    console.log('ეს რიცხვი არის სამის ან ხუთის ჯერადი');
} else {
    console.log('ეს რიცხვი არ არის არც სამის და არც ხუთის ჯერადი');
}


// == - არამკაცრი ტოლობა   5== "5" დააბრუვებს true -ს
// === -მკაცრი ტოლობა  5== "5" დააბრუვებს false-ს
// != -არ უდრის არამკაცრი 5 != 6 დააბრუნებს true ს
// !== მკაცრად არ უდრის 5!== 5 დააბრუნებს true ს
// > მეტობა	10 > 5 აბრუნებს true
// < ნაკლებობა	3 < 2 აბრუნებს false
//>=მეტია ან ტოლი5 >= 5 აბრუნებს true
//<=ნაკლებია ან ტოლი4 <= 7 აბრუნებს true


let number = 15;
let result = (number % 2 === 0) ? 'even' : 'odd';
console.log(result);