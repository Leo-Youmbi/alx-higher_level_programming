$(document).ready(() => {
  $('DIV#add_item').click(() => {
    const newElement = '<li>Item</li>';
    $('ul.my_list').append(newElement);
  });
  $('DIV#remove_item').click(() => {
    $('UL.my_list li:last').remove();
  });
  $('DIV#clear_list').click(() => {
    $('UL.my_list').empty();
  });
});
