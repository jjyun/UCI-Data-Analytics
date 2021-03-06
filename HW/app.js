function buildMetadata(sample) {
  const urlmetadata = "/metadata/<sample>"
  // @TODO: Complete the following function that builds the metadata panel
  // Use `d3.json` to fetch the metadata for a sample
  d3.json(urlmetadata).then(function(data) {
        // Fetch the JSON data and console log it
        console.log(data);
        // Use d3 to select the panel with id of `#sample-metadata`
        var selection = d3.select("#sample-metadata")
        // Use `.html("") to clear any existing metadata
        selection.html("")
        // Use `Object.entries` to add each key and value pair to the panel
        // Hint: Inside the loop, you will need to use d3 to append new
        // tags for each key-value in the metadata.
        Object.entries(data).forEach(([key,value]) => {
          selection.append("h5").text(`${key},${value}`);
        });
}); 
}

function buildCharts(sample) {
  const urldata = "/samples/<sample>"
    // @TODO: Use `d3.json` to fetch the sample data for the plots
    d3.json(urldata).then(function(data) {
      console.log(data)
      .then((data)=> {
        var sample_values = data.sample_values;
        var otu_ids = data.otu_ids;
        var otu_labels = data.otu_labels;
      }
    });
    // @TODO: Build a Bubble Chart using the sample data
    var bubble = [{
      x: otu_ids,
      y: sample_values,
      text: otu_labels,
      mode: "markers",
      marker: {
        size: sample_values,
        color: otu_ids
      }
    }];
    plotly.plot("bubble",bubble);

    // @TODO: Build a Pie Chart
    // HINT: You will need to use slice() to grab the top 10 sample_values,
    // otu_ids, and labels (10 each).
    var pie = [{
      values: sample_values.slice(0,10),
      labels: otu_ids.slice(0,10),
      type: "pie"
    }];
    plotly.plot("pie", pie)

}

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();
