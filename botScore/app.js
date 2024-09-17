localStorage.setItem('count', 1)

const getStr = localStorage.getItem('count')

console.log(getStr)

document.querySelector("#up").addEventListener("click", addPoint)
document.querySelector("#down").addEventListener("click",subtractPoint)

function addPoint() {
    let count = Number(localStorage.getItem("count"))
    count +=1;
    localStorage.setItem("count",count);
    document.querySelector("#points").innertext = String(count);
}

function subtractPoint() {
    let count = Number(localStorage.getItem("count"));
    count -=1;
    localStorage.setItem("count",count);
    document.querySelector("#points").innertext = String(count);
}
