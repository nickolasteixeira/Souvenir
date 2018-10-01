$(document).ready(function() {
    console.log("First run");
    let places = {};
    $('button').on('click', function(){
	if($(this).hasClass('a')){
	    places[$(this).parent().attr('REV_id')] =
		[$(this).parent().attr('place_id'),
		 $(this).parent().attr('user_id')]
	    console.log(places);
	    $(this).toggleClass('a d');
	    $(this).text('delete');
	}
	else if($(this).hasClass('d')){
	    delete places[$(this).parent().attr('REV_id')];
	    console.log(places);
	    $(this).toggleClass('d a');
	    $(this).text('add');
	}
	
    });
    $('#cr').on('click', function(){
	let u_id=$(this).attr('user_id');
	$('body').load('http://127.0.0.1:8000/souvenirapp/results/'+u_id,places);
    });
});