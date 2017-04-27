/*
*   Ray Slider
*   Author: Ahmed Brohi
*   http://raythemes.com
*/


(function ( $ ) {
    $.fn.rayslider = function(options) {

        var totalSlides = this.find('.rayslide').length;
        var $slides=this.find('.rayslide');
        var speed = options.speed;
        var bg = options.bgimgcontainer;
        var activeSlide=0;
        var navleft=options.navleft;
        var navright=options.navright;
        var slideTimeOut=0;

        $(navleft).click(function(){prevSlide();});
        $(navright).click(function(){nextSlide();});


        changeSlide(0);

        /*** change slide ***/

        function changeSlide(target){
            clearTimeout(slideTimeOut);

            var bgimg = $slides.eq(activeSlide).attr('data-bgimg');
            $(bg).attr('style','').removeClass().addClass(bgimg).animate({opacity:1},700);

            if(target>=totalSlides)
                activeSlide=0;

            if(target<0)
                activeSlide=totalSlides-1;
            $(bg).attr('style','').removeClass();

             bgimg = $slides.eq(activeSlide).attr('data-bgimg');
            $(bg).addClass(bgimg).animate({opacity:1},700);

            animateLayerIn($slides.eq(activeSlide).find('.animate'));
            slideTimeOut = setTimeout(function(){
                    animateLayerOut($slides.eq(activeSlide).find('.animate'));
                    setTimeout(function(){
                        var bgimg = $slides.eq(activeSlide).attr('data-bgimg');
                        $(bg).attr('style','').removeClass(bgimg);
                        activeSlide=activeSlide+1;
                        changeSlide(activeSlide);
                    },1200);
            },speed);

        }
        function animateLayerIn(target){
            $(target).each(function(){
                var delay = $(this).attr("data-delay");
                var speed = $(this).attr("data-speed");
                var slideIn="";
                var c=$(this).attr('class');
                $(this).attr('style','');
                $(this).attr('class',c);

                if($(this).hasClass("slide-right"))
                    slideIn="$(this).transition({x:'30%',opacity:1,delay:"+delay+"},"+speed+",'easeInExpo')";
                if($(this).hasClass("slide-left"))
                    slideIn="$(this).transition({x:'-30%',opacity:1,delay:"+delay+"},"+speed+",'easeInExpo')";
                if($(this).hasClass("slide-up"))
                    slideIn="$(this).transition({y:'-2%',opacity:1,delay:"+delay+"},"+speed+",'easeInExpo')";
                if($(this).hasClass("slide-down"))
                    slideIn="$(this).transition({y:'5%',opacity:1,delay:"+delay+"},"+speed+",'easeInExpo')";

                eval(slideIn);
            });

        }//function

        function animateLayerOut(target){
            $(target).each(function(){
                var delay = $(this).attr("data-delay");
                var speed = $(this).attr("data-speed");
                var slideOut="";


                if($(this).hasClass("slide-right"))
                    slideOut="$(this).transition({x:'80%',opacity:0,delay:"+delay+"},"+speed+",'easeInExpo')";
                if($(this).hasClass("slide-left"))
                    slideOut="$(this).transition({x:'-80%',opacity:0,delay:"+delay+"},"+speed+",'easeInExpo')";
                if($(this).hasClass("slide-up"))
                    slideOut="$(this).transition({y:'-250%',opacity:0,delay:"+delay+"},"+speed+",'easeInExpo')";
                if($(this).hasClass("slide-down"))
                    slideOut="$(this).transition({y:'250%',opacity:0,delay:"+delay+"},"+speed+",'easeInExpo')";

                eval(slideOut);
            });
        }//function

        function nextSlide(){
            $slides.eq(activeSlide).find('.animate').css('z-index','-1000');
            activeSlide=activeSlide+1;
            changeSlide(activeSlide);
        }

        function prevSlide(){
            $slides.eq(activeSlide).find('.animate').css('z-index','-1000');
            activeSlide=activeSlide-1;
            changeSlide(activeSlide);
        }

    };
}( jQuery ));

