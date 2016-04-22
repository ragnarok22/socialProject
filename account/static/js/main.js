$(document).ready(function () {

    $('select').material_select();
    $('.button-collapse').sideNav();
    $('.parallax').parallax();
    $('.modal-trigger').leanModal();

    $('#terms').click(function () {
        $('#spinner-terms').show(500);
        $('#terms-content').load('/terms', function (response, status, xhr) {
            if(status == 'error'){
                $('#terms-content').append('<h3><i class="material-icons">error</i> Se ha producido un error ' + xhr.status + '</h3>');
            }
            $('#spinner-terms').hide(500);
        });
    });
    $('#about').click(function () {
        $('#spinner-about').show(500);
        $('#about-content').load('/about', function (response, status, xhr) {
            if(status == 'error'){
                $('#about-content').append('<h3><i class="material-icons">error</i> Se ha producido un error ' + xhr.status + '</h3>');
            }
            $('#spinner-about').hide(500);
        });
    });
    $('#privacy').click(function () {
        $('#spinner-privacy').show(500);
        $('#privacy-content').load('/privacy', function (response, status, xhr) {
            if(status == 'error'){
                $('#privacy-content').append('<h3><i class="material-icons">error</i> Se ha producido un error ' + xhr.status + '</h3>');
            }
            $('#spinner-privacy').hide(500);
        });
    });
});