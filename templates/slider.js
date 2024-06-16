const slides = document.querySelectorAll('.advertising__container');
//const dots = document.querySelectorAll('.dot');
const intervalSlider = 5000;
let slideIndex = 0;

function sliderAuto() {
    setInterval(function() {
        slides[slideIndex].classList.remove('advertising_active');
        //dots[slideIndex].classList.remove('dot_active');
    
        slideIndex++;

        if (slideIndex >= slides.length) {
            slideIndex = 0;
        }
    
        slides[slideIndex].classList.add('advertising_active');
        //dots[slideIndex].classList.add('dot_active');
    }, intervalSlider);
        
    showSlide(slideIndex);
} 

sliderAuto();  