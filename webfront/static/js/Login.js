function Login() {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const request = new Request(
        "../rest/Login/",
        {
            method: 'POST',
            headers: {'X-CSRFToken': csrftoken},
            mode: 'same-origin', 
            body: new FormData(document.getElementById("frm"))
        }
    );
    fetch(request).then(function(response) {
        if(response["status"] == 200) {
            window.location.href = "../Filelist";
        }
        else {
            response.text().then(function (text) {
                alert(text);
            });
        }
    });
}