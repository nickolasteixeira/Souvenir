$(document).ready(function() {
  $('#search-btn').on('click', function(event){
   let city = ($('#search-bar').val());
   let user = ($('#search-bar').attr('user_id')
   event.preventDefault();
   $.ajax({
      type: 'GET',
      url: 'http://127.0.0.1:8000/souvenirapp/api/' + city + '/' + user + '/places',
      dataType: 'json',
      contentType: 'application/json',
      success: function (data) {
        console.log(data);
        let html = '<ul>';
        for (let i = 0; i < data.length; ++i){
           html += '<li>' + data[i].text + '</li>';
        }
        html += '</ul>';
        $('.results').append(html);
      },
      error: function (jqXHR, textStatus, errorThrown) {
        console.log(jqXHR);
        console.log(textStatus);
        console.log(errorThrown);
      }
    });
    });
});
