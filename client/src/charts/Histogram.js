import * as d3 from 'd3';
import {useEffect, useState} from 'react';

const Histogram = (props) => {

	const {width, height } = props;

	let jsonURL = "https://retoolapi.dev/G916NT/data";

	const [data, setData] = useState([]);

  useEffect(()=>{
  	if (data.length > 0) {
  		drawChart();
  	} else {
  		getURLData();
  	}
  },[data])

	const getURLData = async () => {
	    let urlResponse = await fetch(jsonURL);
	    let jsonResult = await urlResponse.json();

	    // build a dictionary to record the frequency of each value in the json response
	    let stateFreq = {};
	    jsonResult.forEach((element) => {
	    	if (stateFreq[element.equity_id] > 0) {
	    		stateFreq[element.equity_id] = stateFreq[element.equity_id] + 1;
	    	} else {
	    		stateFreq[element.equity_id] = 1;
	    	}
	    	})

	    // convert the dictionary to an array
	    let stateFreqArray = Object.keys(stateFreq).map(function(key) {
	    	return {'equity_id': key, 'frequency': stateFreq[key]};
	    })

	    // sort the array by frequency and send it to the data variable
	    setData(stateFreqArray.sort(function(a,b){return b.frequency - a.frequency}));
	}

	const drawChart = () => {

	// declare margins
	const margin = {top: 70, right: 50, bottom: 70, left: 50};

	// create the svg that holds the chart
    const svg = d3.select("#Histogram")
    .append('svg')
		  .style("background-color", "white")
		  .attr("width", width)
		  .attr("height", height)
		  .append('g')
		  .attr("transform",`translate(0,-${margin.bottom-10})`);

	// create the x axis scale, 
	const xScale = d3.scaleBand()
		.domain(data.map(d => d.sale))
		.rangeRound([margin.left, width - margin.right])
		.padding(0.1)

	// create the y axis scale, scaled from 0 to the max
	const yScale = d3.scaleLinear()
		.domain([0, d3.max(data, d => d.frequency)])
		.range([height - margin.bottom, margin.top])

	// create a scale between colors that varies by the frequency
	const barColors = d3.scaleLinear()
	  .domain([0,d3.max(data, d => d.frequency)])
	  .range(["blue","red"])

	  	// set the x axis on the bottom.
	// tilts the axis text so it's readable and not smushed.
    svg.append("g")
      .attr('transform', `translate(0,${height-margin.bottom})`)
      .call(d3.axisBottom(xScale))
      .selectAll("text")
	  .style("text-anchor", "end")
      .attr("dx", "-.8em")
      .attr("dy", ".15em")
      .attr("transform", "rotate(-65)");

    // set the y axis on the left
    svg.append("g")
    .attr('transform', `translate(${margin.left},0)`)
    	.call(d3.axisLeft(yScale));

	  // create the actual bars on the graph, appends a 'rect' for every data element
	  // sets the x and y positions relative to the scales already established
	  // sets the height according to the yscale
	  // static bar width, color is scaled on the y axis
	  // finally the bars have an outline
	  const bars = svg
	  .selectAll("rect")
	  .data(data)
	  .enter().append("rect")
	    .attr('x', d => xScale(d.state))
	    .attr('y', d => yScale(d.frequency))
	    .attr('width', xScale.bandwidth())
	    .attr('height', d => yScale(0) - yScale(d.frequency))
	    .style("padding", "3px")
	    .style("margin", "1px")
	    .style("width", d => `${d * 10}px`)
	    .attr("fill", function(d) {return barColors(d.frequency)})
	    .attr("stroke", "black")
	    .attr("stroke-width", 1)

}

return (
	<div>
	  	<h4> Histogram- http JSON response </h4>
	<div id='Histogram'/>
	</div>
	)
}

export default Histogram;