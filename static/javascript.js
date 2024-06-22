const sectionSelection = Array.from(document.getElementsByClassName('profile__item'))
let currentIndex = 0

function updateSlider() {
    sectionSelection.forEach((element, index) => {
        element.classList.remove('profile__item_active')
    });
    sectionSelection[currentIndex].classList.add('profile__item_active')
}

for (let i = 0; i < sectionSelection.length; i++) {
    sectionSelection[i].addEventListener('click', () => {
        currentIndex = i
        updateSlider()
    })
}

updateSlider()