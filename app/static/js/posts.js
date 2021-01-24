var user_id = $("#user_id")[0].innerText;

function create_post_action(form) {
	let content = $("#content");
	let no_posts = $("#no_posts");

	$.post('/ajax_create_post', {
		'content': content.val(),
		'user_id': user_id
	}).done(function (resp) {
		content.val("");
		if (resp !== "Fail") {
			no_posts.remove();
			let all_posts = $("#all_posts");
			let data = '<div class="post-content" id="post' + resp.id_post + '"><!--Post Date-->' +
				'<div class="post-date hidden-xs hidden-sm">' +
					'<h5>' + resp.user_first_name + '</h5>' +
					'<p class="text-grey">' + resp.date_creation + '</p>' +
				'</div><!--Post Date End-->' +
				'<div class="post-container">' +
					'<div class="btn text-red dell" onclick="dell_post(' + resp.id_post + ')">X</div>' +
					'<img src="' + resp.user_avatar + '" alt="user" class="profile-photo-md pull-left" />' +
					'<div class="post-detail">' +
						'<div class="user-info">' +
							'<h5>' +
								'<a href="/user/id' + resp.auth_id + '" class="profile-link">' + resp.user_first_name + ' ' + resp.user_last_name + '</a>' +
								'<span class="following">following</span>' +
							'</h5>' +
							'<p class="text-muted">Published a ' + resp.type + ' on a ' + resp.time_creation + '</p>' +
						'</div>' +
						'<div class="reaction">' +
							'<a class="btn text-green" id="like' + resp.id_post + '" onclick="like(' + resp.auth_id + ', ' + resp.id_post + '); return false;">' +
								'<i class="icon ion-thumbsup"></i> <span>0</span>' +
							'</a>' +
							'<a class="btn text-red" id="dislike' + resp.id_post + '" onclick="dislike(' + resp.auth_id + ', ' + resp.id_post + '); return false;">' +
								'<i class="fa fa-thumbs-down"></i> <span>0</span>' +
							'</a>' +
						'</div>' +
						'<div class="line-divider"></div>' +
						'<div class="post-text">' +
							'<p>' + resp.content + '</p>' +
						'</div>' +
						'<div class="line-divider"></div>' +
						'<div id="all_comments' + resp.id_post + '"></div>' +
						'<form method="post" onsubmit="add_comment(this); return false;">' +
							'<div class="post-comment">' +
								'<img src="' + resp.user_avatar + '" class="profile-photo-sm" />' +
								'<input type="hidden" name="id_post" value="' + resp.id_post + '">' +
								'<input type="text" name="comment" class="form-control" placeholder="Post a comment">' +
							'</div>' +
						'</form>' +
					'</div>' +
				'</div>' +
			'</div>';
			all_posts.prepend(data);
		}
	});
}

function dell_post(id_post) {
	$.post('/ajax_dell_post/', {
		'id_post': id_post
	}).done(function (resp) {
		console.log(resp);
		if (resp === "deleted") {
			let post = $("#post" + id_post);
			post.remove();
		}
	});
}
