$('#new-image').change(function () {
    var file = $('#new-image')[0].files[0];
    $('#filename').text(`New image will be ${file.name}`);
});