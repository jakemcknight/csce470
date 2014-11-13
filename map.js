/**
 * Created by Alex on 11/13/2014.
 */
function initialize() {
    var myLatlng = new google.maps.LatLng(30.61,-96.34);
    var mapOptions = {
        center: myLatlng,
        zoom: 8
    };
    var map = new google.maps.Map(document.getElementById('map-container'),
        mapOptions);
    var marker1 = new google.maps.Marker({
        position: myLatlng,
        map: map,
        title: 'Hello World!',
        icon: "static/badouthouse.png"
    });
    var marker = new google.maps.Marker({
        position: {lat:31.61,lng:-96.34},
        map: map,
        title: 'Hello World!',
        icon: "static/goodouthouse.png"
    });
    var infowindow = new google.maps.InfoWindow();
    google.maps.event.addListener(marker, 'click', function() {
        infowindow.open(map,myLatlng);
    });
}
google.maps.event.addDomListener(window, 'load', initialize);