$(document).on("submit", ".n5-form", function(event) {
    event.preventDefault();
    submitForm($(this));
})

function submitForm(form){
    let csrf_token = $(form).children("[name='csrfmiddlewaretoken']").attr("value")
    let form_data = $(form).serializeArray();
    let target_url = $(form).attr("target-url");
    let method = $(form).attr("method");
    let data = {};

    for (const object of form_data) {
        data[object.name] = object.value;
    };

    $.ajax({
        headers:{"X-CSRFTOKEN" : csrf_token}, 
        type: method,
        url: target_url,
        contentType: "application/json",
        dataType: "json",
        data: JSON.stringify(data),
        error: function(data) {
            console.log(data);
            reloadContent()
        },
        success: function() {
            closeModal();
            reloadContent();
            console.log(this.url);
        }
    });
};
