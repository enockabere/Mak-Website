// mobile navigation
const primaryNav = document.querySelector('.primary-navigation');
const navToggle = document.querySelector('.mobile-nav-toggle');


navToggle.addEventListener('click', (e) => {
  const visibility = primaryNav.getAttribute('data-visible');

  if (visibility === "false") {
    primaryNav.setAttribute('data-visible', true);
    navToggle.setAttribute('aria-expanded', true);
  } else {
    primaryNav.setAttribute('data-visible', false);
    navToggle.setAttribute('aria-expanded', false);
  }
});




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


// accordion

var accordion = $('body').find('[data-behavior="accordion"]');
var expandedClass = 'is-expanded';

$.each(accordion, function () { // loop through all accordions on the page

  var accordionItems = $(this).find('[data-binding="expand-accordion-item"]');

  $.each(accordionItems, function () { // loop through all accordion items of each accordion
    var $this = $(this);
    var triggerBtn = $this.find('[data-binding="expand-accordion-trigger"]');

    var setHeight = function (nV) {
      // set height of inner content for smooth animation
      var innerContent = nV.find('.accordion__content-inner')[0],
        maxHeight = $(innerContent).outerHeight(),
        content = nV.find('.accordion__content')[0];

      if (!content.style.height || content.style.height === '0px') {
        $(content).css('height', maxHeight);
      } else {
        $(content).css('height', '0px');
      }
    };

    var toggleClasses = function (event) {
      var clickedItem = event.currentTarget;
      var currentItem = $(clickedItem).parent();
      var clickedContent = $(currentItem).find('.accordion__content')
      $(currentItem).toggleClass(expandedClass);
      setHeight(currentItem);

      if ($(currentItem).hasClass('is-expanded')) {
        $(clickedItem).attr('aria-selected', 'true');
        $(clickedItem).attr('aria-expanded', 'true');
        $(clickedContent).attr('aria-hidden', 'false');

      } else {
        $(clickedItem).attr('aria-selected', 'false');
        $(clickedItem).attr('aria-expanded', 'false');
        $(clickedContent).attr('aria-hidden', 'true');
      }
    }

    triggerBtn.on('click', event, function (e) {
      e.preventDefault();
      toggleClasses(event);
    });

    // open tabs if the spacebar or enter button is clicked whilst they are in focus
    $(triggerBtn).on('keydown', event, function (e) {
      if (e.keyCode === 13 || e.keyCode === 32) {
        e.preventDefault();
        toggleClasses(event);
      }
    });
  });

});


// Tabs

let tabs = document.querySelectorAll('.tabs__toggle');
contents = document.querySelectorAll('.tabs__content');


tabs.forEach((tab, index) => {
  tab.addEventListener('click', () => {
    contents.forEach((content) => {
      content.classList.remove('is-active');
    });
    tabs.forEach((tab) => {
      tab.classList.remove('is-active');
    });

    contents[index].classList.add('is-active');
    tabs[index].classList.add('is-active');
  })
})




// Modal popup

const modal = document.querySelector('#modal');
const openModal = document.querySelector('.open-button');
const closeModal = document.querySelector('.close-button');

openModal.addEventListener('click', () => {
  modal.showModal();
})

closeModal.addEventListener('click', (e) => {
  modal.close();
})