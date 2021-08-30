(function ($) {

//forgotpassword functions
 $("#forgotpassword").click(function(){
  refreshmodal("forgotpassword")

  var registrationid=$("#registrationid").val().trim()
  var boardtype=$("#board_type").val().trim()
  if(registrationid.length>0 && boardtype.length>0){
  var response=postAjax("forgotpassword",{'registrationid':registrationid,'boardtype':boardtype})
  if(response['modalcode']=='securityque'){
  $('.okbutton').attr('id','securityque')
  displaynormal('forgotpassword',response)
  }else{
    displayerror('forgotpassword',response)

  }

  }else{
    alert("Please fill the required feilds!")
  }

  //displaynormal('forgotpassword',response)




  });
//submit functions........
 $("#submitBtn").click(function(){
  refreshmodal("submitBtn")
      var registrationid=$("#registrationid").val().trim()
      var boardtype=$("#board_type").val().trim()
  if(registrationid.length>0 && boardtype.length>0){
  var response=postAjax("verifyRegistrationId",{'registrationid':registrationid,'boardtype':boardtype})
  if(response["modalcode"]=='feildrequired' || response["modalcode"]=='invalid'){
  displayerror('submitBtn',response)
  }else{
  if(response['modalcode']=='securityque'){
    $('.okbutton').attr('id','securityque')

  }
     displaynormal('submitBtn',response)


  }

  }else{
  alert("Please fill the required feilds!")

  }

//Security Question clicked
 $(document).find("#securityque").click(function(){
alert("calling")
})



    });



    // USE STRICT
    "use strict";

    $(".form-radio .radio-item").click(function(){
        //Spot switcher:
        $(this).parent().find(".radio-item").removeClass("active");
        $(this).addClass("active");
    });
  
    $('#time').parent().append('<ul class="list-item" id="newtime" name="time"></ul>');
    $('#time option').each(function(){
        $('#newtime').append('<li value="' + $(this).val() + '">'+$(this).text()+'</li>');
    });
    $('#time').remove();
    $('#newtime').attr('id', 'time');
    $('#time li').first().addClass('init');
    $("#time").on("click", ".init", function() {
        $(this).closest("#time").children('li:not(.init)').toggle();
    });

    $('#food').parent().append('<ul class="list-item" id="newfood" name="food"></ul>');
    $('#food option').each(function(){
        $('#newfood').append('<li value="' + $(this).val() + '">'+$(this).text()+'</li>');
    });
    $('#food').remove();
    $('#newfood').attr('id', 'food');
    $('#food li').first().addClass('init');
    $("#food").on("click", ".init", function() {
        $(this).closest("#food").children('li:not(.init)').toggle();
    });
    
    var allOptions = $("#time").children('li:not(.init)');
    $("#time").on("click", "li:not(.init)", function() {
        allOptions.removeClass('selected');
        $(this).addClass('selected');
        $("#time").children('.init').html($(this).html());
        allOptions.toggle();
    });

    var FoodOptions = $("#food").children('li:not(.init)');
    $("#food").on("click", "li:not(.init)", function() {
        FoodOptions.removeClass('selected');
        $(this).addClass('selected');
        $("#food").children('.init').html($(this).html());
        FoodOptions.toggle();
    });




})(jQuery);

function showloader(){
$(".loader").css('visibility', '')
 $(".loader").css('visibility', 'visible')
 }

function hideloader(){
$(".loader").css("visibility", "")
 $(".loader").css("visibility", "hidden")
 }

function displayerror(id,response){
 $('.modal-title').html(response["header"]);
   $('.modal-body').html(response["body"]);
   $('.modal-dialog').css('width','');
   $('.modal-dialog').css('width','400px');
   $("#"+id).attr("data-toggle", "modal");


 }
 function displaynormal(id,response){
 $('.modal-title').html(response["header"]);
   $('.modal-body').html(response["body"]);
   $('.modal-dialog').css('width','');
   $("#"+id).attr("data-toggle", "modal");

 }
 function refreshmodal(id){
  $("#"+id).attr("data-toggle", "");
    $('.okbutton').attr('id','')

 }

