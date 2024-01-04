var id = 0;
var state = "";

function dragStart(event) {
    event.dataTransfer.setData("Text", event.target.id);
    ide = document.getElementById(event.target.id).getElementsByClassName("properties")[0].getAttribute("value");
    event.dataTransfer.setData("id",ide);
    console.log("test target id: "+event.target.id);
    console.log("test id: "+ide);
}
function allowDrop(event) {
    event.preventDefault();
}
function drop(event) {
    if (event.target.id != "") {
        event.preventDefault();
        const data = event.dataTransfer.getData("Text");
        id = event.dataTransfer.getData("id");
        console.log("test id2: "+id);
        event.target.appendChild(document.getElementById(data));
        // todo list
        if (event.target.id == "TO_DO") {
            document.getElementById(data).classList.remove("border-warning", "border-success", "border-secondary");
            document.getElementById(data).classList.add("border-primary");
            document.getElementById(data).getElementsByClassName("project-name")[0].classList.remove("bg-warning", "bg-success", "bg-secondary");
            document.getElementById(data).getElementsByClassName("project-name")[0].classList.add("bg-primary")
            state = event.target.id;
            update_state(id, state);
        }
        // waiting list
        if (event.target.id == "WAITING") {
            document.getElementById(data).classList.remove("border-primary", "border-success","border-warning",);
            document.getElementById(data).classList.add("border-secondary");
            document.getElementById(data).getElementsByClassName("project-name")[0].classList.remove("bg-primary", "bg-success","bg-warning",);
            document.getElementById(data).getElementsByClassName("project-name")[0].classList.add("bg-secondary")
            state = event.target.id;
            update_state(id, state);
        }
        
        // progress list
        if (event.target.id == "IN_PROGRESS") {
            document.getElementById(data).classList.remove("border-primary", "border-success", "border-secondary");
            document.getElementById(data).classList.add("border-warning");
            document.getElementById(data).getElementsByClassName("project-name")[0].classList.remove("bg-primary", "bg-success","bg-secondary");
            document.getElementById(data).getElementsByClassName("project-name")[0].classList.add("bg-warning");
            state = event.target.id;
            update_state(id, state);
        }

        // completed list
        if (event.target.id == "DONE") {
            document.getElementById(data).classList.remove("border-warning", "border-success", "border-secondary");
            document.getElementById(data).classList.add("border-success");
            document.getElementById(data).getElementsByClassName("project-name")[0].classList.remove("bg-warning", "bg-success","bg-secondary");
            document.getElementById(data).getElementsByClassName("project-name")[0].classList.add("bg-success")
            state = event.target.id;
            update_state(id, state);
        }

        //update task state
        function update_state(id, state){
            console.log("id: "+id+" state: "+state);
            $.ajax({
                type: "GET",
                url: '{{ '/' }}',
                data: { id: id, state: state, value:'dragged' },
                success: function callback(response){
                            console.log("success");
                         }
             });
        }
    }
}