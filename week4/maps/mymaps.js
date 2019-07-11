// variables we need for our map
var map;
var ourLocation;
var view;

// init our variables
function init() {
  ourLocation = ol.proj.fromLonLat([-122.43, 37.63]);

  // create a view object
  view = new ol.View({
    center: ourLocation,
    zoom: 6
  });

  // create a map object
  map = new ol.Map({
    target: 'map', // our target references our map divider
    layers: [
      new ol.layer.Tile({
        source: new ol.source.OSM()
      })
    ],
    loadTilesWhileAnimating: true,
    view: view
  });

}

// pan the map back to our home location
function panHome() {
  view.animate({
    center: ourLocation, // our "home" location
    duration: 2000       // in milliseconds
  });
}

// pan to a given location
function panToLocation() {
  // get value from textarea element
  var countryName = document.getElementById("country-name").value;

  // check that there is something there
  if (countryName === "") {
    alert("You forgot to enter a country!");
    return;
  }

  console.log("country name: " + countryName);

  // build Countries API query
  var query = "https://restcountries.eu/rest/v2/name/" + countryName;
  var lon = 0.0;
  var lat = 0.0;

  // in browsers, spaces are "%20"
  query = query.replace(/ /g, "%20");
  alert("my query: " + query);

  // build and make HTTP GET Request
  var countryRequest = new XMLHttpRequest();
  countryRequest.open('GET', query, false);

  countryRequest.send();

  // output response
  console.log("Ready state: " + countryRequest.readyState);
  console.log("Status: " + countryRequest.status);
  console.log("Response: " + countryRequest.responseText);

  var location = ol.proj.fromLonLat([lon, lat]);

  view.animate({
    center: location, // our "home" location
    duration: 2000       // in milliseconds
  });
}

// run init when the window loads
window.onload = init;
