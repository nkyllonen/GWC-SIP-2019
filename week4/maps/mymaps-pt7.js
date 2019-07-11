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

function makeCountryRequest() {
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
  // alert("my query: " + query);

  // build and make HTTP GET Request
  // removed "var" s.t. processCountryRequest has access
  countryRequest = new XMLHttpRequest();
  countryRequest.open('GET', query, false);

  // set our callback function
  countryRequest.onload = processCountryRequest;

  countryRequest.send();
}

// pan to a given location
function processCountryRequest() {
  // exit if the request isn't ready
  if (countryRequest.readyState != 4) {
    return;
  }

  // check for invalide states (200 is good)
  if (countryRequest.status != 200) {
    alert("Invalid request. Did not receive code 200.");
    return;
  }

  // parse JSON to get data
  var countryInfo = JSON.parse(countryRequest.responseText);
  console.log(countryInfo);

  var index = 0;

  // for the US there are 2 entries...
  if (countryInfo.length > 1) {
    index = 1;
  }

  // get real lon + lat data
  var latlngInfo = countryInfo[index]["latlng"];
  console.log(latlngInfo);

  lat = latlngInfo[0];
  lon = latlngInfo[1];

  var location = ol.proj.fromLonLat([lon, lat]);

  view.animate({
    center: location, // our "home" location
    duration: 2000       // in milliseconds
  });
}

// run init when the window loads
window.onload = init;
