// from data.js
var tableData = data;
var tbody = d3.select("tbody");

// YOUR CODE HERE!
tableData.forEach(function(ufosighting) {
  console.log(ufosighting);
  var row = tbody.append("tr");
  Object.entries(ufosighting).forEach(function([key, value]) {
    console.log(key, value);
    // Append a cell to the row for each value
    // in the weather report object
    var cell = tbody.append("td");
    cell.text(value);
  });
});

// Select the submit button
var submit = d3.select("#filter-btn");

submit.on("click", function() {

  // Prevent the page from refreshing
  d3.event.preventDefault();

  // Select the input element and get the raw HTML node
  var inputElement = d3.select("#datetime");

  // Get the value property of the input element
  var inputValue = inputElement.property("value");

  console.log(inputValue);
  console.log(tableData);

  var filteredData = tableData.filter(sightings => sightings.datetime === inputValue);

  console.log(filteredData);

  filteredData.forEach(function(filteredufosighting) {
  console.log(filteredufosighting);
  var row = tbody.append("tr");
  Object.entries(filteredufosighting).forEach(function([key, value]) {
    console.log(key, value);
    // Append a cell to the row for each value
    // in the weather report object
    var cell = tbody.append("td");
    cell.text(value);
  });
});
});