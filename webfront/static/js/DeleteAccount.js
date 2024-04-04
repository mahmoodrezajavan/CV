function Load() {
    $.get("../rest/DeleteAccount", function(data, status){
        alert(data);
    });
}