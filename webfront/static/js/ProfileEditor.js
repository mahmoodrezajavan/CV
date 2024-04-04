function EmailEdit() {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const request = new Request(
        "../rest/EmailChange/",
        {
            method: 'POST',
            headers: {'X-CSRFToken': csrftoken},
            mode: 'same-origin', 
            body: new FormData(document.getElementById("Email_Edit"))
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

function PasswordEdit() {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const request = new Request(
        "../rest/PasswordChange/",
        {
            method: 'POST',
            headers: {'X-CSRFToken': csrftoken},
            mode: 'same-origin', 
            body: new FormData(document.getElementById("Password_Edit"))
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

function Load() {
    try {
        $.getJSON("../rest/getProfile", function(result){
            document.getElementById("username").innerHTML = "Hi, "+result["username"]+document.getElementById("username").innerHTML;
            document.getElementById("email").value = result["email"];
        });
    }
    catch(err) {
        alert(err.message);
    }
}