
function create_task() {
    console.log("Creating a task.")
    $.ajax({
        url: 'create_task/',
        type: "POST",
        data: { the_task : $('#task-title').val() },

        success : function(json) {
            $('#task-title').val(' ');
            console.log(json);
            console.log("Task added successfully.");
        },

        error : function(xhr,errmsg,err) {
            $("#results").html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
            " <a href='#' class='close'>&times;</a></div>");
            console.log(xhr.status + ": " + xhr.responseText);
        }
    });
};