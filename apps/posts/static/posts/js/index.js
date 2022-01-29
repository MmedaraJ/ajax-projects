$(document).ready(function(){
    $('#post_form').submit(function() {
        $.ajax({
           method: $(this).attr('method'),
           url: $(this).attr('action'),
           data: $('#post_form').serialize()
        })
        .done(function( response ) {
           console.log('received response:', response);
           $('#placeholder').html(response);
           $('#post').val('')
        });
        return false;
    });
})