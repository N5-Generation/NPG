$(document).on("click", ".getModal", function() {
    let method = $(this).attr("method");
    let url = $(this).attr("url");
    let type = $(this).attr("type");

    $.ajax({
        type: method,
        url: url,
        success : (data) => {
            createModal(type, data)
        }
    });
});

function createModal(modalType, content) {
    let modalId = Math.random().toString(36).substring(2);
    let modalName = `${modalType}-modal`;

    $("body").append(`<${modalName} id="${modalId}" class="n5-modal">`);
    $(`#${modalId}`).append(content);
}
