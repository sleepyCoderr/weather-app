



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
                  
                  t=precise(response.temp);
                  w=response.wind;
                  h=response.humidity;
                  d=response.description;
                  icon=response.id;
                  l=response.location;
                  tn=response.min_temp;
                // document.querySelector('.Temperature').textContent=t;
                $('.Temperature').unbind().empty().append(t + '&#8457;');
                $('#wind').unbind().empty().append(w+" mph");
                $('#humidity').unbind().empty().append(h+"%");
                $('.description').unbind().empty().append(d);
                $('#city-name').unbind().empty().append(l);
                $('#tonight-temp').unbind().empty().append(tn+'&#8457;');


                // var iconDom=document.querySelector('.wi');                
                // document.getElementById("myDIV").className="wi-owm-"+icon.toString(); 
                // var node=document.getElementById("#icon")
                // i=document.createElement('i');
                // var iconDOM=i.setAttribute("class","wi"+ "wi-owm-"+icon.toString());
   
                i=document.createElement('i');
                i.setAttribute("class","wi"+" wi-owm-day-"+icon.toString());
                // document.getElementById("icon").appendChild(i); 
                $('#icon').unbind().empty().append(i);
                              }

            });  
            return false;
                }).slideDown();                  
                
})