$(window).scroll(function () {
    if ($(this).scrollTop() >= 500) {
      $('.bd-navbar').addClass('bd-navbar__fixed sticky-top');
    } else {
      $('.bd-navbar').removeClass('bd-navbar__fixed sticky-top');
    }
     });