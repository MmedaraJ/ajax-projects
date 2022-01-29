$(document).ready(function(){
    console.log($('input[name=page_number]').val())
    $('a').click(function() {
        $('input[name=page_number]').val($(this).attr('data-value'));
        submitForm();
        return false;
    })
})