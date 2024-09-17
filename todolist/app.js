document.querySelector("#AddTask").addEventListener("click",addEvent);
function addEvent() {
    let addedTask = document.querySelector("#input").value;

    let tasks = JSON.parse(localStorage.getItem("tasks")) || [];

    tasks.push(addedTask)
    
    localStorage.setItem("tasks", JSON.stringify(tasks));
    document.querySelector("#input").value = "";
    updateDisplay()
}


function updateDisplay() {
    let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
    let taskList = document.getElementById("toDoList");
    taskList.innerHTML =""

    tasks.forEach((task, index) => {
        let listItem= document.createElement("li");
        listItem.textContent = task ;

        let removeButton = document.createElement("button");
        removeButton.textContent= "Remove";
        removeButton.addEventListener("click", function(){
            removeTask(index);
    });
    listItem.appendChild(removeButton)
    taskList.appendChild(listItem)
    })
}

function removeTask(index) {
    let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
    tasks.splice(index,1);
     localStorage.setItem("tasks", JSON.stringify(tasks));
     updateDisplay()
}
updateDisplay()


// document.querySelector("#toDoList").innerHTML = (localStorage.getItem("tasks"))
