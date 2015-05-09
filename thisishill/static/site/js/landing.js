"use strict";

$(document).ready(function () {
    var width = $(window).width(),
        height = $(window).height(),
        root;

    var force = d3.layout.force()
                            .size([width, height])
                            .on("tick", tick);

    var svg = d3.select("body").append("svg")
                            .attr("width", width)
                            .attr("height", height);

    var link = svg.selectAll(".link"),
        node = svg.selectAll(".node");

    d3.json("/static/site/data/json/d3r3sum3.json", function(json) {
        root = json;
        collapseAllToStart(); // COMMENT THIS LINE IF YOU WANT TREE TO START IN FULL (NOT COLLAPSED)
        update();
    });

    //new code
    function collapseAllToStart() {
        var collapseMe = flatten(root);
        for(var j = 0; j< collapseMe.length; j++) {
            click(collapseMe[j]);
        }
    }

    var current_node; 

    function update() {
        var nodes = flatten(root),
            links = d3.layout.tree().links(nodes);

        // Restart the force layout.
        force
            .nodes(nodes)
            .links(links)
            .linkDistance(getDistance)
            .start();

        // Update the links.
        link = link.data(links, function(d) { return d.target.id; });

        // Exit any old links.
        link.exit().remove();

        // Enter any new links.
        link.enter().insert("line", ".node")
                            .attr("class", "link")
                            .attr("x1", function(d) { return d.source.x; })
                            .attr("y1", function(d) { return d.source.y; })
                            .attr("x2", function(d) { return d.target.x; })
                            .attr("y2", function(d) { return d.target.y; });

        // Update the nodes.
        node = node.data(nodes, function(d) { return d.id; }).style("fill", color);

        // Exit any old nodes.
        node.exit().remove();

        // Enter any new nodes.
        node.enter().append("circle")
                            .attr("class", "node")
                            .attr("cx", function(d) { return d.x; })
                            .attr("cy", function(d) { return d.y; })
                            .attr("r", function(d) { return Math.sqrt(d.size) / 10 || 4.5; })
                            .style("fill", color)
                            .on("click", click)
                            .call(force.drag);
    }

    function getDistance(node) {
        return node.distance || 100;
    }

    function tick() {
        link.attr("x1", function(d) { return d.source.x; })
                            .attr("y1", function(d) { return d.source.y; })
                            .attr("x2", function(d) { return d.target.x; })
                            .attr("y2", function(d) { return d.target.y; });

        node.attr("cx", function(d) { return d.x; })
                            .attr("cy", function(d) { return d.y; });
    }

    // Color leaf nodes orange, and packages white or blue.
    function color(d) {
        return d.color || (d._children ? "#3182bd" : d.children ? "#c6dbef" : "#fd8d3c");
    }

    function displayNodePanel(d) {
        console.log(d.name);
    }

    // Toggle children on click.
    function click(d) {
        try {
            if (!d3.event.defaultPrevented) {
                displayNodePanel(d);
                if (d.children) {
                    d._children = d.children;
                    d.children = null;
                } else {
                    d.children = d._children;
                    d._children = null;
                }
                current_node = d;
            }
        }
        catch (e) {
            if (e instanceof TypeError) {
                if (d.children) {
                    d._children = d.children;
                    d.children = null;
                } else {
                    d.children = d._children;
                    d._children = null;
                }
            } else {
                console.log(e);
            }
        }
        finally {
            update();
        }
    }

    // Returns a list of all nodes under the root.
    function flatten(root) {
        var nodes = [], i = 0;

        function recurse(node) {
            if (node.children) node.children.forEach(recurse);
            if (!node.id) node.id = ++i;
            nodes.push(node);
        }
        recurse(root);
        current_node = nodes[0];
        return nodes;
    }

});