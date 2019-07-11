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

// run init when the window loads
window.onload = init;
