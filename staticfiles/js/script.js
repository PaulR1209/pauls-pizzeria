document.addEventListener('DOMContentLoaded', function() {
    const toggler = document.querySelector('.navbar-toggler');
    const menu = document.getElementById('navbarNav');

    toggler.addEventListener('click', function() {
        menu.classList.toggle('show');
    });
});