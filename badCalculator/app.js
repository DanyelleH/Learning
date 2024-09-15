let allResult =[]; //Result are saved here after moving on to add another value.
let add = false;
let subtract=false;
let multiple = false;
let divide = false;
document.querySelector('#one').addEventListener('click',toDisplay);
document.querySelector('#two').addEventListener('click', toDisplay);
document.querySelector('#three').addEventListener('click',toDisplay);
document.querySelector('#four').addEventListener('click', toDisplay);
document.querySelector('#five').addEventListener('click', toDisplay);
document.querySelector('#six').addEventListener('click',  toDisplay);
document.querySelector('#seven').addEventListener("click", toDisplay);
document.querySelector("#eight").addEventListener("click", toDisplay);
document.querySelector('#nine').addEventListener("click", toDisplay);
document.querySelector("#zero").addEventListener("click", toDisplay);
document.querySelector("#add").addEventListener("click", addResult);
document.querySelector("#subtract").addEventListener("click", subtractResult);
document.querySelector("#divide").addEventListener("click",divideResult);
document.querySelector("#multiply").addEventListener("click", multiplyResult);
document.querySelector("#clear").addEventListener("click",clearAll);
document.querySelector("#equals").addEventListener("click", equalsFunction);


function toDisplay() {
  let currentValue = document.querySelector(".Display").innerText 
// every time a value is inputted into the calculator, it is added to the inner text of the display class.
  let value = this.innerText
  document.querySelector(".Display").innerText = currentValue + value
}


function addResult(){
  allResult.push(document.querySelector(".Display").innerText)
  //push whatever value is showing on the disply to the allValues list.
  document.querySelector(".Display").innerText = ''
  // clear the value from the screen after it is stored in allValues
  console.log(allResult)
  add=true; // tracks what function is currently being utilized.
  //**enter function to do calculations */
}
function subtractResult() {
  allResult.push(document.querySelector(".Display").innerText);
  document.querySelector(".Display").innerText= '';
  subtract = true;
  //**enter function to do calculations */
}

function multiplyResult() {
  allResult.push(document.querySelector(".Display").innerText);
  document.querySelector(".Display").innerText = '';
  multiply = true;
  //**enter function to do calculations */
}

function divideResult() {
  allResult.push(document.querySelector(".Display").innerText)
  document.querySelector(".Display").innerText='';
  divide = true;
}

function clearAll(){
  document.querySelector(".Display").innerText='';
  allResult=[];
  add=subtract=divide=multiple=false;
}


function Calculation() {
  const secondValue = document.querySelector(".Display").innerText
  if (add) {
    const result = Number(allResult[0]) + Number(secondValue);
    document.querySelector(".Display").innerText= result
    allResult = [result];
    add = false;
    console.log(result)
  }
}
//   }
//   if (subtract) {
//     const result = Number(allResult[0])+ Number(secondValue);
//     document.querySelector(".Display").innerText=result;
//     allResult= result
//     subtract=false;
//   }
//   if (multiply) {
//     const result = Number(allResult[0]) * Number(secondValue);
//   }
// }

function equalsFunction() {
  document.querySelector(".Display").innerText = allResult[0];
}