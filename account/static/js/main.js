$(document).ready(function () {
    $('#terms').click(function () {
        $('#spinner-terms').show(500);
        $('#terms-content').load('terms', function (response, status, xhr) {
            if(status == 'error'){
                $('#terms-content').append('<p><i class="fa fa-times-circle-o"> Se ha producido un error ' + xhr.status + '</p></i>');
            }
            $('#spinner-terms').hide(500);
        });
    });
    $('#about').click(function () {
        $('#spinner-about').show(500);
        $('#about-content').load('about', function (response, status, xhr) {
            if(status == 'error'){
                $('#about-content').append('<p><i class="fa fa-times-circle-o"> Se ha producido un error ' + xhr.status + '</p></i>');
            }
            $('#spinner-about').hide(500);
        });
    });
    $('#privacy').click(function () {
        $('#spinner-privacy').show(500);
        $('#privacy-content').load('privacy', function (response, status, xhr) {
            if(status == 'error'){
                $('#privacy-content').append('<p><i class="fa fa-times-circle-o"> Se ha producido un error ' + xhr.status + '</p></i>');
            }
            $('#spinner-privacy').hide(500);
        });
    });
});