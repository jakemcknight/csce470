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