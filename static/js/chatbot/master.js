// $(function() {
//         $(".send-icon").click(function()
//             {
//                 var text_value = $(".chat-input").val();
//                 if(text_value != ""){
//                     $(".messages").append("<div class='outer-message'><div class='message my-message'>" + text_value + "</div></div>")
//                     $(".chat-input").val("");
//                     var myDiv = document.getElementById("style-1");
//                     myDiv.scrollTop = myDiv.scrollHeight;
//                 }
//             }
//         );
//
//         $(document).on('keypress', function(e) {
//             if(e.which == 13) {
//                 var text_value = $(".chat-input").val();
//                 if(text_value != ""){
//                     $(".messages").append("<div class='outer-message'><div class='message my-message'>" + text_value + "</div></div>")
//                     $(".chat-input").val("");
//                     var myDiv = document.getElementById("style-1");
//                     myDiv.scrollTop = myDiv.scrollHeight;
//                 }
//             }
//         });
// });
$(document).ready(function() {
    $('.send-icon').click(function() {
        $('#submit').click();
    });
});
