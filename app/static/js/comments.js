function add_comment(form) {
	let id_post = form.id_post.value;
	let text = form.comment.value;

	$.post('/ajax_add_comment/', {
		'id_post': id_post,
		'text': text
	}).done(function (resp) {
		form.comment.value = "";
		if (resp !== "False"){
			let all_comments = $('#all_comments' + resp.id_post);
			let data = "<div class=\"post-comment\" id='comment" + resp.id_comment + "'>" +
				"<img src=\"" + resp.user_avatar + "\" class=\"profile-photo-sm\" />" +
				"<a href=\"/user/id" + resp.id_user + "\" class=\"profile-link\">" + resp.user_first_name + "</a>" +
				"<p>&nbsp;&nbsp;" + resp.text + "</p>" +
				"<div class=\"btn text-red dell\" onclick=\"dell_comment(" + resp.id_comment + ")\">X</div>" +
			"</div>" +
			"<div class=\"line-divider\" id=\"divider" + resp.id_comment + "\"></div>";
			all_comments.prepend(data);
		}
	});
}

function dell_comment(id_comment) {
	$.post('/ajax_dell_comment/', {
		'id_comment': id_comment
	}).done(function (resp) {
		if (resp === "deleted") {
			let comment = $("#comment" + id_comment);
			let divider = $("#divider" + id_comment);

			comment.remove();
			divider.remove();
		}
	});
}
