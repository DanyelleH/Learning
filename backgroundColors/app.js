document.querySelector("#turnRed").addEventListener("click", turnRedFunction);
document.querySelector("#turnBlue").addEventListener("click", turnBlueFunction);
document.querySelector("#turnGreen").addEventListener("click", turnGreenFunction);
document.querySelector("#turnOrange").addEventListener("click", turnOrangeFunction);
document.querySelector("#turnYellow").addEventListener("click", turnYellowFunction);
document.querySelector("#turnRandom").addEventListener("click", turnRandomFunction);

function turnRedFunction() {
  document.querySelector("body").style.backgroundColor = "red";
}

function turnBlueFunction() {
  document.querySelector("body").style.backgroundColor = "blue";
}

function turnPurpleFunction() {
  document.querySelector("body").style.backgroundColor = "purple";
}
function turnGreenFunction(){
  document.querySelector("body").style.backgroundColor = "green";
}
function turnOrangeFunction() {
  document.querySelector("body").style.backgroundColor = "orange";
}
function turnYellowFunction() {
  document.querySelector("body").style.backgroundColor ='yellow';
}
function turnRandomFunction() {
  document.querySelector("body").style.backgroundColor =' pink';
}

function turnRandomFunction() {
  const randomColor = '#' + Math.floor(Math.random() * 16777215).toString(16);
    document.body.style.backgroundColor = randomColor;
}