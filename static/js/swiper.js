// RECIPES CHOSEN | SWIPER

const swiper = new Swiper('.swiper', {
    direction: 'horizontal',
    mousewheel: true,
    loop: true,
    effect: 'fade',

    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },

    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },

});