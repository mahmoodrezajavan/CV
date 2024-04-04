function Load() {
    $.get("../rest/Logout", function(data, status){
        alert(data);
    });
}