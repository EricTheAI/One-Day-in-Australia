/**
 * Created by XX on 2017/5/7.
 */

var width = 400,
    height = 400,
    radius = Math.min(width, height) / 2,
    innerRadius = 0.3 * radius;

var pie = d3.layout.pie()
    .sort(null)
    .value(function(d) { return d.width; });

var tip = d3.tip()
    .attr('class', 'd3-tip')
    .offset([0, 0])
    .html(function(d) {
        return d.data.label + ": <span style='color:orangered'>" + d.data.score + "</span>";
    });

var arc = d3.svg.arc()
    .innerRadius(innerRadius)
    .outerRadius(function (d) {
        return (radius - innerRadius) * (d.data.score / 20.0) + innerRadius;
    });

var outlineArc = d3.svg.arc()
    .innerRadius(innerRadius)
    .outerRadius(radius);

var svg = d3.select("#chart").append("svg")
    .attr("width", width)
    .attr("height", height)
    .append("g")
    .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

svg.call(tip);
function updatePie(){
    d3.json('/comment/like', function(error, json) {
        if(error){
            return;
        }
        svg.selectAll("*").remove();
        // console.log(json);
        var data = [];
        var colors = ["#9E0041", "#E1514B", "#FEC574", "#FAE38C", "#6CC4A4", "#4776B4"];
        for(var i = 0; i < json.length; i++){
            var slice = {};
            slice.order  = i;
            slice.color  = colors[i];
            slice.weight = 1;
            slice.score  = json[i].count;
            slice.width  = 1;
            slice.label  =  json[i].emotion;
            data.push(slice);
        }

        // for (var i = 0; i < data.score; i++) { console.log(data[i].id) }

        var path = svg.selectAll(".solidArc")
            .data(pie(data))
            .enter().append("path")
            .attr("fill", function(d) { return d.data.color; })
            .attr("class", "solidArc")
            .attr("stroke", "gray")
            .attr("d", arc)
            .on('mouseover', tip.show)
            .on('mouseout', tip.hide);

        var outerPath = svg.selectAll(".outlineArc")
            .data(pie(data))
            .enter().append("path")
            .attr("fill", "none")
            .attr("stroke", "gray")
            .attr("class", "outlineArc")
            .attr("d", outlineArc);


        // calculate the weighted mean score
        var score =
            data.reduce(function(a, b) {
                //console.log('a:' + a + ', b.score: ' + b.score + ', b.weight: ' + b.weight);
                return a + (b.score * b.weight);
            }, 0);

        svg.append("svg:text")
            .attr("class", "aster-score")
            .attr("dy", ".35em")
            .attr("text-anchor", "middle") // text-align: right
            .text(Math.round(score));
    });
}
updatePie();
setInterval(function() {
    updatePie();
}, 2000); //5 seconds
