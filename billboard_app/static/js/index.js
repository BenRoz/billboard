var board = {};

board.start = function(){
    $(document).ready(function(){
        $(".send_msg_btn").bind("click",board.createnewpost);
        $(".del.msg_btn").bind("click",board.delete_post);
        $(".cancel_msg_btn").bind("click",board.back_to_billboard);
        $(".add_msg_btn").bind("click",board.hide_msg);

    })


};


board.hide_msg = function (){
    $(".no_msg_div").css("display", "none");
    $('#form_section').css("display", "flex");
}


board.createnewpost = function(){
    var title = $(".form_header").val();
    var msg = $(".form_text").val();
    var author = $(".form_author").val();
    if (!title || !msg || !author){
        bad_form = $('<div/>').text("Please fill all form before submitting");
        bad_form.appendTo(".form").attr("id","form_error");

    }else {
        $('#form_section').slideUp();
        $.ajax("/sentmsg", {
            type: "POST",
            data: {
                "title": title,
                "msg": msg,
                "author": author
            },
            success: function (data) {
                $("#posts_holder").html(data+$("#posts_holder").html());
                $(".form_header").val("");
                $(".form_text").val("");
                $(".form_author").val("");
                $(".del.msg_btn").bind("click",board.delete_post);
            }
        });
    }
};


board.delete_post = function(){
        $(this).closest(".msg_div").slideUp();
        $.ajax("/post/" +this.id + "/", {
            type: "POST",
            success: function (data) {
                console.log("success")

            }
        });
};

board.back_to_billboard = function () {
    $('#posts_holder').slideDown();
    $('#form_section').slideUp();
}

board.start();