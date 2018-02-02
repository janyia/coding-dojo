			
	$(document).ready(function(){
		console.log('document loaded')
    
    $('.click').click(function(){
        alert("testing alert")
    })
    $('.click').click(function(){
        console.log('click event')
    })
    $('.hide').click(function(){
        $(".hide").hide()
    })
    $('.show').click(function(){
        $(".hide").show()
    })
    $('.toggle').click(function(){
        $(".hide").toggle()
    })
    $('.slideDown').click(function(){
        $(".hidden").slideDown()
    })
    $('.slideUp').click(function(){
        $("#slideUp").slideUp()
    })
    $('.slideToggle').click(function(){
        $("#slideToggle").slideToggle()
    })
    $('.fadeIn').click(function(){
        $("#fadeIn").fadeIn()
    })
    $('.fadeOut').click(function(){
        $("#fadeOut").fadeOut()
    })
    $('.addClass').click(function(){
        $("#addClass").addClass("green")
    })
    $('.before').click(function(){
        $("#before").before("<h1>before</h1>")
    })
    $('.after').click(function(){
        $("#after").after("<h1>after</h1>")
    })
    $('.append').click(function(){
        $("#append").append("<span>I am a span tag</span>")
    })
    $('.html').click(function(){
        $("#html").html("<h1>Hello</h1>")
    })
    $('.attr').click(function(){
        var classVal = $("#attr").attr("class")
        $('#attr').append(classVal)
    })
    $('.attr2').click(function(){
        $("#attr").attr("class", "red")
    })
    $('.val').click(function(){
        console.log($("#val").val())
    })
    $('.val2').click(function(){
        $('#val').val("hello")
    })
    $('.text').click(function(){
        $("#text").text("hello")
    })
    $(".data").click(function(){
        $("#data").text("new data")
    })
    })

