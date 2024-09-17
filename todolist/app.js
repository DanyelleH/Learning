document.querySelector("#AddTask").addEventListener("click",addEvent);
function addEvent() {
    let addedTask = document.querySelector("#input").value;
    // list.textContent = addedTasktask;
    // document.getElementById("toDoList").appendChild(list);
    // localStorage.setItem("task", [])
    let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
    tasks.push(addedTask)
    
    localStorage.setItem("tasks", JSON.stringify(tasks));
}