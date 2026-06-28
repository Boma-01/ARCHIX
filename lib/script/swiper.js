document.addEventListener("DOMContentLoaded", () => {
    const swiper = new Swiper(".mySwiper", {
        slidesPerView: 1,
        spaceBetween: 30,
        speed: 800,
        effect: "fade",
        loop: false,

        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
        },

        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },
    });

    console.log(swiper.slides.length);
});