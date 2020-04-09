var update = function() {
    const email = $('#usrname').val()
    const oldName = $('#oldName').val()
    const newName = $('#newName').val()
    const edit = $('#editType').val()
    // if (edit == "edit") {
    //         alert("edit");
    // }
    // if (edit == "add") {
    //         alert("add");
    // }
    // if (edit == "delete") {
    //         alert("delete");
    // }
    const data = {
        "email": email,
        "oldVal": oldName,
        "newVal": newName,
        "edit": edit
    }
    endpoint = "/edit_contact"
    prefix = "http://127.0.0.1:5000"
    url = prefix.concat(endpoint)
    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data)
    }).then(response => {
        response.json().then(data => {
            const val  = data.value
            $("#emailField").val(usrname);
        })
    });
}


$("input#submit_btn").click(function() {
        update();
});
