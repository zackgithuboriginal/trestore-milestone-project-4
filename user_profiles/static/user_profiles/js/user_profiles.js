/**
 * Toggles between showing the user's delivery details or the
 * delivery details input form, if a user clicks the edit button
 */
 $('#toggle-delivery-details').click(function(){
    let target = $(this);
    if (target.children(":first").attr('class') === 'fas fa-edit') {
        target.children(":first").attr('class', 'fas fa-times');
        target.children(":first").css('color', '#CC2936');
        $('#details-display').css('display', 'none');
        $('#details-form').css('display', 'flex');

    } else {
        target.children(":first").attr('class', 'fas fa-edit');
        target.children(":first").css('color', '#336857');
        $('#details-display').css('display', 'flex');
        $('#details-form').css('display', 'none');
    }
});