var doLogin = function() {
    const email = $('#usr').val()
    const data = {
        "email": email
    }
    endpoint = "/contact"
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
            const info = data["contacts"]
             $("#contacts").val(info);
        })
    });
}


$("input#submitBtn").click(function() {
        doLogin();
});
