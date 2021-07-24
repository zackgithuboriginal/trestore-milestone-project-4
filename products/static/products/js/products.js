$('#id_image').change(function () {
    var file = $('#id_image')[0].files[0];
    $('#filename').text(`New image will be ${file.name}`);
});