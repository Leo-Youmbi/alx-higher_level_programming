$(
  $('DIV#toggle_header').click(() => {
    const hasRedClass = $('header').hasClass('red');
    if (hasRedClass) {
      $('header').removeClass('red').addClass('green');
    } else {
      $('header').removeClass('green').addClass('red');
    }
  })
);
