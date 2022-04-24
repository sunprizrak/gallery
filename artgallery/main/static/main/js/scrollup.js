$(function(){
    $(window).scroll(function() {
        if ($(this).scrollTop() > 200) {
            $('.btn-up').fadeIn();
        } else {
            $('.btn-up').fadeOut();
        }
    });
    $(".scroll-up").on('click', '.btn-up',  function(e) {
        e.preventDefault();
        $('html, body').animate({scrollTop: 0}, 100);
    });
});
