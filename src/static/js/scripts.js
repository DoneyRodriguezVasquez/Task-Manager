function dragStart(event) {
    event.dataTransfer.setData("Text", event.target.id);
}
function allowDrop(event) {
    event.preventDefault();
}
function drop(event) {
    if (event.target.id != "") {
        event.preventDefault();
        const data = event.dataTransfer.getData("Text");
        event.target.appendChild(document.getElementById(data));
        // todo list
        if (event.target.id == "todo") {
            document.getElementById(data).classList.remove("border-warning", "border-success", "border-secondary");
            document.getElementById(data).classList.add("border-primary");
            document.getElementById(data).getElementsByClassName("project-name")[0].classList.remove("bg-warning", "bg-success", "bg-secondary");
            document.getElementById(data).getElementsByClassName("project-name")[0].classList.add("bg-primary")
        }
        // waiting list
        if (event.target.id == "waiting") {
            document.getElementById(data).classList.remove("border-primary", "border-success","border-warning",);
            document.getElementById(data).classList.add("border-secondary");
            document.getElementById(data).getElementsByClassName("project-name")[0].classList.remove("bg-primary", "bg-success","bg-warning",);
            document.getElementById(data).getElementsByClassName("project-name")[0].classList.add("bg-secondary")
        }

        // progress list
        if (event.target.id == "progress") {
            document.getElementById(data).classList.remove("border-primary", "border-success", "border-secondary");
            document.getElementById(data).classList.add("border-warning");
            document.getElementById(data).getElementsByClassName("project-name")[0].classList.remove("bg-primary", "bg-success","bg-secondary");
            document.getElementById(data).getElementsByClassName("project-name")[0].classList.add("bg-warning")
        }

        // completed list
        if (event.target.id == "completed") {
            document.getElementById(data).classList.remove("border-warning", "border-success", "border-secondary");
            document.getElementById(data).classList.add("border-success");
            document.getElementById(data).getElementsByClassName("project-name")[0].classList.remove("bg-warning", "bg-success","bg-secondary");
            document.getElementById(data).getElementsByClassName("project-name")[0].classList.add("bg-success")
        }
    }
}