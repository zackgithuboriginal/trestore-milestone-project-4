/**
 * This function handles the display of the post edit options dropdown menu
 */
 function productOptionsDropdown(product_id) {
    let target = document.getElementById(`product-options-${product_id}`);
    if (target.style.display == "flex") {
        clearDropdowns();
        target.style.display = "none";
    } else {
        clearDropdowns();
        target.style.display = "flex";
    }
}

/**
 * This function clears all of the post edit option dropdowns to ensure no more than one displays at a time
 */
function clearDropdowns() {
    let allDropdowns = document.querySelectorAll(".product-edit-options");
    for (let i = 0; i < allDropdowns.length; i++) {
        allDropdowns[i].style.display = "none";
    }
}
