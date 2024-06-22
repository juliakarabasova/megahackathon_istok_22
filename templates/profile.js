const infoBlock = document.querySelector('.main__inner');
const linkCategory = document.querySelectorAll('.profile__item');

//снимаем .link_active с категории
function clearActiveCategory() {
    document.querySelector('.profile__item.link_active').classList.remove('link_active');
}

//меняем активную актегорию
function toggleLinkCategory()  {
    linkCategory.forEach((item) => {
        item.addEventListener('click', (event) => {
            let categoryObj = event.target.closest('.profile__item');
            clearActiveCategory();
            categoryObj.classList.add('link_active');

            if(item.classList.contains('link_active')) {
                categoryObj = item.innerText;
            }
        });
    });
}

function drawMainInfo() {
    infoBlock.innerHTML = '';
    let mainInfo = `<div class="info_container">
                    <form class="form" action="" method="">
                    <label class="form__label">
                        <legend class="form__legend">Фамилия</legend>
                        <input class="form__input" type="text" name="name">
                    </label>
                    <label class="form__label">
                        <legend class="form__legend">Имя</legend>
                        <input class="form__input" type="text" name="name">
                    </label>
                    <label class="form__label">
                        <legend class="form__legend">Отчество</legend>
                        <input class="form__input" type="text" name="name">
                    </label>
                    <label class="form__label">
                        <legend class="form__legend">Номер телефона</legend>
                        <input class="form__input" type="tel" name="name">
                    </label>
                    <label class="form__label">
                        <legend class="form__legend">Почта</legend>
                        <input class="form__input" type="email" name="name">
                    </label>
                    <section class="delivery">
                        <h3 class="delivery__address">Адреса доставки</h3>
                    </section>
                </form>
                </div>`;
infoBlock.innerHTML += mainInfo;
}

function drawOrder() {
    infoBlock.innerHTML = '';
let order = `<section class="order">
                    <div class="order__box order__box_confirmation">
                        <div class="order__box_text">
                            <h3 class="order__title">Заказ №598652086</h3>
                            <p class="order__text">Кухонный шкаф 30x40, кухонная плита, духовой шкаф, кухонный шкаф...</p>
                        </div>
                        <img src="/static/Profile/svg/confirmation.svg" class="confirmation" alt="confirmation" width="56" height="56">
                    </div>
                    <div class="order__box order__box_assembly">
                        <div class="order__box_text">
                            <h3 class="order__title">Заказ №598652086</h3>
                            <p class="order__text">Кухонный шкаф 30x40, кухонная плита, духовой шкаф, кухонный шкаф...</p>
                        </div>
                        <img src="/static/Profile/svg/assembly.svg" class="assembly" alt="assembly" width="56" height="56">
                    </div>
                    <div class="order__box order__box_sending">
                        <div class="order__box_text">
                            <h3 class="order__title">Заказ №598652086</h3>
                            <p class="order__text">Кухонный шкаф 30x40, кухонная плита, духовой шкаф, кухонный шкаф...</p>
                        </div>
                        <img src="/static/Profile/svg/sending.svg" class="sending" alt="sending" width="56" height="56">
                    </div>
                    <div class="order__box order__box_received">
                        <div class="order__box_text">
                            <h3 class="order__title">Заказ №598652086</h3>
                            <p class="order__text">Кухонный шкаф 30x40, кухонная плита, духовой шкаф, кухонный шкаф...</p>
                        </div>
                        <img src="/static/Profile/svg/received.svg" class="received" alt="received" width="56" height="56">
                    </div>
                </section>`;
infoBlock.innerHTML += order;
}

function drawBonuses() {
    infoBlock.innerHTML = '';
let order = `<section class="bonuses">
                    <p class="bonuses_amount">10141 Б</p>
                    <h4 class="bonuses_history">История бонусов</h4>
                    <div class="bonuses_wrap">
                        <div class="bonuses_wrap_text">
                            <h6 class="bonuses_title">Реферальная программа</h6>
                            <p class="bonuses_data">28.07.2024</p>
                        </div>
                        <p class="bonuses_number bonuses_number_plus">+10000</p>
                    </div>
                    <div class="bonuses_wrap">
                        <div class="bonuses_wrap_text">
                            <h6 class="bonuses_title">Заказ</h6>
                            <p class="bonuses_data">26.07.2024</p>
                        </div>
                        <p class="bonuses_number bonuses_number_plus">+141</p>
                    </div>
                    <div class="bonuses_wrap">
                        <div class="bonuses_wrap_text">
                            <h6 class="bonuses_title">Заказ</h6>
                            <p class="bonuses_data">26.07.2024</p>
                        </div>
                        <p class="bonuses_number bonuses_number_minus">-10000</p>
                    </div>
                    <div class="bonuses_wrap">
                        <div class="bonuses_wrap_text">
                            <h6 class="bonuses_title">Реферальная программа</h6>
                            <p class="bonuses_data">28.07.2024</p>
                        </div>
                        <p class="bonuses_number bonuses_number_plus">+10000</p>
                    </div>
                </section>`;
infoBlock.innerHTML += order;
}

document.addEventListener("DOMContentLoaded", function() {
    drawMainInfo();
    toggleLinkCategory();
});