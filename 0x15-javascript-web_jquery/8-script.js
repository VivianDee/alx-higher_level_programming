//Fetches and lists the title for all movies by using this URL
$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function(data, status) {
	data.results.forEach(function(movie) {
		$('ul#list_movies').append('<li>' + movie.title + '</li>');
	});
});
