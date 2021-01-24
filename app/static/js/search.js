/**
 * Created by Roma on 10.06.2018.
 */

var age_from = $("#age_from");
var age_to = $("#age_to");
var fame_from = $("#fame_from");
var fame_to = $("#fame_to");
var gender = $('#gender_select');
var country = $("#country");
var city = $("#city");
var tag_1 = $("#tag_1");
var tag_2 = $("#tag_2");
var tag_3 = $("#tag_3");


function re_sort(data) {
    let user_list = JSON.parse(data);
    let search_result = $('#search_result');

    search_result.html("");
    $.each(user_list, function(i, item) {
        $('<div class="col-md-4 col-sm-4">' +
            '<div class="friend-card">' +
            '<img src="' + item.cover + '" alt="profile-cover" class="img-responsive cover">' +
            '<div class="no_pading card-info text-center">' +
            '<img src="' + item.avatar + '" alt="user" class="profile-photo-lg">' +
            '<div class="friend-info user_div_info">' +
            '<h5><a href="/user/id'+ item.id_user +'/" class="profile-link">' +
            item.first_name + ' '+ item.last_name +'</a></h5>' +
            '<span class="user_span_info"><strong>Rating</strong>:  ' + item.rating + '  </span>' +
            '<span class="user_span_info"><strong>Age</strong>:  ' + item.age + '  </span>' +
            '<span class="user_span_info"><strong>Distance</strong>:  ' + item.distance + ' km </span>' +
            '</div></div></div></div>').appendTo(search_result);
    })
}


$("#apply_filter_btn").click(function () {
    event.preventDefault();
    var sort = 'none';
    var sort_list = $(".active_arrow")[0];
    if (sort_list){
    	sort = sort_list.id;}
    $.ajax({
		url: '/ajax_filter_apply',
		data: {'age_from': age_from.val(), 'age_to': age_to.val(), 'fame_from': fame_from.val(), 'fame_to': fame_to.val(),
            'country': country.val(), 'city': city.val(), 'tag_1': tag_1.val(), 'tag_2': tag_2.val(), 'tag_3': tag_3.val(),
            'sort': sort, 'gender': gender.val()},
		type: 'POST',
		success: function(response)
		{
            re_sort(response);
		}
	});
});

$("#age_desc").click(function () {
    $.ajax({
		url: '/ajax_filter_apply',
		data: {'age_from': age_from.val(), 'age_to': age_to.val(), 'fame_from': fame_from.val(), 'fame_to': fame_to.val(),
            'country': country.val(), 'city': city.val(), 'tag_1': tag_1.val(), 'tag_2': tag_2.val(), 'tag_3': tag_3.val(),
            'sort': 'age_desc', 'gender': gender.val()},
		type: 'POST',
		success: function(response)
		{
            $(".fas").removeClass("active_arrow");
            $("#age_desc").addClass("active_arrow");
            re_sort(response);
		}
	});
});

$("#age_asc").click(function () {
   $.ajax({
		url: '/ajax_filter_apply',
		data: {'age_from': age_from.val(), 'age_to': age_to.val(), 'fame_from': fame_from.val(), 'fame_to': fame_to.val(),
            'country': country.val(), 'city': city.val(), 'tag_1': tag_1.val(), 'tag_2': tag_2.val(), 'tag_3': tag_3.val(),
            'sort': 'age_asc', 'gender': gender.val()},
		type: 'POST',
		success: function(response)
		{
            $(".fas").removeClass("active_arrow");
            $("#age_asc").addClass("active_arrow");
            re_sort(response);
		}
	});
});

$("#dist_desc").click(function () {
    $.ajax({
		url: '/ajax_filter_apply',
		data: {'age_from': age_from.val(), 'age_to': age_to.val(), 'fame_from': fame_from.val(), 'fame_to': fame_to.val(),
            'country': country.val(), 'city': city.val(), 'tag_1': tag_1.val(), 'tag_2': tag_2.val(), 'tag_3': tag_3.val(),
            'sort': 'dist_desc', 'gender': gender.val()},
		type: 'POST',
		success: function(response)
		{
            $(".fas").removeClass("active_arrow");
            $("#dist_desc").addClass("active_arrow");
            re_sort(response);
		}
	});
});

$("#dist_asc").click(function () {
    $.ajax({
		url: '/ajax_filter_apply',
		data: {'age_from': age_from.val(), 'age_to': age_to.val(), 'fame_from': fame_from.val(), 'fame_to': fame_to.val(),
            'country': country.val(), 'city': city.val(), 'tag_1': tag_1.val(), 'tag_2': tag_2.val(), 'tag_3': tag_3.val(),
            'sort': 'dist_asc', 'gender': gender.val()},
		type: 'POST',
		success: function(response)
		{
            $(".fas").removeClass("active_arrow");
            $("#dist_asc").addClass("active_arrow");
            re_sort(response);
		}
	});
});

$("#rate_desc").click(function () {
    $.ajax({
		url: '/ajax_filter_apply',
		data: {'age_from': age_from.val(), 'age_to': age_to.val(), 'fame_from': fame_from.val(), 'fame_to': fame_to.val(),
            'country': country.val(), 'city': city.val(), 'tag_1': tag_1.val(), 'tag_2': tag_2.val(), 'tag_3': tag_3.val(),
            'sort': 'rate_desc', 'gender': gender.val()},
		type: 'POST',
		success: function(response)
		{
            $(".fas").removeClass("active_arrow");
            $("#rate_desc").addClass("active_arrow");
            re_sort(response);
		}
	});
});

$("#rate_asc").click(function () {
    $.ajax({
		url: '/ajax_filter_apply',
		data: {'age_from': age_from.val(), 'age_to': age_to.val(), 'fame_from': fame_from.val(), 'fame_to': fame_to.val(),
            'country': country.val(), 'city': city.val(), 'tag_1': tag_1.val(), 'tag_2': tag_2.val(), 'tag_3': tag_3.val(),
            'sort': 'rate_asc', 'gender': gender.val()},
		type: 'POST',
		success: function(response)
		{
            $(".fas").removeClass("active_arrow");
            $("#rate_asc").addClass("active_arrow");
            re_sort(response);
		}
	});
});