//Toggles the class of the <header> element when the
// user clicks on the tag DIVi#toggle_header
$('div#toggle_header').on('click', function() 
      {
        if ($('header').hasClass('red')) {
          $('header').removeClass('red');
          $('header').addClass('green');
        }
        else if ($('header').hasClass('green')) {
          $('header').removeClass('green');
          $('header').addClass('red');
        }
        else {
          $('header').addClass('red');
        }
        
      });
