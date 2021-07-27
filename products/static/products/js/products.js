/**
 * when user uploads an image to the add or edit product forms,
 * a text element will be displayed containing the file name of the input image
 */
$('#id_image').change(function () {
    var file = $('#id_image')[0].files[0];
    $('#filename').text(`New image will be ${file.name}`);
});