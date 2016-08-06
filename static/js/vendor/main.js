$(document).ready(function(){
    $("a[class^='new']").click(function () {
        $(this).siblings().removeClass('underline');
        $(this).toggleClass('underline');
     });
 }