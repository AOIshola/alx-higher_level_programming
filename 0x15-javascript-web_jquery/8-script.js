let url = "https://swapi-api.alx-tools.com/api/films/?format=json";
$(() => {
	$.get(url)
		.done((data) => {
			data.results.forEach(elem => {
				$("#list_movies").append(`<li>${elem.title}</li>`)
			});
		});
});
