//Fetches the character name from this URL
$.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data, status) {
	$('div#character').text(data.name);
});
