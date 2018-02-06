$(document).ready(function(){
    console.log('document loaded')

$('img').click(function() {
    $("img").attr("data-alt-src");
    $(this).attr("src",$(this).attr("data-alt-src"));
 })
})