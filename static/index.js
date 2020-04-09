var doCreate = function() {
    const username = $('#username').val()
    const password = $('#password').val()
    const data = {
        "username": username,
        "password": password
    }
    endpoint = "/create"
    url = string.concat(prefix, endpoint)
    fetch(url, {
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
