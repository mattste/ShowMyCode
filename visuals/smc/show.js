$.get('/structure', function(ajaxData){
	var data =  JSON.parse(ajaxData);

	var width = 960,
	height = 500,
	duration = 750;

	var timer = setInterval(update, duration);

	var svg = d3.select("body").append("svg")
	.attr("width", width)
	.attr("height", height);

	var force = d3.layout.force()
	.gravity(.01)
	.distance(200)
	.charge(-10)
	.size([width, height]);

	function update() {
	if (data.length >= 500) return clearInterval(timer);
	}

	d3.json(data, function(error) {
		force
		.nodes(data.nodes)
		.links(data.links)
		.start();

		var link = svg.selectAll(".link")
		.data(data.links)
		.enter().append("line")
		.attr("class", "link");

		var node = svg.selectAll(".node")
		.data(data.nodes)
		.enter().append("g")
		.attr("class", "node")
		.attr("transform", "translate(10, 10)")
		.call(force.drag);

		node.append("image")
		.attr("xlink:href", "https://github.com/favicon.ico")
		.attr("x", 0)
		.attr("y", 0)
		.attr("width", 16)
		.attr("height", 16);

		node.append("text")
		    .attr("dx", 12)
		    .attr("dy", ".35em")
		    .text(function(d) { 
			    var outStr = d.name; 
			    for(var i in d.args)
			    {
			        if( i == 0)
				    outStr += '(';
			        outStr += ' ' + d.args[i];
				if(i == d.args.length - 1)
				    outStr += ')';
				else
				    outStr += ',';
				
			    }
			    return outStr
			    });

		force.on("tick", function() {
			link.attr("x1", function(d) { return d.source.x; })
			.attr("y1", function(d) { return d.source.y; })
			.attr("x2", function(d) { return d.target.x; })
			.attr("y2", function(d) { return d.target.y; });

			node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });
			});
	});
});
