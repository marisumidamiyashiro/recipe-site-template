
//const wrapper = document.querySelector(".chosen-recipe-tab");
//const tabs = wrapper.querySelectorAll(".tab");
//const tabToggle = wrapper.querySelectorAll(".tab-toggle");


//function openTab() {
//    console.log(this)
//    const content = this.parentElement.nextElementSibling;
//    const activeItems = wrapper.querySelectorAll(".active");
//
//    if (!this.classList.contains('active')) {
//        this.classList.toggle('active');
//        content.classList.toggle('active');
//
//        activeItems.forEach(item => item.classList.toggle('active'));
//
//        wrapper.style.minHeight = content.offsetHeight + "px";
//    }
//}

//tabToggle.forEach(toggle => toggle.addEventListener('click', openTab));

window.addEventListener('load', function ()
{
const wrapper = document.querySelector(".chosen-recipe-tab");
const tabs = wrapper.querySelectorAll(".tab");
const tabToggle = wrapper.querySelectorAll(".tab-toggle");

function openTab() {

    const content = this.parentElement.nextElementSibling;
    const activeItems = wrapper.querySelectorAll(".active");

    if (!this.classList.contains('active')) {
        this.classList.toggle('active');
        content.classList.toggle('active');

        activeItems.forEach(item => item.classList.toggle('active'));

        wrapper.style.minHeight = content.offsetHeight + "px";
    }
}

tabToggle.forEach(toggle => toggle.addEventListener('click', openTab));
//    tabToggle[0].dispatchEvent(new Event('click'));
});
