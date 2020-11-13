

$(document).ready(function() {
    $(document).on('submit','#signupform',function(e){
    e.preventDefault();
    var us_email = $('input[name="email"]').val();
    var us_name =$('input[name="name"]').val();
    var us_password =$('input[name="password"]').val();
   

    var url="/signup?name="+us_name+"&email="+us_email+"&password="+us_password;
    var request = new XMLHttpRequest();
    request.onreadystatechange=function(){
          if(this.status==200 && this.readyState==4){
             if(request.responseText=="true"){
            alert("account created");

             }




          }
      };
      request.open("GET", url, true);
      request.send();
    })
    $(document).on('blur','input[name="email"]',function(){
        var us_email = $('input[name="email"]').val();

        var url="/checkemail?email="+us_email;
        var request = new XMLHttpRequest();
        request.onreadystatechange=function(){
              if(this.status==200 && this.readyState==4){
                 if(request.responseText=="true"){
                 $('input[name="submit"]').attr('disabled','true');
                 }
                 else{
                     $('input[name="submit"]').removeAttr('disabled');
                }
    
    
    
    
              }
          };
          request.open("GET", url, true);
          request.send();


    })



});