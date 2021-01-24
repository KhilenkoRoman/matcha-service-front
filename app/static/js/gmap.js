function init_edit_Map() {
  let latitude = parseFloat($('#lat').val());
  let longitude = parseFloat($('#long').val());

  var uluru = {lat: latitude, lng: longitude};
  if (!document.getElementById('map_edit')){return};
  var map = new google.maps.Map(document.getElementById('map_edit'), {
	zoom: 10,
	center: uluru,
	zoomControl: true,
	scaleControl: false,
	scrollwheel: false,
	disableDoubleClickZoom: true
  });

  var marker = new google.maps.Marker({
	position: uluru,
	map: map,
	draggable:true,
	title:"Drag me!"
  });

  google.maps.event.addListener(marker, 'dragend', function (event) {
	  document.getElementById("lat").value = event.latLng.lat();
	  document.getElementById("long").value = event.latLng.lng();
  });

  $("#upd_loc_btn").click(function() {
  event.preventDefault();
  $.ajax({
			url: '/ajax_update_location',
			data: {'id_user': $("#user_id").text(), 'latitude': parseFloat($('#lat').val()), 'longitude': parseFloat($('#long').val())},
			type: 'POST',
			success: function (response) {
				console.log(response);
			},
			error: function (error) {
				console.log(error);
			}
  });
  });
}


function init_UNIT_Map() {
  var uluru = {lat: 50.46883805910163, lng: 30.462166049957204};
  if (!document.getElementById('UNIT_Map')){return};
  var map = new google.maps.Map(document.getElementById('UNIT_Map'), {
	zoom: 20,
	center: uluru,
	zoomControl: true,
	scaleControl: false,
	scrollwheel: false,
	disableDoubleClickZoom: true
  });

  var marker = new google.maps.Marker({
	position: uluru,
	map: map,
	draggable:true,
	title:"Drag me!"
  });
}


function map_people_nearby() {
  let latitude = parseFloat($('#self_latitude').text());
  let longitude = parseFloat($('#self_longitude').text());


  var uluru = {lat: latitude, lng: longitude};
  if (!document.getElementById('map_people_nearby')){return};
  var map = new google.maps.Map(document.getElementById('map_people_nearby'), {
	zoom: 10,
	center: uluru,
	zoomControl: true,
	scaleControl: false,
	scrollwheel: false,
	disableDoubleClickZoom: true
  });

  var marker = new google.maps.Marker({
	position: uluru,
	map: map,
	icon: {
		url: $('#avatar').text(),
		scaledSize: new google.maps.Size(32, 32)
	},
	title:$("#user_login").text()
  });

  let users = document.getElementsByClassName("nearby-user");

  for (var i = 0; i < users.length; i++) {
	  let user_photo = users[i].getElementsByClassName("profile-photo-lg")[0].src;
	  let longitude = parseFloat(users[i].getElementsByClassName("longitude")[0].innerHTML);
	  let latitude = parseFloat(users[i].getElementsByClassName("latitude")[0].innerHTML);
	  let name = users[i].getElementsByClassName("profile-link")[0].innerHTML;


	  let marker = new google.maps.Marker({
		position: {lat: latitude, lng: longitude},
		map: map,
		icon: {
			url: user_photo,
			scaledSize: new google.maps.Size(32, 32)
		},
		 title:name
		});

  }

  var myoverlay = new google.maps.OverlayView();
	 myoverlay.draw = function () {
		 this.getPanes().markerLayer.id='markerLayer';
	 };
  myoverlay.setMap(map);
}

function init_about_Map() {
  let latitude = parseFloat($('#about_latitude').text());
  let longitude = parseFloat($('#about_longitude').text());
  var uluru = {lat: latitude, lng: longitude};
  if (!document.getElementById('map_about')){return};
  var map = new google.maps.Map(document.getElementById('map_about'), {
	zoom: 12,
	center: uluru,
	zoomControl: true,
	scaleControl: false,
	scrollwheel: false,
	disableDoubleClickZoom: true
  });

  var marker = new google.maps.Marker({
	position: uluru,
	map: map,
  });
}