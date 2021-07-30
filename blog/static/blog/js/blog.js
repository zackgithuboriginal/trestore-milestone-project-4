/**
 * this functions toggles the display of the comment section
 */
 $('.display-comments').click(function() {
    let elementId = $(this).attr('id').split('display-comments-')[1];
    if ($(`#comment-container-${ elementId }`).css('display') == 'none') {
        $(`#comment-container-${ elementId }`).css('display', 'flex');
        $(this).children(":first").text('Hide Comments ');
    } else {
        $(`#comment-container-${ elementId }`).css('display', 'none');
        $(this).children(":first").text('Show Comments ');
    }
});

/**
 * this functions toggles the display of the edit comment form
 */
$('.comment-link-edit').click(function(){
    let elementId = $(this).attr('id').split('comment-link-')[1];
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
    $(`#comment-edit-${elementId}`).css('display', 'flex');
    $(`#comment-${elementId}`).css('display', 'none');
});

/**
 * this functions toggles the display of the comment section
 */
$('.comment-cancel').click(function(){
    let elementId = $(this).attr('id').split('comment-cancel-')[1];
    $(`#comment-edit-${elementId}`).css('display', 'none');
    $(`#comment-${elementId}`).css('display', 'inline');
});

/**
 * this functions clears the add comment form
 */
$('.clear-text-button').click(function (e) {
    var elementId = $(this).attr('id').split('clear-button-')[1];
    $(`#comment_content_${elementId}`).val('');
});

/**
 * This function controls the 
 */

$('#id_image').change(function () {
    var file = $('#id_image')[0].files[0];
    $('#filename').text(`New image will be ${file.name}`);
});