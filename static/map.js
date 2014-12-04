var map
var myLatlng
function initialize() {
   myLatlng = new google.maps.LatLng(30.61,-96.34);
    var mapOptions = {
        center: myLatlng,
        zoom: 8
    };
   map = new google.maps.Map(document.getElementById('map-container'),
        mapOptions);
    var marker1 = new google.maps.Marker({
        position: myLatlng,
        map: map,
        title: 'Hello World!',
        icon: "../static/badouthouse.png"
    });
    var marker = new google.maps.Marker({
        position: {lat:31.61,lng:-96.34},
        map: map,
        title: 'Hello World!',
        icon: "../static/goodouthouse.png"
    });
}
google.maps.event.addDomListener(window, 'load', initialize);
//console.log("you dawg i heard you like maps")
// var marker5 = new google.maps.Marker({
//        position: {lat:31.69,lng:-99.34},
//        map: map,
//        title: 'Hello!',
//        icon: "../static/goodouthouse.png"
//    });
function get_data() {
    console.log("test")
    $(document).ready(function(){
    $("button").click(function(){
    $.getJSON("/api/get_all",function(result){
    $.each(result, function(i, field){
    console.log(result)
});
});
});
});
}
  function addMarker() {
        $.getJSON("/api/get_all",function(data){
        $.each(data,function(key,value){
            var x=value.latitude;
            var y=value.longitude;
            var string = value.name;
            var string1= "is a sexy motherfucker";
            var contentString = '<div id="content">'+
            '<div id="siteNotice">'+
            '</div>'+
            '<h1 id="firstHeading" class="firstHeading">'+string+'</h1>'+
            '<div id="bodyContent">'+string1+
            '</div>'+
            '</div>';
            var infowindow = new google.maps.InfoWindow({
            content: contentString
            });
            myLatlng = new google.maps.LatLng(x,y);
            if(value.good > value.bad) {
                var marker = new google.maps.Marker({
                    position: myLatlng,
                    map: map,
                    title: string,
                    icon: "../static/goodouthouse.png"
                });
            } else {
                var marker = new google.maps.Marker({
                    position: myLatlng,
                    map: map,
                    title: string,
                    icon: "../static/badouthouse.png"
                });
            }
      google.maps.event.addListener(marker, 'click', function() {
        infowindow.open(map,marker);
      });

      });
      });  //end of json

  };