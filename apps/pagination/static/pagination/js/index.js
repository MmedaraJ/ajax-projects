function submitForm(){
    $.ajax({
        method: $('#info_form').attr('method'),
        url: $('#info_form').attr('action'),
        data: $('#info_form').serialize(),
        beforeSend: function(){
            if($('input[name=name]').val() == ""){
                console.log("Empty")
                $('input[name=page_number]').val("1");
                return false;
            }
        },
        success: function(response){
            $('#placeholder').html(response)
        }
    });
    return false;
}

Date.prototype.toDateInputValue = (function() {
    var local = new Date(2021, 01, 20, 10, 33, 30, 0);
    return local.toJSON().slice(0,10);
});

Date.prototype.toDateInputValue1 = (function() {
    var local = new Date(2022, 02, 20, 10, 33, 30, 0);
    return local.toJSON().slice(0,10);
});

$(document).ready(function(){
    console.log($('input[name=page_number]').val())
    $('input[name=name]').keyup(function(){
        submitForm();
    })
    $('input[name=date_from], input[name=date_to]').onSelect(function(){
        submitForm();
    })
    $('#date_to').val(new Date().toDateInputValue1());
    $('#date_from').val(new Date().toDateInputValue());
})