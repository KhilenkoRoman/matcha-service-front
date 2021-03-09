function register(view_url)
{
	event.preventDefault();
	var button = event.srcElement;
	var error = 0;
	first_name = $("#firstname").val();
	last_name = $("#lastname").val();
	login = $("#r_login").val();
	email = $("#email").val();
	pasword = $("#password").val();
	var gender;

	if ($('input[id=male]:checked').val() == 'on')
	{gender = 1;}
	else
	{gender = 2;}

	day = $("#day").val()
	month = $("#month").val()
	year = $("#year").val()

	$("#firstname").removeClass("unvalid");
	$("#lastname").removeClass("unvalid");
	$("#r_login").removeClass("unvalid");
	$("#email").removeClass("unvalid");
	$("#password").removeClass("unvalid");
	$("#day").removeClass("unvalid");
	$("#month").removeClass("unvalid");
	$("#year").removeClass("unvalid");

	if (first_name.length < 3 || first_name.length > 20)
	{$("#firstname").addClass("unvalid");
		error = 1;}
	if (last_name.length < 3 || last_name.length > 20)
	{$("#lastname").addClass("unvalid");
		error = 1;}
	if (email.length < 3 || email.length > 30)
	{$("#email").addClass("unvalid");
		error = 1;}
	if (pasword.length < 6 || pasword.length > 40)
	{$("#password").addClass("unvalid");
		error = 1;}
	if (!day)
	{$("#day").addClass("unvalid");
		error = 1;}
	if (!month)
	{$("#month").addClass("unvalid");
		error = 1;}
	if (!year)
	{$("#year").addClass("unvalid");
		error = 1;}

	if (error == 1)
		return("error");

    button.disabled = true;

	$.ajax({
		url: view_url,
		data: {'email': email, 'login': login, 'pasword': pasword, 'first_name': first_name, 'last_name': last_name, 'day': day,
		'month': month, 'year': year, 'gender': gender},
		type: 'POST',
		success: function(response)
		{
			if (response == "wrong_data"){
			$("#day").addClass("unvalid");
			$("#month").addClass("unvalid");
			$("#year").addClass("unvalid");}

			if (response == "email_exist" || response == "no_email" || response == "long_mail" || response == "wrong_email"){
			$("#email").addClass("unvalid");}

			if (response == "login_exist" || response == "no_login" || response == "long_login" || response == "wrong_login"){
			$("#r_login").addClass("unvalid");}

			if (response == "long_pwd" || response == "no_pwd" || response == "week_pwd"){
			$("#password").addClass("unvalid");}

			if (response == "registered"){
				$('#register').fadeOut(600, function(){ $(this).html("<p id='reg_tnx'>Thanks for registration");});
				$('#register').fadeIn(600, function(){});
				$('#login_tab_btn').removeAttr('href');
				$('#register_tab_btn').removeAttr('href');
				location.reload();
			}

			button.disabled = false;
		},
		error: function(error)
		{
			console.log(error);
		}
	});
}

function login(view_url)
{
	event.preventDefault();
	var error = 0;
	var login = $("#my-email").val();
	var pwd = $("#my-password").val();

	$("#my-email").removeClass("unvalid");
	$("#my-password").removeClass("unvalid");

	if (login.length < 3 || login.length > 30)
	{$("#my-email").addClass("unvalid");
		error = 1;}
	if (pwd.length < 6 || pwd.length > 40)
	{$("#my-password").addClass("unvalid");
		error = 1;}

	if (error == 1)
		return("error");

	$.ajax({
		url: view_url,
		data: {'login': login, 'pwd': pwd},
		type: 'POST',
		success: function(response)
		{
			if (response == "no_login" || response == "long_login" || response == "not_active" || response == "no_user"){
			$("#my-email").addClass("unvalid");}
			if (response == "no_pwd" || response == "long_pwd" || response == "wrong_pwd"){
			$("#my-password").addClass("unvalid");}
			if (response == "logged_in"){
			location.replace("/");}
		},
		error: function(error)
		{
			console.log(error);
		}
	});
}

function recover(view_url)
{
	event.preventDefault();
	var button = event.srcElement;
	const login = $("#forg_my_email").val();
	$("#forg_my_email").removeClass("unvalid");

	if (login.length < 3 || login.length > 30){
	$("#forg_my_email").addClass("unvalid");
	return ("error");}

    button.disabled = true;

	$.ajax({
		url: view_url,
		data: {'login': login},
		type: 'POST',
		success: function(response)
		{
			if (response == "no_user" || response == "not_active"){
			$("#forg_my_email").addClass("unvalid");}

			if (response != "msg_sent"){
			event.srcElement.disabled = false;}

			if (response == "msg_sent"){
				$('#forgot_pwd').fadeOut(600, function(){ $(this).html("<p id='reg_tnx'>Mesaage sent<br>Look your email for instructions</p>");});
				$('#forgot_pwd').fadeIn(600, function(){});
				$('#login_tab_btn').removeAttr('href');
				$('#register_tab_btn').removeAttr('href');
			}

			button.disabled = false;
		},
		error: function(error)
		{
			console.log(error);
		}
	});
}

function new_pwd(view_url, token, email)
{
	event.preventDefault();
	const password = document.getElementById("rec_pwd_inp").value;
	$("#rec_pwd_inp").removeClass("unvalid");

	if (password.length < 6 || password.length > 40)
	{
	$("#rec_pwd_inp").addClass("unvalid");
	return;
	}

	$.ajax({
		url: view_url,
		data: {'pwd': password, 'token': token, 'email': email},
		type: 'POST',
		success: function(response)
		{
			if (response != "changed")
			{
			    $("#rec_pwd_inp").addClass("unvalid");
			    return;
			}
			else
			{
				$('#recover_form').fadeOut(600, function(){ $(this).html("<p id='reg_tnx'>Password changed</p>");});
				$('#recover_form').fadeIn(600, function(){});
			}

		},
		error: function(error)
		{
			console.log(error);
		}
	});
}

$("#forg_pwd_btn").click(function(){
	event.preventDefault();
	$("#login").toggleClass("active");
	$("#forgot_pwd").toggleClass("active");
});

$("#rem_pwd_btn").click(function(){
	event.preventDefault();
	$("#login").toggleClass("active");
	$("#forgot_pwd").toggleClass("active");
});

$("#register_btm").click();