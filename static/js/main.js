// $(document).ready(function () {
//     $('#modal-btn').click(function ())
// })

// document.addEventListener("DOMContentLoaded", function(){
//   window.addEventListener('scroll', function() {
//       if (window.scrollY > 50) {
//         document.getElementById('navbar_top').classList.add('fixed-top');
//         // add padding top to show content behind navbar
//         navbar_height = document.querySelector('.navbar').offsetHeight;
//         document.body.style.paddingTop = navbar_height + 'px';
//       } else {
//         document.getElementById('navbar_top').classList.remove('fixed-top');
//          // remove padding top from body
//         document.body.style.paddingTop = '0';
//       }
//   });
// });

let cords = ['scrollX','scrollY'];
// Перед закрытием записываем в локалсторадж window.scrollX и window.scrollY как scrollX и scrollY
window.addEventListener('unload', e => cords.forEach(cord => localStorage[cord] = window[cord]));
// Прокручиваем страницу к scrollX и scrollY из localStorage (либо 0,0 если там еще ничего нет)
window.scroll(...cords.map(cord => localStorage[cord]));