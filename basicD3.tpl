<!doctype html>
<html lang = "en">
<style>

.link {
  fill: none;
  stroke: #ccc;
  stroke-width: 1.5px;
/*  stroke-dasharray: 0, 2 1;*/
}

.top-buffer { margin-top:35px; }

.elt {
  text-align: center;
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
    <link href="/visuals/bootstrap/css/bootstrap.min.css" rel="stylesheet" media="screen">
    <link href="/visuals/bootstrap/css/slider.css" rel="stylesheet" media="screen">
    <script type="text/javascript" src="/visuals/bootstrap/js/bootstrap.min.js"></script>
    <script type="text/javascript" src="/visuals/jquery/jquery.js"></script>
    <script type="text/javascript" src="/visuals/smc/show.js"></script>
    <script type="text/javascript" src="/visuals/bootstrap/js/bootstrap-slider.js"></script>
</head>
<body>
<div class="container controller">
    <div class="row-fluid">
      <div id="back" class="elt offset1 span2">
        <button class='btn'>
          <i class="icon-step-backward"></i>
        </button>
      </div>
      <div id="action" class="elt play offset1 span4">
        <button class='btn'> 
          <i class="icon-play" id="playBtn"></i>
          <i class="icon-pause" id="pauseBtn" style="display:none"></i>
        </button>
      </div>
      <div id="fwd" class="elt span2 offset1">
        <button class='btn'> 
          <i class="icon-step-forward"></i>
        </button>
      </div>
    </div>
    <div class="row-fluid elt top-buffer">
      <div id="well" class="elt offset3 span6">
        <input type='text' class="slider slider-horizontal" id="speedSlide" style="width: 140px"/>
        <!--
       <input type="text" class="span2 slider" value="" data-slider-min="-20" data-slider-max="20" data-slider-step="1" data-slider-value="-14" data-slider-orientation="horizontal" data-slider-selection="after"data-slider-tooltip="hide"> 
        Slide
      -->
      </div>
    </div>
</div>
<div class="container">
</div>
</body>
</html>
