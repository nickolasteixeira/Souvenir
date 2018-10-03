
$(document).ready(function() {
    console.log("First run");
    let places = {};
    $(document).on('click', 'button', function() {
        if ($(this).hasClass('a')) {
            places[$(this).parent().attr('rev_id')] = [$(this).parent().attr('place_id'),
                $(this).parent().attr('user_id')
            ]
            console.log(places);
            $(this).toggleClass('a d');
	        $(this).toggleClass("btn-primary btn-danger");
            $(this).text('delete');
        } else if ($(this).hasClass('d')) {
            delete places[$(this).parent().attr('rev_id')];
            console.log(places);
            $(this).toggleClass('d a');
	        $(this).toggleClass("btn-primary btn-danger");
            $(this).text('add');
        }

    });
    $('.cr').on('click', function() {
        let u_id = $(this).attr('user_id');
        $('body').load('http://127.0.0.1:8000/souvenirapp/results/' + u_id, places);
    });

    $('#search-btn').on('click', function(event) {
        let city = ($('#search-bar').val());
        let user = $('#search-bar').attr('user_id');
        event.preventDefault();
        $.ajax({
            type: 'GET',
            url: 'http://127.0.0.1:8000/souvenirapp/api/' + city + '/' + user + '/places',
            dataType: 'json',
            contentType: 'application/json',
            success: function(data) {
                console.log(data);
                let html = '<ul>';
                for (let i of data) {
                    html += '<li class="listing ' + i[1].category + '">';
                    html += '<article>';
                    html += '<img src="'+i[1].photourl+'" class="img-thumbnail">';
                    html += '<div class="p-3 mb-2 bg- ">';
                    html += '<div class="information" rev_id=' + i[0].id + ' user_id=' + i[2].id + ' place_id=' + i[1].id + '>';
                    html += '<p>' + i[1].name + ' - ' + i[1].description + '</p>';
                    html += '<button type="button" class="a btn btn-primary float-right" data-toggle="button" aria-pressed="false" autocomplete="off">' + "ADD" + '</button>';
                    html += '<p>' + "Review: " + i[0].text + '</p>';
                    html += '<p>' + "Recommended by " + i[2].first_name + '</p>';
                    html += '<p>' + 'Category - ' + i[1].category + '</p>';
                    for (let j = 0; j < i[0].rating; ++j) {
                        html += '<i class="fas fa-star"></i>';
                    }
                    html += '</div>';
                    html += '</div>';
                    html += '</article>';
                    html += '</li>';
                }
                html += '</ul>';
                $('.results').html(html);
            },
            error: function(jqXHR, textStatus, errorThrown) {
                html = '<h1>No data found</h1>';
                $('.results').html(html);
                console.log(jqXHR);
                console.log(textStatus);
                console.log(errorThrown);
            }
        });
    });
    
    $('#eat-container').on('click', function(event) {
        $('.Eat:hidden').show('fast');
        $('.Stay').css('display', 'none');
        $('.Play').css('display', 'none');
    });

    $('#stay-container').on('click', function(event) {
        $('.Stay:hidden').show('fast');
        $('.Eat').css('display', 'none');
        $('.Play').css('display', 'none');
    });

    $('#play-container').on('click', function(event) {
        $('.Play:hidden').show('fast');
        $('.Eat').css('display', 'none');
        $('.Stay').css('display', 'none');
    });

});
