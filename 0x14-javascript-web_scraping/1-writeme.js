#!/usr/bin/node

const fs = require("fs");
file = process.argv[2];
content = process.argv[3];
fs.writeFile(file, content, (err) => {
	if (err) {
		console.log(err);
	}
});
