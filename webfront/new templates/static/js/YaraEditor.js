function match() {
    try {
        var taskID = window.location.href.slice(33);
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const request = new Request(
            "../../rest/YaraMatch/"+taskID,
            {
                method: 'POST',
                headers: {'X-CSRFToken': csrftoken},
                mode: 'same-origin', 
                body: new FormData(document.getElementById("frm"))
            }
        );
        fetch(request).then(function(response){
            response.text().then(function (text) {
                document.getElementById("match_resualt").innerHTML = text;
            });
        });
    }
    catch(err) {
        alert(err.message);
    }
}