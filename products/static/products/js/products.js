/**
 * when user uploads an image to the add or edit product forms,
 * a text element will be displayed containing the file name of the input image
 */
 $('#id_image').change(function () {
    var file = $('#id_image')[0].files[0];
    $('#filename').text(`New image will be ${file.name}`);
});


/**
 * The following functions handle submitting the product filter and sort form when the user changes the selection
 */
$('.product-filter-select').change(function(){
    submitForm();
});

$('.product-sort-select').change(function(){
    submitForm();
});

function submitForm(){
    $('.product-filter-form').submit();
}