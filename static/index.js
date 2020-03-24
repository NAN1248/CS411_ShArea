var doCreate = function() {
    const username = $('#username').val()
    const password = $('#password').val()
    const data = {
        "username": username,
        "password": password
    }
    fetch("http://127.0.0.1:5000/create", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data)
    }).then(response => {
        response.json().then(data => {
            const name = data.username
            $("#showName").val(name);

        })
    });
}


$("input#createButton").click(function() {
    doCreate();
});
