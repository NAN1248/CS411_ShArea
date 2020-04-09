var test = "http://localhost:5000/login"
var url = "http://127.0.0.1:5000/login"

var doLogin = function() {
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
            const val = data.value
            // $("#emailField").val(email);
            if (val == "Success") {
                    window.location.href = './templates/settings';
            }
        })
    });
}


$("input#login_btn").click(function() {
        doLogin();
});
