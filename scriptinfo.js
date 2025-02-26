// function sumval(x,y){
//     console.log("hello world")
//     s=x+y
//     return s
// }

// i=1
// j=2
// a=sumval(i,j)
// console.log(a)

// s1=0
// s2=0
// x=1
// y=10
// naturalsum = (x,y)=>{
//     for(i=x;i<=y;i++){
//         s1+=i
//     }
//     return s1
// }
// sum1=naturalsum(x,y)
// console.log(sum1)

// function naturalsum1(x,y){
//     for(i=x;i<=y;i++){
//         s2+=i
//     }
//     return s2
// }
// sum2=naturalsum1(x,y)
// console.log(sum2)

// flag = 0
// n = 12
// i = 2
// prime = ()=>{
    
//     while(i <= (n/2)){
//         if(n%i == 0){
//             flag = 1
//             break
//         }
//         i += 1
//     } 
//     return flag
// }
// f=prime(n)
// if(f==1){
//     console.log("not prime")
//  }else{
//      console.log("prime")
//  }


// function prime(n){
//     while(i <= (n/2)){
//         if(n%i == 0){
//             flag = 1
//             break
//         }
//         i += 1
//     } 
//     return flag
// }
// f=prime(n)
// if(f==1){
// console.log("not prime")
// }else{
//     console.log("prime")
// }


setinfo = ()=>{
    console.log("hehehehe")
    document.getElementById("adata").innerHTML = "lol"
    document.querySelector("#adata").innerHTML = 100
    document.querySelector(".bdata").innerHTML = 200
    document.querySelector(".bdata").style.color = 'red'
}


//register_form.html
details = ()=>{
    console.log(document.querySelector("#name").value)
    console.log(document.querySelector("#email").value)
    console.log(document.querySelector('input[type="radio"][class="user"]:checked').value)
  }



//   arr=[1,2,3,4,5]
//   console.log(arr[0])

//   arr1=new Array()

// //display the sum of values in an array
// s=0
// for(i=0;i<=arr.length;i++){
//     s+=i
// }
// console.log(s)

// arr=['apple',1,2,'orange']
// console.log(arr[0])

// // display the count of capital letters in each element in an array
// arr=['apple','OranGe','BanAna','CheRRy','waTermelon']
// count=0
// for(i=0;i<arr.length;i++){
//     count=0
//     console.log(arr[i])
//     for(j=0;j<arr[i].length;j++){
//         if(arr[i][j]>='A' && arr[i][j]<='Z'){
//             count+=1
//         }
//     }
//     console.log(count)
// }

// Defining class using es6
class Vehicle {
	constructor(name, maker, engine) {
		this.name = name;
		this.maker = maker;
		this.engine = engine;
	}
	getDetails() {
		return (`The name of the bike is ${this.name}.`)
	}
}
// Making object with the help of the constructor
let bike1 = new Vehicle('Hayabusa', 'Suzuki', '1340cc');
let bike2 = new Vehicle('Ninja', 'Kawasaki', '998cc');

console.log(bike1.name); // Hayabusa
console.log(bike2.maker); // Kawasaki
console.log(bike1.getDetails());
