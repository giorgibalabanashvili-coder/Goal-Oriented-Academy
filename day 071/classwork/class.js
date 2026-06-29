//hoisting გაძლევს საშუალებას გამოვიყენოთ ფუნქცია ან ცვლადი მანამ სანამ მას კოდში ფიზიკურად დავწერთ
helloworld();
function helloworld(){
    console.log("მიესალმე სამყაროს");
    
}


let fruits = ["ვაშლი", "ბანანი", "ატამი", "მარწყვი", "საზამთრო"];

fruits.push("ანანასი");

fruits[fruits.length] = "მსხალი";
console.log(fruits); 



fruits[3] = "ალუბალი"; 
fruits[5] = "კივი";  

console.log(fruits);



console.log("პირველი ელემენტი:", fruits[0]); 
console.log("მეორე ელემენტი:", fruits[1]);  
console.log("მეხუთე ელემენტი:", fruits[4]);