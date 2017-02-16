$(document).ready(function(){
    $('.upvoting').hover(function(){
        $(this).css('cursor', 'pointer');
    });
    $('.downvoting').hover(function(){
        $(this).css('cursor', 'pointer');
    });
    $('.flagging').hover(function(){
        $(this).css('cursor', 'pointer');
    });

    $(".content-section").typed({
        strings: ["Suggestion Box. ", "Put your suggestions and comments there and React to a friend's Suggestion"],
        typeSpeed: 0
    });

    if($("#pwd").val() != $("#cfmpwd").val()){

    }

});


