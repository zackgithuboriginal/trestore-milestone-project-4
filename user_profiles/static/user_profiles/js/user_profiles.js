function toggleForm(event) {
    if (event.firstChild.className === 'fas fa-edit') {
        event.firstChild.className = 'fas fa-times';
        event.firstChild.style.color = '#CC2936';
        event.parentNode.parentNode.parentNode.children[1].style.display = 'none';
        event.parentNode.parentNode.parentNode.children[2].style.display = 'flex';

    } else {
        event.firstChild.className = 'fas fa-edit';
        event.firstChild.style.color = '#336857';
        event.parentNode.parentNode.parentNode.children[1].style.display = 'flex';
        event.parentNode.parentNode.parentNode.children[2].style.display = 'none';
    }
}