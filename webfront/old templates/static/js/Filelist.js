var list;

function ref() {
    for(let i = 0; i < list.length; i++) {
        $.getJSON("../../rest/Status/"+list[i].task_id+"/", function(result) {
            document.getElementById(list[i].task_id).childNodes[4].innerHTML = result.task.status;
        });
    }
}

function htmlEncode(str){
    return String(str).replace(/[^\w. ]/gi, function(c){
        return '&#'+c.charCodeAt(0)+';';
    });
}

function Load() {
    try {
        $.getJSON("../../rest/getFilelist/", function(result){
            list = result.items;
            for(let i = 0; i < result.items.length; i++) {
                let size = parseInt(parseFloat(result.items[i].size)/1024);
                document.getElementById("list").innerHTML += "<div id=\""+result.items[i].task_id+"\" class=\"fileitem\">\n<div class=\"fileName\">"+htmlEncode(result.items[i].name)+"</div><div class=\"Size\">"+size.toString()+" KB</div><div class=\"Detection\">"+result.items[i].detection+"</div><div class=\"Status\">"+result.items[i].status+"</div>\n<div class=\"menu\"><a href=\"../YaraEditor/"+result.items[i].task_id+"/\">Yara Editor</a><a style=\"cursor: pointer;\" onclick=\"del("+result.items[i].task_id+")\">Delete</a><a href=\"../Report/"+list[i].task_id+"/\">Result</a></div>\n</div>";
            }
        });
    }
    catch(err) {
        alert(err.message);
    }
}

function Send() {
    document.getElementById("upload_hidden_panel").style.visibility = "hidden";
    try {
        var taskID = window.location.href.slice(33);
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const request = new Request(
            "../rest/CreateTask/",
            {
                method: 'POST',
                headers: {'X-CSRFToken': csrftoken},
                mode: 'same-origin', 
                body: new FormData(document.getElementById("frm"))
            }
        );
        fetch(request).then(function(response){
            response.text().then(function (text) {
                alert(text);
                location.reload();
            });
        });
    }
    catch(err) {
        alert(err.message);
    }
}

function open_upload_panel() {
    document.getElementById("upload_hidden_panel").style.visibility = "visible";
    document.getElementById("close_btn").style.visibility = "visible";
    document.getElementById("btn").style.visibility = "hidden";
}

function close_upload_panel() {
    document.getElementById("upload_hidden_panel").style.visibility = "hidden";
    document.getElementById("close_btn").style.visibility = "hidden";
    document.getElementById("btn").style.visibility = "visible";
}

function del(input) {
    $.get("../rest/Delete/"+input+"/", function(data, status){
        alert(data);
        location.reload();
    });
}

setInterval(ref ,5000);