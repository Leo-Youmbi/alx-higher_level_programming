$(
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: (moviesData) => {
      $.each(moviesData.results, (index, movie) => {
        $('UL#list_movies').append(`<li>${movie.title}</li>`);
      });
    }
  })
);
