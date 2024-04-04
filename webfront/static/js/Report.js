function Load() {
    try {
        var taskID = window.location.href.slice(29);
        
        $.getJSON("../../rest/Status/"+taskID, function(result){
            document.getElementById("task_category").innerHTML = "Category: "+result.task.category;
            document.getElementById("added_on").innerHTML = "Analyze added to the Queue on: "+result.task.added_on;
            document.getElementById("completed_on").innerHTML = "Analyze completed on: "+result.task.completed_on;
        });
        
        $.getJSON("../../rest/Report/"+taskID, function(result){
            
            document.getElementById("list").innerHTML = "";
            
            for(var i in result) {
                if(i == "info") {
                    document.getElementById("list_header").innerHTML += "<div class=\"category active\" onclick=\"category_click(event, '"+i+"')\">"+i+"</div>";
                }
                else {
                    document.getElementById("list_header").innerHTML += "<div class=\"category\" onclick=\"category_click(event, '"+i+"')\">"+i+"</div>";
                }
            }
            
            for(var i in result) {
                if(i == "info") {
                    document.getElementById("list").innerHTML += "<div id=\""+i+"\" class=\"tabcontent\" style=\"display: block;\">"+json2html(result[i])+"</div>\n";
                }
                else {
                    document.getElementById("list").innerHTML += "<div id=\""+i+"\" class=\"tabcontent\" style=\"display: none;\">"+json2html(result[i])+"</div>\n";
                }
            }
        });
    }
    catch(err) {
        alert(err.message);
    }
}

function category_click(event, id) {
    var i, tabcontent, category;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    category = document.getElementsByClassName("category");
    for (i = 0; i < category.length; i++) {
        category[i].className = category[i].className.replace(" active", "");
    }
    document.getElementById(id).style.display = "block";
    event.currentTarget.className += " active";
}

function json2html(json) {
    let answer = "";
    if(typeof json == "string") {
        if(json.length != 0) {
            answer += json+"<br>";
        }
        else{
            answer += "empty<br>"
        }
    }
    else if(typeof json == "number") {
        answer += String(json)+"<br>";
    }
    else if(typeof json == "boolean") {
        answer += String(json)+"<br>";
    }
    else {
        answer += "<div>";
        if(json != null) {
            if(!jQuery.isEmptyObject(json)) {
                for(var i in json) {
                    answer += "<b>"+i+": </b>";
                    answer += json2html(json[i]);
                }
            }
            else{
                answer += "empty list";
            }
        }
        else{
            answer += "null";
        }
        answer += "</div>";
    }
    return answer;
}