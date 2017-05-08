/**
 * Created by Evan on 2017/5/6.
 */
var graph = new Springy.Graph();

jQuery(function(){
    var springy = window.springy = jQuery('#ncanvas').springy({
        graph: graph,
        nodeSelected: function(node){
            console.log('Node selected: ' + JSON.stringify(node.data));
            $("#nodetext").html("Message:" + node.data.label);
            if(node.data.from !== undefined)
                $("#nodefromtext").html("From:" + node.data.from);
            else
                $("#nodefromtext").html("");
        }
    });
});

function calcColor(colors) {
    var colorMixedR = colors[0];
    var colorMixedG = colors[1];
    var colorMixedB = colors[2];
    return "rgb(" + parseInt(colorMixedR) + "," + parseInt(colorMixedG) + "," + parseInt(colorMixedB) + ")";
}

var nodesGlobal = {};


function getLive() {
    $.get( "comment/live", function( data ) {
        if(data === undefined){
            alert("Error");
            return;
        }
        for (var property in nodesGlobal) {
            if (nodesGlobal.hasOwnProperty(property)) {
                graph.removeNode(nodesGlobal[property]);
            }
        }
        nodesGlobal = {};
        // console.log(data);
        var json = JSON.parse(data);
        // console.log(json);
        var nodes = json.nodes;
        var relationships = json.relationship;
        // console.log(json);
        // var colorsArray = [["55", "155","166"],["71", "147","156"],["87", "139","146"],["103", "131","136"],["119", "123","126"],
            // ["135", "107","116"],["151", "107","106"],["167", "99","96"],["183", "91","86"],["199", "83","76"]];
        var colorsArray = [["71", "217","191"],["69", "178","157"],["239", "201","76"],["226", "122","63"],["213", "86","70"],
            ["0", "161","217"],["116", "165","136"],["214", "204","173"],["220", "156","118"],["214", "101","90"]];
        for (var i = 0; i < nodes.length; i++) {
            if(nodes[i] === null){
                continue;
            }
            console.log(nodes[i]);
            var node_color = calcColor(colorsArray[i%10]);
            var node = graph.newNode({
                label: nodes[i].name,
                id: nodes[i].id,
                size: nodes[i].size,
                color: node_color,
                from: nodes[i].from});
            // console.log(nodes[i]);

            nodesGlobal[nodes[i].id] = node;
        }
        for (var j = 0; j < relationships.length; j++) {
            var rel =  relationships[j];
            // console.log(rel);
            graph.newEdge(nodesGlobal[rel.id_1], nodesGlobal[rel.id_2], {color: '#EB6841'});
        }
    });
}
getLive();
setInterval(function() {
    getLive();
}, 5000); //5 seconds


