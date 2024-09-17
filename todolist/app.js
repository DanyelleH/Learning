document.querySelector("#AddTask").addEventListener("click",addEvent);
function addEvent() {
    let list = document.createElement("li");
    let task = document.querySelector("#input").value;
    list.textContent = task;
    document.getElementById("toDoList").appendChild(list);
    document.querySelector("#input").value="";
    console.log(list)
}
