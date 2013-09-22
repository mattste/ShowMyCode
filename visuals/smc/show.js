$.get('/structure', function(ajaxData){
	var data =  JSON.parse(ajaxData);

	var width = 960,
	height = 500;

	var svg = d3.select("body").append("svg")
	.attr("width", width)
	.attr("height", height);

	var force = d3.layout.force()
	.nodes(data.nodes)
	.links(data.links)
	.gravity(.01)
	.distance(200)
	.charge(-70)
	.on("tick", tick)
	.size([width, height])
	.start();

	svg.append("svg:defs").selectAll("marker")
	    .data(["suit", "licensing", "resolved"])
	    .enter().append('svg:marker')
	    .attr("id", "resolved")
	    .attr("viewBox", "0 -5 10 10")
	    .attr("refX", 15) 
	    .attr("refY", -1.5)
	    .attr("markerWidth", 6)
	    .attr("markerHeight", 6)
	    .attr("orient", "auto")
	    .append("svg:path")
	    .attr("d", "M0,-5L10,0L0,5");

	var path = svg.append("svg:g").selectAll('path')
	    .data(force.links())
	    .enter().append("svg:path")
	    .attr("class", "link resolved")
	    .attr("marker-end", "url(#resolved)");

	var circle = svg.append("svg:g").selectAll("circle")
		.data(force.nodes())
		.enter().append("svg:circle")
		.attr("r", 6)
		.call(force.drag);

var text = svg.append("svg:g").selectAll("g")
    .data(force.nodes())
  .enter().append("svg:g");

// A copy of the text with a thick white stroke for legibility.
text.append("svg:text")
    .attr("x", 8)
    .attr("y", ".31em")
    .attr("class", "shadow")
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

text.append("svg:text")
    .attr("x", 8)
    .attr("y", ".31em")
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


// Use elliptical arc path segments to doubly-encode directionality.
function tick() {
  path.attr("d", function(d) {
    var dx = d.target.x - d.source.x,
        dy = d.target.y - d.source.y,
        dr = Math.sqrt(dx * dx + dy * dy);
    return "M" + d.source.x + "," + d.source.y + "A" + dr + "," + dr + " 0 0,1 " + d.target.x + "," + d.target.y;
  });

  circle.attr("transform", function(d) {
    return "translate(" + d.x + "," + d.y + ")";
  });

  text.attr("transform", function(d) {
    return "translate(" + d.x + "," + d.y + ")";
  });
}
});
