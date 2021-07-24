$('.update-basket-button').click(function (e) {
    var form = $(this).prev('.update-quantity-form');
    form.submit();
});

$('.update-basket-button-sm').click(function (e) {
    var form = $(this).prev('.update-quantity-form');
    form.submit();
});

$('.basket-product-delete-tb').click(function (e) {
    var csrfToken = $('.basket-product-delete-tb').attr('data-csrf');
    var itemId = $(this).attr('id').split('delete_')[1];
    var url = `/basket/delete/${itemId}/`;
    var data = {
        'csrfmiddlewaretoken': csrfToken
    };

    $.post(url, data)
        .done(function () {
            location.reload();
        });
});

$('.basket-product-delete-sm').click(function (e) {
    var csrfToken = $('.basket-product-delete-sm').attr('data-csrf');
    var itemId = $(this).attr('id').split('delete_sm_')[1];
    var url = `/basket/delete/${itemId}/`;
    var data = {
        'csrfmiddlewaretoken': csrfToken
    };

    $.post(url, data)
        .done(function () {
            location.reload();
        });
});