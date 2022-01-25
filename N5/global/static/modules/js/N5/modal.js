modalInstance = null;

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
    let modalName = `${modalType}-${modalId}`

    $("body").append(`<modal id="${modalName}" class="n5-modal">`);
    $(`#${modalName}`).append(content);
}

function closeModal() {
    $("modal").addClass("n5-modal-off")
    modalInstance = setTimeout(() => {
        $("modal").remove()
    },500)
}

