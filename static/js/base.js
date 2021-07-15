/**
 * This function handles the display of the post edit options dropdown menu
 */
 function displayOptionsDropdown(id) {
    let target = document.getElementById(`display-options-${id}`);
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
    let allDropdowns = document.querySelectorAll(".display-edit-options");
    for (let i = 0; i < allDropdowns.length; i++) {
        allDropdowns[i].style.display = "none";
    }
}
