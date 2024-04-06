let url = "https://hellosalut.stefanbohacek.dev/?lang=fr"
$(() => {
	$.get(url)
		.done((data) => {
			$("#hello").text(data.hello);
		});
});
