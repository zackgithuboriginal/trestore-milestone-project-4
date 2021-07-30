/**
 * Handles the update product form submission from the larger page view
 */
$('.update-basket-button').click(function (e) {
    var form = $(this).prev('.update-quantity-form');
    form.submit();
});

/**
 * Handles the update product form submission from the small page view
 */
$('.update-basket-button-sm').click(function (e) {
    var form = $(this).prev('.update-quantity-form');
    form.submit();
});

/**
 * Handles the delete product request submission from the larger page view
 */
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

/**
 * Handles the delete product request submission from the sm page view
 */
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