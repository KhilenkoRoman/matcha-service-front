io.connect(location.protocol +'//' + document.domain + ':' + location.port);
var notif_socket = io(location.protocol + '//' + document.domain + ':' + location.port + '/notifications');


notif_socket.on('check_notifications', function(data)
{
	var notifications = document.getElementById("notifications");
	var notif_horn = $("#notif_horn");
	if (!data){
		document.getElementById('notifications').innerHTML = "";
		notif_horn.addClass("none");
	}
	else {
		document.getElementById('notifications').innerHTML = "";
		data.forEach(function (item, i, data) {
			// console.log( i + ": " + item['notification'] + " (массив:" + data + ")" );
			var new_notif = document.createElement('li');
			new_notif.innerHTML = "<a>" + item['notification'] + "</a>";
			notifications.appendChild(new_notif);
		});
		var delete_notif = document.createElement('li');
		delete_notif.innerHTML = '<a href="" id="notification_red" onclick="notification_red()">Mark all as red</a>';
		notifications.appendChild(delete_notif);
		notif_horn.removeClass("none");
	}
});

notif_socket.on('update_notifications', function(data)
{
	// console.log(data);
	$.ajax({
		url: '/ajax_update_notifications',
		data: {'id_user': data},
		type: 'POST',
		success: function(response){
			var win = new Audio('http://' + document.domain + ':' + location.port + '/static/sounds/notification.mp3');
			win.play();
		},
		error: function(error)
		{
			console.log(error);
		}
	});
});


function notification_red() {
	event.preventDefault();

	$.ajax({
		url: '/ajax_clear_notifications',
		data: {},
		type: 'POST',
		success: function(response)
		{
			// console.log(response);
			if (response === "notifications_clear"){
				document.getElementById('notifications').innerHTML = "";
				$("#notif_horn").addClass("none");
			}
		},
		error: function(error)
		{
			console.log(error);
		}
	});}