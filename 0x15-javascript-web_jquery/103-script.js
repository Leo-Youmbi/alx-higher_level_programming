$(document).ready(() => {
  $('INPUT#btn_translate').click(fetchTranslation);
  $('INPUT#language_code').keypress(function (event) {
    if (event.which === 13) { // Enter key
      fetchTranslation();
    }
  });

  function fetchTranslation () {
    const languageCode = $('INPUT#language_code').val();
    const apiUrl = 'https://www.fourtonfish.com/hellosalut/?' + `lang=${languageCode}`;
    alert(apiUrl)

    $.ajax({
      url: apiUrl,
      method: 'GET',
      success: function (response) {
        $('#hello').html(response.hello);
      },
      error: function () {
        $('#hello').html('Translation not found!');
      }
    });
  }
});
