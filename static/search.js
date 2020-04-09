// var ex = ['a','b','c']
var doLogin = function() {
    const email = $('#usr').val()
    const data = {
        "email": email
    }
    fetch("http://127.0.0.1:5000/contact", {
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
