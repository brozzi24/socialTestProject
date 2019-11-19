setTimeout(function(){
    jQuery('#message').fadeOut('slow');
}, 3000);

// For logout on navbar
$('#trigger').click(function(){ 
    formSubmit(); 
    return false; 
});

function formSubmit(){
    document.getElementById("logout").submit();
}

