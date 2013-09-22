<!doctype html>
<html lang = "en">
<style>

.header {
  margin: 20px 50px 20px 50px;
  text-align: center;
}

.playback-controls {
  margin-top: 20px;
}

.slider-controls {
  margin-top: 5px;
}

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
  font: 18px sans-serif;
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

circle.bubble {
    fill: #d1006c;
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
    <div class="span12 row-fluid">
      <div class="span4">
        <H1>Show My Code</H1>
      </div>
      <div class="playback-controls offset1 span7">
      <div id="back" class="elt span1">
        <button class='btn'>
          <i class="icon-step-backward"></i>
        </button>
      </div>
      <div id="action" class="elt play span1">
        <button class='btn'> 
          <i class="icon-play" id="playBtn"></i>
          <i class="icon-pause" id="pauseBtn" style="display:none"></i>
        </button>
      </div>
      <div id="fwd" class="elt span1">
        <button class='btn'> 
          <i class="icon-step-forward"></i>
        </button>
      </div>
      <div class="slider-controls span3">
      <input type='text' class="slider slider-horizontal" id="speedSlide" style="width: 140px"/>
      </div>
      </div>
    </div>
<!--     <div class="row-fluid elt top-buffer">
      <div id="well" class="elt offset3 span6">
        <div class="slider slider-horizontal" style="width: 140px">
        </div> -->
        
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
