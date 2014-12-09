var map
var myLatlng

var markers = [];

function initialize() {
   myLatlng = new google.maps.LatLng(30.61,-96.34);
    var mapOptions = {
        center: myLatlng,
        zoom: 8
    };
   map = new google.maps.Map(document.getElementById('map-container'),
        mapOptions);
}
google.maps.event.addDomListener(window, 'load', initialize);

function addMarker(search) {
    for(var i=0; i < markers.length; i++){
        markers[i].setMap(null);
    }
    $.getJSON("/api/search/zip/"+search,function(data){
        $.each(data.results,function(key,value){
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
                markers.push(marker);
            } else {
                var marker = new google.maps.Marker({
                    position: myLatlng,
                    map: map,
                    title: string,
                    icon: "../static/badouthouse.png"
                });
                markers.push(marker);
            }
      google.maps.event.addListener(marker, 'click', function() {
        infowindow.open(map,marker);
      });

      });
      });  //end of json

};