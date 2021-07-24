function displayComments(element, post_id) {
    if ($(`#comment-container-${ post_id }`).css('display') == 'none') {
        $(`#comment-container-${ post_id }`).css('display', 'flex');
        element.firstElementChild.textContent = 'Hide Comments ';
    } else {
        $(`#comment-container-${ post_id }`).css('display', 'none');
        element.firstElementChild.textContent = 'Show Comments ';
    }
}

function displayEditForm(comment_id) {
    let editNodes = document.getElementsByClassName('comment-edit');
    let editArray = [].slice.call(editNodes);
    let commentNodes = document.getElementsByClassName('comment-card');
    let commentArray = [].slice.call(commentNodes);
    for (var i = 0; i < editArray.length; i++) {
        editArray[i].style.display = 'none';
    }
    for (var j = 0; j < commentArray.length; j++) {
        commentArray[j].style.display = 'inline';
    }
    $(`#comment-edit-${ comment_id}`).css('display', 'flex');
    $(`#comment-${ comment_id}`).css('display', 'none');
}

function closeEdit(comment_id) {
    $(`#comment-edit-${ comment_id}`).css('display', 'none');
    $(`#comment-${ comment_id}`).css('display', 'inline');
}

$('.clear-text-button').click(function (e) {
    var elementId = $(this).attr('id').split('clear-button-')[1];
    $(`#comment_content_${elementId}`).val('');
});

$('#id_image').change(function () {
    var file = $('#id_image')[0].files[0];
    $('#filename').text(`New image will be ${file.name}`);
});