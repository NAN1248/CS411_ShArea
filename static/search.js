// var ex = ['a','b','c']
var test = "http://localhost:5000/contact"
var url = "http://127.0.0.1:5000/contact"
var doLogin = function() {
    const email = $('#usr').val()
    const data = {
        "email": email
    }
    endpoint = "/create"
    url = string.concat(prefix, endpoint)
    fetch(url, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data)
    }).then(response => {
        response.json().then(data => {
            const info = data.contacts
             $("#contacts").val(info);
        })
    });
}


$("input#submitBtn").click(function() {
        doLogin();
});
