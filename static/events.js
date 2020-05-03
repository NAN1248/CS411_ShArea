var getEvents = function() {
    endpoint = "/get_all_events"
    prefix = "http://127.0.0.1:5000"
    url = prefix.concat(endpoint)
    fetch(url, {
        method: "GET",

        headers: {
            "Content-Type": "application/json",
        }
    }).then(response => {
        response.json().then(data => {
                // console.log(res)
                var obj = data["result"]
                var display = []
                for(var i = 0; i < obj.length; i++) {
                        var item = obj[i]
                        tmp = []
                        tmp.push("id: " + item.id)
                        tmp.push("start_time: " + item.start_time)
                        tmp.push("tags: " + item.tags)
                        tmp.push("duration: " + item.duration)
                        // console.log(obj[i].start_time);
                        display.push(tmp)
                }
             $("#Events").val(display);
        })
    });
}

var searchEvent = function() {
    const query = $('#tag_info').val()
    const data = {
        "query": query
    }
    prefix = "http://127.0.0.1:5000"
    endpoint = "/search_event"
    url = prefix.concat(endpoint)
    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data)
    }).then(response => {
        response.json().then(data => {
                var obj = data["result"]
                var display = []
                for(var i = 0; i < obj.length; i++) {
                        var item = obj[i]
                        tmp = []
                        tmp.push("id: " + item.id)
                        tmp.push("start_time: " + item.start_time)
                        tmp.push("tags: " + item.tags)
                        tmp.push("duration: " + item.duration)
                        // console.log(obj[i].start_time);
                        display.push(tmp)
                }
             $("#Events").val(display);
        })
    });
}


$("input#submitBtn").click(function() {
        getEvents();
});

$("input#searchBtn").click(function() {
        searchEvent();
});
