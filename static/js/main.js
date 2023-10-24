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

let cords = ['scrollX', 'scrollY'];
// Перед закрытием записываем в локалсторадж window.scrollX и window.scrollY как scrollX и scrollY
window.addEventListener('unload', e => cords.forEach(cord => localStorage[cord] = window[cord]));
// Прокручиваем страницу к scrollX и scrollY из localStorage (либо 0,0 если там еще ничего нет)
window.scroll(...cords.map(cord => localStorage[cord]));

$(document).ready(function () {
    let display = false
    $(".cmt_btn").click(function () {
        if (display === false) {
            $(this).next(".comment-box").show("slow");
            display = true
        } else {
            $(this).next(".comment-box").hide("slow");
            display = false
        }
    });

    $('.like-form').submit(function (e) {
        e.preventDefault()

        const post_id = $(this).attr('id')

        const likeText = $(`.like-btn${post_id} > span`).text()
        const trim = $.trim(likeText)

        const url = $(this).attr('action')

        let res;
        const likes = $(`.like-count${post_id}`).text()
        const trimCount = parseInt(likes)

        console.log(trim)
        console.log(likes)
        console.log(trimCount)

        $.ajax({
            type: 'POST',
            url: url,
            data: {
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
                'post_id': post_id,
            },
            success: function (response) {
                if (trim === 'Like') {
                    $(`.like-btn${post_id} > i`).addClass("press");
                    $(`.like-btn${post_id} > span`).addClass("press").text("Unlike");


                    res = trimCount + 1
                } else {
                    $(`.like-btn${post_id} > i`).removeClass("press");
                    $(`.like-btn${post_id} > span`).removeClass("press").text("Like");

                    res = trimCount - 1
                }

                $(`.like-count${post_id}`).text(res + ' ' + 'отметок "Нравится"')
            },
            error: function (response) {
                console.log('error', response)
            }
        })

    })
});