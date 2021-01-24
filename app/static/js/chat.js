var socket = io.connect('http://' + document.domain + ':' + location.port);
var chat_socket = io('http://' + document.domain + ':' + location.port + '/chat');
var room = $("#chat_room").text();

window.onload = function () {
	var chat_body = document.getElementById('chat_body');
	var last_msg = chat_body.lastChild.previousSibling;
	if (last_msg){
		var topPos = last_msg.offsetTop;
		document.getElementById('scrollbar_wrapper').scrollTop = topPos;}
}



function send_message(){
	var message = $("#message_input").val();
	if (!message){return;}
	var data =  {'user_id': $("#user_id").text(),'user_to_id': $("#user_to_id").text(), 'message': message};
	chat_socket.emit('message', data);
	$("#message_input").val("");
}

chat_socket.on('message_from_server', function(data)
{
	var msg = data['message'];
	var id_user_from = data['user_id'];
	var user_data = data['user_data'];
	// console.log(user_data);

	new_msg = document.createElement('li');
	if (id_user_from == $("#user_id").text()){
		$(new_msg).addClass('right');
		$(new_msg).html('<img src="'+ user_data['avatar'] +'" alt=""class="profile-photo-sm pull-right"><div class="chat-item"><div class="chat-item-header"><h5>'+ user_data['first_name'] +' '+ user_data['last_name'] +'</h5><small class="text-muted">'+ data['date_time'] +'</small></div><p>' +
		msg + '</p></div>');
	}
	else{
		$(new_msg).addClass('left');
		$(new_msg).html('<img src="'+ user_data['avatar'] +'" alt=""class="profile-photo-sm pull-left"><div class="chat-item"><div class="chat-item-header"><h5>'+ user_data['first_name'] +' '+ user_data['last_name'] +'</h5><small class="text-muted">'+ data['date_time'] +'</small></div><p>' +
		msg + '</p></div>');
	}

	$(new_msg).appendTo($("#chat_body"));

	topPos = new_msg.offsetTop;
	document.getElementById('scrollbar_wrapper').scrollTop = topPos;
});

chat_socket.on('connect', function()
{
	chat_socket.emit('join_room', {'room': room, 'user_id': $("#user_id").text(), 'user_to_id': $("#user_to_id").text()});
});

$(document).keypress(function(e) {
	var keycode = (e.keyCode ? e.keyCode : e.which);
	var input = document.getElementById("message_input");
	if (keycode == '13' && $('#message_input').is(':focus')) {
		send_message();
	}
});

$('#mesage_submit').on('click', function() {
	send_message();
});
