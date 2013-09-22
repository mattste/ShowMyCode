<!doctype html>
<html lang = "en">
<style>

.link {
  fill: none;
  stroke: #ccc;
  stroke-width: 1.5px;
/*  stroke-dasharray: 0, 2 1;*/
}

.node text {
  pointer-events: none;
  font: 10px sans-serif;
}
path.link {
    fill: none;
    stroke: #666;
    stroke-width: 1.5px;
}

marker#licensing {
   fill: green;
}

path.link.running {
   stroke: green;
}

path.link.resolved {
   stroke-dasharray: 0,2 1;
}

circle {
    fill: #ccc;
    stroke: #333;
    stroke-width: 1.5px;
}

circle.running {
  fill: green;
}


text {
    font: 10px sans-serif;
    pointer-events: none;
}

text.shadow {
    stroke: #fff;
    stroke-width: 3px;
    stroke-opacity: .8;
}
</style>
<head>
    <meta charset = "utf-8"/>
    <title>D3 Test</title>
    <script type="text/javascript" src="http://mbostock.github.com/d3/d3.js?1.29.1"></script>
   <!-- 
    <script type="text/javascript" src="/visuals/d3/d3.js"></script>
  -->
    <script type="text/javascript" src="/visuals/jquery/jquery.js"></script>
    <script type="text/javascript" src="/visuals/smc/show.js"></script>
</head>
<body>
<div class="container">
</div>
</body>
</html>
