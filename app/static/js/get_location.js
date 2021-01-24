function getLocation() {
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(showPosition, showError);
	} else {
		console.log("Geolocation is not supported by this browser.");
	}
}

function showPosition(position) {
	console.log(position.coords.latitude);
	console.log(position.coords.longitude);

	$.ajax({
		url: '/ajax_set_location',
		data: {'id_user': $("#user_id").text(), 'latitude': position.coords.latitude, 'longitude': position.coords.longitude},
		type: 'POST',
		success: function(response)
		{
			console.log(response);
		},
		error: function(error)
		{
			console.log(error);
		}
	});
}

function showError(error) {
	$.getJSON('https://json.geoiplookup.io/api?callback=?', function(data) {
		console.log(data.latitude);
		console.log(data.longitude);

		$.ajax({
		url: '/ajax_set_location',
		data: {'id_user': $("#user_id").text(), 'latitude': data.latitude, 'longitude': data.longitude},
		type: 'POST',
		success: function(response)
		{
			console.log(response);
		},
		error: function(error)
		{
			console.log(error);
		}
	});
	});
}

window.onload = getLocation();

// var JSON.stringify(data, null, 2);});