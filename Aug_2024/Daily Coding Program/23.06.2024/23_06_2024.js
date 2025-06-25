const arr = JSON.parse(prompt("enter the arr:"));
const target = parseInt(prompt("enter the target:"));

const arr_new = [];

for (let i=0; i <arr.length; i++) {
    for (let j= i+1; j<arr.length;j++){
        if (arr[i] + arr[j] === target){
         arr_new.push(arr[i],arr[j]);
        }
   }
}

console.log(arr_new);