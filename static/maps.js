p = new google.maps.Polyline(null);

function initialize() {
    var myLatlng = new google.maps.LatLng(40.7143528,-73.90597309999999);
    var mapOptions = {
	zoom: 13,
	center: myLatlng
    }
    map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

    for(x=0;x<addr.length;x++){
	var marker = new google.maps.Marker({
	    position: new google.maps.LatLng(addr[x][1],addr[x][2]),
	    map: map,
	    title: addr[x][0]
	});
	google.maps.event.addListener(marker,"click",function(){
	    showData(this.title);
	});
    }
}

google.maps.event.addDomListener(window, 'load', initialize);



function showData(n){
    $.get("teacherjs-"+n.replace(" ","+"),function(d){
	curPath = google.maps.geometry.encoding.decodePath(d.split(" ")[0])
	$("#sidebar").html(d.replace(d.split(" ")[0],""))
    });
}

function viewTransit(){
    p.setMap(null);
    p = new google.maps.Polyline({
	path: curPath,
	geodesic: true,
	strokeColor: '#0000ff',
	strokeOpacity: 1.0,
	strokeWeight: 4
    });

    p.setMap(map);
}