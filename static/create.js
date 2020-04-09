var doCreate = function() {
    const email = $('#email').val()
    const password = $('#password').val()
    const data = {
        "email": email,
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
            const name = data.email
            $("#showName").val(name);
        })
    });
}


$("input#createButton").click(function() {
        doCreate();
});
