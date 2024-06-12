// NAV MENU ICON
const menubutton = document.querySelector('.menu-button');
const mylistitems = document.querySelector('.site-nav li');
const mysitenav = document.querySelector('.site-header .site-nav');

menubutton.onclick = function () {
    if (mysitenav.getAttribute('data-navstate') === 'open') {
        mysitenav.setAttribute('data-navstate', 'closed');
    } else {
        mysitenav.setAttribute('data-navstate', 'open');
    }
};