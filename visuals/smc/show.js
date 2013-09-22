var queue = [];
var progStack = [];
var qIndex = 0;
var intervalId;


$.get('/structure', function(ajaxData){

    function incrementQIndex()
    {
    	var newIndex = (qIndex + 1)% queue.length;
		var checkName =queue[qIndex].name;
		while(checkName === queue[newIndex].name)
		{
			console.log(newIndex);
			newIndex = (newIndex + 1)% queue.length;
		}
		qIndex = newIndex;
		updateGraph();
    }

    function decrementQIndex()
    {
		var newIndex = (qIndex + queue.length - 1)% queue.length;
		var checkName =queue[qIndex].name;
		while(checkName=== queue[newIndex].name)
		{
			console.log(newIndex);
			newIndex = (newIndex + queue.length - 1)% queue.length;
		}
		qIndex = newIndex;
		updateGraph();
    }
    function playProg()
    {
    	intervalId = setInterval(incrementQIndex, ((11-$('#speedSlide').slider('getValue').val())*100));
    }
    function pauseProg()
    {
    	clearInterval(intervalId);
    }

	$(document).ready(function(){

		$('.slider').slider();
		$('#back').click(function(e){
			decrementQIndex();
		});
		$('#fwd').click(function(e){
			incrementQIndex();
		});
		$('#speedSlide').on('slide', function(e)
		{
			//Playing
			if($('#pauseBtn').css('display') !== 'none')
			{
				clearInterval(intervalId);
				playProg();
			}
		});
		$('#action').click(function(e){
			$('#playBtn').toggle();
			$('#pauseBtn').toggle();
			//Paused
			if($('#pauseBtn').css('display') === 'none')
			{
				pauseProg();
			}
			//Playing
			else
			{
				playProg();
			}
		});

	});
	var data =  JSON.parse(ajaxData);
	console.log(data);

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
	    .attr("markerWidth", 12)
	    .attr("markerHeight", 12)
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
		.attr("r", 12)
		.attr("id", function(d){ return d.name;})
		.attr("class", function(d){
			return d.name === 'main' ? "running" : "";
		})
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

var i = 0;
// Use elliptical arc path segments to doubly-encode directionality.
function tick() {
  path.attr("d", function(d) {

  	// prevent nodes from traveling out of bounds
  	// check target nodes
  	if (d.target.y > height) { d.target.y = height - 20; }
  	else if (d.target.y < 0) { d.target.y = 20; }
  	if (d.target.x > width) { d.target.x = width - 20; }
  	else if( d.target.x < 30 ){ d.target.x = 20; }
  	
  	// check source nodes
  	if (d.source.y > height) { d.source.y = height - 20; }
  	else if (d.source.y < 0) { d.source.y = 20; }
  	if (d.source.x < 0) { d.source.x = 20; }
    
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

function passArgBubble()
{
	var curPath = getCurrentPath();
	if (!curPath)
		return;

	var bubble = 
	svg.insert("svg:circle", ":first-child")
	.attr("class", "bubble")
    .attr("r", 10)
    .attr("x", curPath.datum().source.x)
    .attr("y", curPath.datum().source.y);

    transition(bubble, curPath);
}

function getCurrentPath()
{
	var curObj = queue[qIndex];
	var prevObj = queue[qIndex-1];

	console.log("desired source: " + prevObj.name);
	console.log("desired target: " + curObj.name);	

	var rets = path.filter(function(d, i) {
		console.log("iter source: " + d.source.name);
		console.log("iter target: " + d.target.name);
		return (d.source.name == prevObj.name &&
				d.target.name == curObj.name);
	});

	console.log("found path: " + rets.node());

	return rets;
}

function transition(bubble, curPath)
{
	console.log("path: " + curPath);
	bubble.transition()
	.duration(2000)
	.attrTween("transform", translateAlong(curPath.node()))
	.each("end", function(){
		bubble.remove();
	});
}

// Returns an attrTween for translating along the specified path element.
function translateAlong(thePath) 
{
  var l = thePath.getTotalLength();
  return function(d, i, a) {
    return function(t) {
      var p = thePath.getPointAtLength(t * l);
      return "translate(" + p.x + "," + p.y + ")";
    };
  };
}

function updateQueue()
{
	//Continuously update the graph
	$.get('/realtime', function(ajaxData){
		//console.log(JSON.parse(ajaxData));
		queue = queue.concat(JSON.parse(ajaxData));
		setTimeout(updateQueue, 3000);
	});
}


function updateGraph()
{
	if(queue.length <= 0)
		return;
	if(qIndex >= queue.length || qIndex < 0)
		qIndex = 0;
	logObj = queue[qIndex];
	var curName = logObj.name;

	d3.selectAll('circle').
	attr("class", function(d){
		return (d && d.name === curName) ? "running" : "";
	});
	passArgBubble();
}
updateQueue();
});

