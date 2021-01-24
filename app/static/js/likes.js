function like(auth_id, post_id) {
	$.post('/ajax_like/', {
		'post_id': post_id
	}).done(function (resp) {
		let like = $('#like' + post_id);
		let c_like = $('#like' + post_id + ' span');
		if (resp === "liked") {
			like.removeClass('text-green');
			c_like[0].innerText = parseInt(c_like[0].innerText) + 1;
		} else if (resp === "unliked") {
			like.addClass('text-green');
			c_like[0].innerText = parseInt(c_like[0].innerText) - 1;
		}
	});
}

function dislike(auth_id, post_id) {
	$.post('/ajax_dislike/', {
		'post_id': post_id
	}).done(function (resp) {
		let dislike = $('#dislike' + post_id);
		let c_dislike = $('#dislike' + post_id + ' span');
		if (resp === "disliked") {
			dislike.removeClass('text-red');
			c_dislike[0].innerText = parseInt(c_dislike[0].innerText) + 1;
		} else if (resp === "undisliked") {
			dislike.addClass('text-red');
			c_dislike[0].innerText = parseInt(c_dislike[0].innerText) - 1;
		}
	});
}

