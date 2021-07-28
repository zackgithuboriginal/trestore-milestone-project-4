
/**
 * This function handles the display of the post edit options dropdown menu
 */
 $('.display-edit-dropdown').click(function() {
    let elementId = $(this).attr('id').split('display-dropdown-')[1]
    let target = document.getElementById(`display-options-${elementId}`);
    if (target.style.display == "flex") {
        clearDropdowns();
        target.style.display = "none";
    } else {
        clearDropdowns();
        target.style.display = "flex";
    }
})

/**
 * This function clears all of the post edit option dropdowns to ensure no more than one displays at a time
 */
function clearDropdowns() {
    let allProductDropdowns = document.querySelectorAll(".display-product-options");
    let allPostDropdowns = document.querySelectorAll(".display-edit-options");
    for (let i = 0; i < allPostDropdowns.length; i++) {
        allPostDropdowns[i].style.display = "none";
    }
    for (let i = 0; i < allProductDropdowns.length; i++) {
        allProductDropdowns[i].style.display = "none";
    }
}


/**
 * Automatically updates footer copyright date
 */
$(document).ready(function () {
    $("#date-target").text(new Date().getFullYear());
})

/**
 * Displays any django messages to the user when the page loads
 */
$(document).ready(function() {
    $(".toast").toast('show');
});