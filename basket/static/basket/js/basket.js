$('.update-basket-button').click(function (e) {
    var form = $(this).parent().prev('.update-quantity-form');
    form.submit();
});


$('.basket-product-delete').click(function (e) {
    var csrfToken = "{{ csrf_token }}";
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