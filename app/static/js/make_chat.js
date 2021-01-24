function chat_start()
{
	event.preventDefault();
	var chat_to = event.srcElement.parentNode.getElementsByClassName("chat_login_to")[0].innerHTML;
	var chat_from = $("#user_login").text();

	console.log(chat_from);

	$.ajax({
		url: "/ajax_create_chat",
		data: {'chat_to': chat_to, 'chat_from': chat_from},
		type: 'POST',
		success: function(response)
		{
			var form = $('<form class="none" action="/chat" method="post">' +
			'<input type="text" name="room_name" value="' + response + '" />' +
			'<input type="text" name="chat_to" value="' + chat_to + '" />' +
			'<input type="text" name="chat_from" value="' + chat_from + '" /></form>');
			$('body').append(form);
			form.submit();
		},
		error: function(error)
		{
			console.log(error);
		}
	});
}