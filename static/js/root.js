// mobile navigation
const primaryNav = document.querySelector('.primary-navigation');
const navToggle = document.querySelector('.mobile-nav-toggle');


navToggle.addEventListener('click', (e) => {
    const visibility = primaryNav.getAttribute('data-visible');

    if (visibility === "false") {
        primaryNav.setAttribute('data-visible', true);
        navToggle.setAttribute('aria-expanded', true);
    } else  {
        primaryNav.setAttribute('data-visible', false);
        navToggle.setAttribute('aria-expanded', false);
    } 
});



function showHideNavStyling() {
	
    // if ($(window).scrollTop() > $(window).height() / 2 ) {
    //     $("#header").addClass('visible');
    //     console.log(visible);
    // } else {
    //     $("#header").removeClass('visible');
    // }

}




// carousel selector
document.querySelectorAll(".carousel").forEach(carousel => {

    const items = carousel.querySelectorAll(".carousel__item");
    const buttonsHtml = Array.from(items, () => {

        return `<span class="carousel__button"></span>`;

    });

    carousel.insertAdjacentHTML("beforeend", `

        <div class="carousel__nav"> ${buttonsHtml.join("")} </div>

    `);

    const buttons = carousel.querySelectorAll(".carousel__button");

    buttons.forEach((button, i) => {

        button.addEventListener("click", () => {

            // un-select all the items
            items.forEach(item => item.classList.remove("carousel__item--selected"));
            buttons.forEach(button => button.classList.remove("carousel__button--selected"));

            items[i].classList.add("carousel__item--selected");
            button.classList.add("carousel__button--selected");

        });
    });

    // select the first item on page load
    items[0].classList.add("carousel__item--selected");
    buttons[0].classList.add("carousel__button--selected");

});