"use strict";

(function ($) {
  "use strict";

  /*--------------------------------------------------------------
   [Table of contents]
  
  nesmee PRELOADER JS INIT
  nesmee HEADER SEARCH JS INIT
  nesmee STICKY MENU JS INIT
  nesmee MENU SIDEBAR JS INIT
  nesmee SKILLBAR JS INIT
  nesmee HERO SLIDER INIT
  nesmee FOUR COLUMN SLIDER INIT
  nesmee THREE COLUMN SLIDER INIT
  nesmee FOUR COLUMN SLIDER TWO INIT
  nesmee TWO COLUMN SLIDER INIT
  nesmee ONE COLUMN SLIDER INIT
  nesmee THREE COLUMN SLIDER TWO INIT
  nesmee BRAND SLIDER INIT
  nesmee COUNTER JS INIT
  nesmee COUNTER JS TWO INIT
  nesmee MAP JS
   
  -------------------------------------------------------------------*/

  /*--------------------------------------------------------------
  CUSTOM PRE DEFINE FUNCTION
  ------------------------------------------------------------*/
  /* is_exist() */
  jQuery.fn.is_exist = function () {
    return this.length;
  };
  $(function () {
    /*--------------------------------------------------------------
    nesmee PRELOADER JS INIT
    --------------------------------------------------------------*/
    $(".nesmee-preloader-wrap").fadeOut(500);

    /*--------------------------------------------------------------
    nesmee HEADER SEARCH JS INIT
    ------------------------------------------------------------*/
    $(".nesmee-header-search, .nesmee-header-search-close, .search-overlay").click(function () {
      $(".nesmee-header-search-section, .search-overlay").toggleClass("open");
    });

    /*--------------------------------------------------------------
    nesmee STICKY MENU JS INIT
    --------------------------------------------------------------*/
    $(window).on('scroll', function () {
      if ($(window).scrollTop() > 50) {
        $('#sticky-menu').addClass('sticky-menu');
      } else {
        $('#sticky-menu').removeClass('sticky-menu');
      }
    });

    /*--------------------------------------------------------------
    nesmee MENU SIDEBAR JS INIT
    --------------------------------------------------------------*/
    $(".nesmee-header-barger").on("click", function (e) {
      $(".nesmee-sidemenu-column, .offcanvas-overlay").addClass("active");
      event.preventDefault(e);
    });
    $(".nesmee-sidemenu-close, .offcanvas-overlay").on("click", function () {
      $(".nesmee-sidemenu-column, .offcanvas-overlay").removeClass("active");
    });

    /*--------------------------------------------------------------
    nesmee HERO SLIDER INIT
    --------------------------------------------------------------*/
    /*----------- Global Slider ----------*/
    $(".global-carousel").each(function () {
      var carouselSlide = $(this);
      function d(data) {
        return carouselSlide.data(data);
      }
    });
    /*----------- Custom Animaiton For Slider ----------*/

    $('[data-ani-duration]').each(function () {
      var durationTime = $(this).data('ani-duration');
      $(this).css('animation-duration', durationTime);
    });
    $('[data-ani-delay]').each(function () {
      var delayTime = $(this).data('ani-delay');
      $(this).css('animation-delay', delayTime);
    });
    $('[data-ani]').each(function () {
      var animaionName = $(this).data('ani');
      $(this).addClass(animaionName);
      $('.slick-slide [data-ani]').addClass('slider-animated');
    });
    $('.global-carousel').on('afterChange', function (event, slick, currentSlide, nextSlide) {
      $(slick.$slides).find('[data-ani]').removeClass('slider-animated');
      $(slick.$slides[currentSlide]).find('[data-ani]').addClass('slider-animated');
    });
    var hero_slider = $('.nesmee-hero-slider');
    if (hero_slider.is_exist()) {
      hero_slider.slick({
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: true,
        dots: false,
        autoplay: false,
        speed: 800,
        lazyLoad: 'progressive',
        prevArrow: '<button class="slide-arrow nesmee-hero-next"><i class="ri-arrow-left-s-line"></i></button>',
        nextArrow: '<button class="slide-arrow nesmee-hero-prev"><i class="ri-arrow-right-s-line"></i></button>'
      }).slickAnimation();
    }

    /*--------------------------------------------------------------
    nesmee FOUR COLUMN SLIDER INIT
    --------------------------------------------------------------*/
    var four_column_slider = $('.nesmee-4column-slider');
    if (four_column_slider.is_exist()) {
      four_column_slider.slick({
        infinite: true,
        slidesToShow: 4,
        slidesToScroll: 1,
        arrows: false,
        dots: true,
        autoplay: false,
        centerMode: true,
        centerPadding: '300px',
        responsive: [{
          breakpoint: 1600,
          settings: {
            slidesToShow: 3,
            centerPadding: '250px'
          }
        }, {
          breakpoint: 1399,
          settings: {
            slidesToShow: 3,
            centerPadding: '150px'
          }
        }, {
          breakpoint: 1199,
          settings: {
            slidesToShow: 3,
            centerPadding: '100px'
          }
        }, {
          breakpoint: 992,
          settings: {
            slidesToShow: 2,
            centerPadding: '100px'
          }
        }, {
          breakpoint: 768,
          settings: {
            slidesToShow: 1,
            centerPadding: '100px'
          }
        }, {
          breakpoint: 575,
          settings: {
            slidesToShow: 1,
            centerPadding: '0px'
          }
        }]
      });
    }

    /*--------------------------------------------------------------
    nesmee THREE COLUMN SLIDER INIT
    --------------------------------------------------------------*/
    var three_column_slider = $('.nesmee-3column-slider');
    if (three_column_slider.is_exist()) {
      three_column_slider.slick({
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 1,
        arrows: false,
        dots: true,
        autoplay: false,
        centerMode: true,
        centerPadding: '100px',
        responsive: [{
          breakpoint: 1399,
          settings: {
            slidesToShow: 2
          }
        }, {
          breakpoint: 850,
          settings: {
            slidesToShow: 1,
            centerPadding: '70px'
          }
        }, {
          breakpoint: 575,
          settings: {
            slidesToShow: 1,
            centerPadding: '0px'
          }
        }]
      });
    }

    /*--------------------------------------------------------------
    nesmee FOUR COLUMN SLIDER TWO INIT
    --------------------------------------------------------------*/
    var four_column_slider2 = $('.nesmee-4column-slider2');
    if (four_column_slider2.is_exist()) {
      four_column_slider2.slick({
        infinite: true,
        slidesToShow: 4,
        slidesToScroll: 1,
        arrows: false,
        dots: true,
        autoplay: false,
        responsive: [{
          breakpoint: 1399,
          settings: {
            slidesToShow: 3
          }
        }, {
          breakpoint: 1199,
          settings: {
            slidesToShow: 2
          }
        }, {
          breakpoint: 768,
          settings: {
            slidesToShow: 1
          }
        }]
      });
    }

    /*--------------------------------------------------------------
    nesmee TWO COLUMN SLIDER INIT
    --------------------------------------------------------------*/
    var two_column_slider = $('.nesmee-2column-slider');
    if (two_column_slider.is_exist()) {
      two_column_slider.slick({
        infinite: true,
        slidesToShow: 2,
        slidesToScroll: 1,
        arrows: false,
        dots: true,
        autoplay: false,
        responsive: [{
          breakpoint: 991,
          settings: {
            slidesToShow: 1
          }
        }]
      });
    }

    /*--------------------------------------------------------------
    nesmee ONE COLUMN SLIDER INIT
    --------------------------------------------------------------*/
    var t_one_column_slider = $('.nesmee-1column-slider');
    if (t_one_column_slider.is_exist()) {
      t_one_column_slider.slick({
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: true,
        dots: false,
        autoplay: false,
        speed: 800,
        prevArrow: '<button class="slide-arrow nesmee-t-next"><i class="ri-arrow-left-s-line"></i></button>',
        nextArrow: '<button class="slide-arrow nesmee-t-prev"><i class="ri-arrow-right-s-line"></i></button>'
      });
    }

    /*--------------------------------------------------------------
    nesmee THREE COLUMN SLIDER TWO INIT
    --------------------------------------------------------------*/
    var three_column_slider2 = $('.nesmee-3column-slider2');
    if (three_column_slider2.is_exist()) {
      three_column_slider2.slick({
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 1,
        arrows: false,
        dots: true,
        autoplay: false,
        responsive: [{
          breakpoint: 1299,
          settings: {
            slidesToShow: 2
          }
        }, {
          breakpoint: 768,
          settings: {
            slidesToShow: 1
          }
        }]
      });
    }

    /*--------------------------------------------------------------
    nesmee BRAND SLIDER INIT
    --------------------------------------------------------------*/
    var nesmee_brand_slider = $('.nesmee-brand-slider');
    if (nesmee_brand_slider.is_exist()) {
      nesmee_brand_slider.slick({
        infinite: true,
        slidesToShow: 5,
        slidesToScroll: 1,
        arrows: false,
        dots: false,
        autoplay: true,
        autoplaySpeed: 0,
        speed: 6000,
        cssEase: 'linear',
        pauseOnHover: true,
        adaptiveHeight: true,
        responsive: [{
          breakpoint: 1199,
          settings: {
            slidesToShow: 3
          }
        }, {
          breakpoint: 767,
          settings: {
            slidesToShow: 2
          }
        }]
      });
    }

    /*--------------------------------------------------------------
    nesmee COUNTER JS INIT
    --------------------------------------------------------------*/
    var nesmee_counter = $('#nesmee-counter');
    if (nesmee_counter.is_exist()) {
      var a = 0;
      $(window).scroll(function () {
        var oTop = $(nesmee_counter).offset().top - window.innerHeight;
        if (a == 0 && $(window).scrollTop() > oTop) {
          $('.nesmee-counter').each(function () {
            var $this = $(this),
              countTo = $this.attr('data-percentage');
            $({
              countNum: $this.text()
            }).animate({
              countNum: countTo
            }, {
              duration: 4000,
              easing: 'swing',
              step: function step() {
                $this.text(Math.floor(this.countNum));
              },
              complete: function complete() {
                $this.text(this.countNum);
              }
            });
          });
          a = 1;
        }
      });
    }

    /*--------------------------------------------------------------
    nesmee COUNTER JS TWO INIT
    --------------------------------------------------------------*/
    var nesmee_counter2 = $('#nesmee-counter2');
    if (nesmee_counter2.is_exist()) {
      var a = 0;
      $(window).scroll(function () {
        var oTop = $(nesmee_counter2).offset().top - window.innerHeight;
        if (a == 0 && $(window).scrollTop() > oTop) {
          $('.nesmee-counter2').each(function () {
            var $this = $(this),
              countTo = $this.attr('data-percentage');
            $({
              countNum: $this.text()
            }).animate({
              countNum: countTo
            }, {
              duration: 4000,
              easing: 'swing',
              step: function step() {
                $this.text(Math.floor(this.countNum));
              },
              complete: function complete() {
                $this.text(this.countNum);
              }
            });
          });
          a = 1;
        }
      });
    }
    /*--------------------------------------------------------------
    nesmee AOS ANIMATION JS INIT
    --------------------------------------------------------------*/

    AOS.init({
      once: true // Ensure animations can trigger multiple times
    });
  }); /*End document ready*/

  $(window).on("resize", function () {}); // end window resize

  $(window).on('load', function () {}); // End window LODE

  /*--------------------------------------------------------------
  nesmee MAP JS
  ------------------------------------------------------------*/
  var google_map = $('#map');
  if (google_map.is_exist()) {
    var init = function init() {
      var mapOptions = {
        zoom: 11,
        scrollwheel: false,
        navigationControl: false,
        mapTypeControl: false,
        scaleControl: false,
        draggable: true,
        disableDefaultUI: true,
        center: new google.maps.LatLng(40.6700, -73.9400),
        styles: [{
          "featureType": "landscape.man_made",
          "elementType": "geometry",
          "stylers": [{
            "color": "#f7f1df"
          }]
        }, {
          "featureType": "landscape.natural",
          "elementType": "geometry",
          "stylers": [{
            "color": "#d0e3b4"
          }]
        }, {
          "featureType": "landscape.natural.terrain",
          "elementType": "geometry",
          "stylers": [{
            "visibility": "off"
          }]
        }, {
          "featureType": "poi",
          "elementType": "labels",
          "stylers": [{
            "visibility": "off"
          }]
        }, {
          "featureType": "poi.business",
          "elementType": "all",
          "stylers": [{
            "visibility": "off"
          }]
        }, {
          "featureType": "poi.medical",
          "elementType": "geometry",
          "stylers": [{
            "color": "#fbd3da"
          }]
        }, {
          "featureType": "poi.park",
          "elementType": "geometry",
          "stylers": [{
            "color": "#bde6ab"
          }]
        }, {
          "featureType": "road",
          "elementType": "geometry.stroke",
          "stylers": [{
            "visibility": "off"
          }]
        }, {
          "featureType": "road",
          "elementType": "labels",
          "stylers": [{
            "visibility": "off"
          }]
        }, {
          "featureType": "road.highway",
          "elementType": "geometry.fill",
          "stylers": [{
            "color": "#ffe15f"
          }]
        }, {
          "featureType": "road.highway",
          "elementType": "geometry.stroke",
          "stylers": [{
            "color": "#efd151"
          }]
        }, {
          "featureType": "road.arterial",
          "elementType": "geometry.fill",
          "stylers": [{
            "color": "#ffffff"
          }]
        }, {
          "featureType": "road.local",
          "elementType": "geometry.fill",
          "stylers": [{
            "color": "black"
          }]
        }, {
          "featureType": "transit.station.airport",
          "elementType": "geometry.fill",
          "stylers": [{
            "color": "#cfb2db"
          }]
        }, {
          "featureType": "water",
          "elementType": "geometry",
          "stylers": [{
            "color": "#a2daf2"
          }]
        }]
      };
      var mapElement = document.getElementById('map');
      var map = new google.maps.Map(mapElement, mapOptions);
      var marker = new google.maps.Marker({
        position: new google.maps.LatLng(40.6700, -73.9400),
        map: map,
        // icon: 'assets/images/all-img/contact/map.png',
        title: 'nesmee'
      });
      var contentString = '<div id="content">' + '<div id="tpw">' + '<h3>nesmee' + '</div>';
      var infowindow = new google.maps.InfoWindow({
        content: contentString,
        maxWidth: 280
      });
      marker.setAnimation(google.maps.Animation.BOUNCE);
      setTimeout(function () {
        marker.setAnimation(null);
      }, 750); //time it takes for one bounce   

      google.maps.event.addListener(marker, 'click', function () {
        infowindow.open(map, marker);
      });
    };
    google.maps.event.addDomListener(window, 'load', init);
  }
})(jQuery);