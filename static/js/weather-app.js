
document.getElementById("tomo").style.display="none";
document.getElementById("tonight").style.display="none";
document.getElementById("w").style.display="none";
document.getElementById("h").style.display="none";
document.getElementById("T").style.display="none";
document.getElementById("d").style.display="none";




$(function(){



    $('form#weather-search').on('submit',function(){

        var that=$(this),
          url = that.attr('action'),
          type=that.attr('method'),
          data={}; 
          that.find('[name]').each(function(index,value){
            var that=$(this),
            name=that.attr('name'),
            value=that.val()
            data[name]=value;
          });
          $.ajax({
              dataType:'json',
              url:url,
              type:type,
              data:data,
              success: function(response){
                function precise(x) {
                    return Number.parseFloat(x).toPrecision(2);
                  }
                  console.log(response);
                  t=precise(response.current);
                  w=response.wind;
                  h=response.humidity;
                  d=response.description;
                  icon=response.id;
                  l=response.location;
                  tn=response.tonight;
                  tomo=response.tomorrow;
                  nightIcon=response.tonight_id;
                  tomoIcon=response.tomo_id;
                  time=response.time;

                  if (time =="night"){
                      var ic="night";
                  }

                  else{
                      var ic="day"};
                // document.querySelector('.Temperature').textContent=t;
                $('.Temperature').unbind().empty().append(t + '&#8457;');
                $('#wind').unbind().empty().append(w+" mph");
                $('#humidity').unbind().empty().append(h+"%");
                $('.description').unbind().empty().append(d);
                $('#city-name').unbind().empty().append(l);
                $('#tonight-temp').unbind().empty().append(tn+'&#8457;');
                $('#tomorrow-temp').unbind().empty().append(tomo+'&#8457;').slideDown();
          

                

        
   
                i=document.createElement('i');
                iTwo=document.createElement('i');
                iThree=document.createElement('i');



                i.setAttribute("class","wi"+" wi-owm-"+ic+"-"+icon.toString()+" i");
                
                iTwo.setAttribute("class","wi"+" wi-owm-night-"+nightIcon.toString()+" i2");
                iThree.setAttribute("class","wi"+" wi-owm-day-"+tomoIcon.toString()+" i3");

                $('#icon').unbind().empty().append(i);
                $('#icon-2').unbind().empty().append(iTwo);
                $('#icon-3').unbind().empty().append(iThree);
       

                $( "#tomo" ).fadeIn( "slow", function() {
                    document.getElementById("tomo").style.display="block";
                    });

                $('#tonight').fadeIn( "slow", function() {
                    document.getElementById("tonight").style.display="block";
                    });
                $('#w').fadeIn( "slow", function() {
                    document.getElementById("w").style.display="block";
                    });
                $('#h').fadeIn( "slow", function() {
                    document.getElementById("h").style.display="block";
                    });
                
                $('#T').fadeIn( "slow", function() {
                    document.getElementById("T").style.display="block";
                    });
                    
                $('#d').fadeIn( "slow", function() {
                    document.getElementById("d").style.display="block";
                    });
                 }

            });  
            return false;
                });                  
                
})