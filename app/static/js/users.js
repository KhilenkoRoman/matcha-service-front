var auth_id = $("#auth_id")[0].innerText;
var user_id = $("#user_id")[0].innerText;
var friends_button = $("#friends_request button");
var friends_button_sm = $("#friends_request_sm button");

$(document).ready(function () {
	if (auth_id !== "None") {
		$.get("/ajax_check_friends/", {
			'user_id': user_id
		})
		.done(function(response)
		{
			friends_status(response);
		});
	}
	else {
		$("#friends_request").addClass("hidden");
		$("#friends_request_sm").addClass("hidden");
	}
});

function friends_status(response) {
	let friends_button_class = friends_button[0].classList.toString();
	let friends_button_sm_class = friends_button_sm[0].classList.toString();
	var test = friends_button_class.split(" ");
	var test_sm = friends_button_sm_class.split(" ");

	if (response === "waiting") {
		for (let i = 0; i < test.length; i++) {
			friends_button[0].classList.remove(test[i]);
		}
		for (let i = 0; i < test_sm.length; i++) {
			friends_button_sm[0].classList.remove(test_sm[i]);
		}
		friends_button.addClass("btn-my");
		friends_button.addClass("btn-warning");
		friends_button_sm.addClass("btn-my");
		friends_button_sm.addClass("btn-warning");
		friends_button.on('click', delete_user_request);
		friends_button_sm.on('click', delete_user_request);
		friends_button[0].innerText = "Delete request";
		friends_button_sm[0].innerText = "Delete request";
	}
	else if (response === "pending") {
		for (let i = 0; i < test.length; i++) {
			friends_button[0].classList.remove(test[i]);
		}
		for (let i = 0; i < test_sm.length; i++) {
			friends_button_sm[0].classList.remove(test_sm[i]);
		}
		friends_button.addClass("btn-my");
		friends_button.addClass("btn-success");
		friends_button_sm.addClass("btn-my");
		friends_button_sm.addClass("btn-success");
		friends_button.on('click', confirm_user_request);
		friends_button_sm.on('click', confirm_user_request);
		friends_button[0].innerText = "Confirm request";
		friends_button_sm[0].innerText = "Confirm request";
	}
	else if (response === "0") {
		for (let i = 0; i < test.length; i++) {
			friends_button[0].classList.remove(test[i]);
		}
		for (let i = 0; i < test_sm.length; i++) {
			friends_button_sm[0].classList.remove(test_sm[i]);
		}
		friends_button.addClass("btn-my");
		friends_button.addClass("btn-primary");
		friends_button_sm.addClass("btn-my");
		friends_button_sm.addClass("btn-primary");
		friends_button.on('click', add_user_request);
		friends_button_sm.on('click', add_user_request);
		friends_button[0].innerText = "Add friend";
		friends_button_sm[0].innerText = "Add friend";
	}
	else if (response === "1") {
		for (let i = 0; i < test.length; i++) {
			friends_button[0].classList.remove(test[i]);
		}
		for (let i = 0; i < test_sm.length; i++) {
			friends_button_sm[0].classList.remove(test_sm[i]);
		}
		friends_button.addClass("btn-my");
		friends_button.addClass("btn-default");
		friends_button_sm.addClass("btn-my");
		friends_button_sm.addClass("btn-default");
		friends_button.on('click', delete_user_friend);
		friends_button_sm.on('click', delete_user_friend);
		friends_button[0].innerText = "Delete from friends";
		friends_button_sm[0].innerText = "Delete from friends";
	}
	else if (response === "same user") {
		$("#friends_request").addClass("hidden");
		$("#friends_request_sm").addClass("hidden");
	}
}

function delete_user_request() {
	$.get("/ajax_delete_user_request", {
		'user_id': user_id
	})
	.done(function(response)
	{
		let friends_button_class = friends_button[0].classList.toString();
		let friends_button_sm_class = friends_button_sm[0].classList.toString();
		let test = friends_button_class.split(" ");
		let test_sm = friends_button_sm_class.split(" ");

		if (response === "0") {
			for (let i = 0; i < test.length; i++) {
				friends_button[0].classList.remove(test[i]);
			}
			for (let i = 0; i < test_sm.length; i++) {
				friends_button_sm[0].classList.remove(test_sm[i]);
			}
			friends_button.addClass("btn-my");
			friends_button.addClass("btn-primary");
			friends_button_sm.addClass("btn-my");
			friends_button_sm.addClass("btn-primary");
			friends_button.on('click', add_user_request);
			friends_button_sm.on('click', add_user_request);
			friends_button[0].innerText = "Add friend";
			friends_button_sm[0].innerText = "Add friend";
		}
	});
}

function confirm_user_request() {
	$.get("/ajax_confirm_user_request", {
		'user_id': user_id
	})
	.done(function(response)
	{
		let friends_button_class = friends_button[0].classList.toString();
		let friends_button_sm_class = friends_button_sm[0].classList.toString();
		let test = friends_button_class.split(" ");
		let test_sm = friends_button_sm_class.split(" ");

		if (response === "1") {
			for (let i = 0; i < test.length; i++) {
				friends_button[0].classList.remove(test[i]);
			}
			for (let i = 0; i < test_sm.length; i++) {
				friends_button_sm[0].classList.remove(test_sm[i]);
			}
			friends_button.addClass("btn-my");
			friends_button.addClass("btn-default");
			friends_button_sm.addClass("btn-my");
			friends_button_sm.addClass("btn-default");
			friends_button.on('click', delete_user_friend);
			friends_button_sm.on('click', delete_user_friend);
			friends_button[0].innerText = "Delete from friends";
			friends_button_sm[0].innerText = "Delete from friends";
		}
	});
}

function add_user_request() {
	$.get("/ajax_add_user_request", {
		'user_id': user_id
	})
	.done(function(response)
	{
		let friends_button_class = friends_button[0].classList.toString();
		let friends_button_sm_class = friends_button_sm[0].classList.toString();
		let test = friends_button_class.split(" ");
		let test_sm = friends_button_sm_class.split(" ");

		if (response === "waiting") {
			for (let i = 0; i < test.length; i++) {
				friends_button[0].classList.remove(test[i]);
			}
			for (let i = 0; i < test_sm.length; i++) {
				friends_button_sm[0].classList.remove(test_sm[i]);
			}
			friends_button.addClass("btn-my");
			friends_button.addClass("btn-warning");
			friends_button_sm.addClass("btn-my");
			friends_button_sm.addClass("btn-warning");
			friends_button.on('click', delete_user_request);
			friends_button_sm.on('click', delete_user_request);
			friends_button[0].innerText = "Delete request";
			friends_button_sm[0].innerText = "Delete request";
		}
	});
}

function delete_user_friend() {
	$.get("/ajax_delete_user_friend", {
		'user_id': user_id
	})
	.done(function(response)
	{
		let friends_button_class = friends_button[0].classList.toString();
		let friends_button_sm_class = friends_button_sm[0].classList.toString();
		let test = friends_button_class.split(" ");
		let test_sm = friends_button_sm_class.split(" ");

		if (response === "0") {
			for (let i = 0; i < test.length; i++) {
				friends_button[0].classList.remove(test[i]);
			}
			for (let i = 0; i < test_sm.length; i++) {
				friends_button_sm[0].classList.remove(test_sm[i]);
			}
			friends_button.addClass("btn-my");
			friends_button.addClass("btn-primary");
			friends_button_sm.addClass("btn-my");
			friends_button_sm.addClass("btn-primary");
			friends_button.on('click', add_user_request);
			friends_button_sm.on('click', add_user_request);
			friends_button[0].innerText = "Add friend";
			friends_button_sm[0].innerText = "Add friend";
		}
	});
}

function edit_basic(form) {
	$.post("/ajax_edit_basic/", {
		"first_name": form.firstname.value,
		"last_name": form.lastname.value,
		"email": form.email.value,
		"optradio": form.optradio.value,
		"sex": form.sex.value,
		"city": form.city.value,
		"country": form.country.value,
		"information": form.information.value,
		"theme": form.theme.value
	}).done(function (res) {
		if (res === "success") {
			location.reload(true);
		} else {
			let error = $("#error")[0];
			error.innerText = res;
		}
	});
}

function edit_advanced(form) {
	$.post("/ajax_edit_advanced/", {
		"phone": form.phone.value,
		"language": form.language.value,
		"status": form.status.value,
		"political": form.political.value,
		"fb": form.fb.value,
		"tw": form.tw.value,
		"inst": form.inst.value,
		"site": form.site.value,
		"hobbies": form.hobbies.value,
		"tv_shows": form.tv_shows.value,
		"movies": form.movies.value,
		"games": form.games.value,
		"music": form.music.value,
		"books": form.books.value,
		"writers": form.writers.value,
		"others": form.others.value
	}).done(function (res) {
		if (res === "Success") {
			location.reload(true);
		} else {
			let error = $("#error")[0];
			error.innerText = res;
		}
	});
}

function delete_tag(tag) {
	event.preventDefault();
	$.ajax({
		url: "/ajax_remove_tag",
		data: {'id_user': $("#user_id").text(), 'tag_name': tag.innerText.trim()},
		type: 'POST',
		success: function(response)
		{
			console.log(response);
			tag.remove();
		},
		error: function(error)
		{
			console.log(error);
		}
	});
}


$("#add_tag_form").submit(function () {
	event.preventDefault();
	const tag = $("#add-interest").val();
	if (tag.length < 2){return};
	const list = document.getElementById('tags_edit_list');

	$.ajax({
		url: "/ajax_add_tag",
		data: {'id_user': $("#user_id").text(), 'tag_name': tag},
		type: 'POST',
		success: function(response)
		{
			if (response === 'tag_exist'){
				$("#add-interest").val('');
				return;
			}

			if (response !== "error"){
				var node = document.createElement("li");
				node.setAttribute("onclick", "delete_tag(this)");
				node.innerHTML = '<a><i class="'+ response +'"></i> '+ tag + '</a>';
				list.appendChild(node);
				$("#add-interest").val('');
			}
		},
		error: function(error)
		{
			console.log(error);
		}
	});
});


$("#edit_change_password").submit(function () {
	event.preventDefault();

	var old_pwd = $('#my-password');
	var new_pwd = $('#edit_new_pwd');
	var conf_pwd = $('#edit_conf_pwd');

	old_pwd.removeClass("unvalid");
	new_pwd.removeClass("unvalid");
	conf_pwd.removeClass("unvalid");

	if (!old_pwd.val())
		old_pwd.addClass("unvalid");
	if (!new_pwd.val())
		new_pwd.addClass("unvalid");
	if (!conf_pwd.val())
		conf_pwd.addClass("unvalid");

	if (!old_pwd.val() || !new_pwd.val() || !conf_pwd.val()){
		return;}


	$.ajax({
		url: "/ajax_change_pwd",
		data: {'old_pwd': old_pwd.val(), 'new_pwd': new_pwd.val(), 'conf_pwd': conf_pwd.val(), 'id_user': $('#user_id').text()},
		type: 'POST',
		success: function(response)
		{
		   if (response == 'wrong_confirm'){
				conf_pwd.addClass("unvalid");
		   }
		   if (response == 'short_pwd' || response == 'long_pwd' || response == 'week_pwd'){
				new_pwd.addClass("unvalid");
		   }
		   if (response == 'wrong_old_pwd'){
				old_pwd.addClass("unvalid");
		   }
		   if (response == 'sucsess'){
				old_pwd.val('');
				new_pwd.val('');
			   conf_pwd.val('');
			   $("#edit_change_pwd_btn").text('Changed');
			   $("#edit_change_pwd_btn").prop('disabled', true);
		   }
		}
	});
});




