var exec = require('child_process').exec,
	fs   = require('fs'),

	get_haiku = function get_haiku(callback) {
	    exec(
	    	'haiku',
	    	function(error, stdout, stderr) {
	    		callback(stdout);
	    	}
    	);
	},

	toJson = function toJson(haiku) {
		return JSON.stringify({
			"data": {"haiku": haiku}
		}, 4);
	},

	writeFile = function writeFile(path, data) {
		console.log('writing to ' + path);
		fs.writeFile(path, data, function(err) {
			if(err) {
				console.log(err);
			}
		});
	};

get_haiku(function(haiku) {
	console.log(haiku);
	writeFile('/home/jumblesale/twine/haiku.json', toJson(haiku));
});