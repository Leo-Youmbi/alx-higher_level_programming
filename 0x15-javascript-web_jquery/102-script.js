$(document).ready(() => {
  $('INPUT#btn_translate').click(() => {
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/?',
      type: 'GET',
      data: {
        lang: $('INPUT#language_code').val()
      },
      success: (data) => {
        $('DIV#hello').html(data.hello);
      },
      error: () => {
        $('#hello').html('Translation not found!');
      }
    });
  });
});
