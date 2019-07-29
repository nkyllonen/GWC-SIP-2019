var dataFile = "data.json";
var zomato_key = "54b0eda3d9055df127947076b27dbd2c";
var resultLoc = [];

// getJSON example: https://www.w3schools.com/jquery/ajax_getjson.asp
// $(document).ready(function(){
//   $("button").click(function(){
//     $.getJSON("data.json", function(result){
//       $.each(result, function(i, field){
//         $("div").append(field + " ");
//       });
//     });
//   });
// });

function getData() {
  $.getJSON(dataFile, function(result){
    console.log(typeof(result));
    $.each(result, function(name, object){
      // console.log(result);
      // what to do for each item in dataFile
      var txt = document.createElement("p");  // Create with DOM
      txt.innerHTML = "Results: " + "\n" + name + " " + object;
      var resultDiv = document.getElementById("result");
      resultDiv.append(txt);
    });
  });
}

function getRestaurant() {
  var n = "denny's";
  dataFile = "charities.json";
  $.getJSON(dataFile, function(result){
    $.each(result, function(name, object){
      if(object["name"].toLowerCase() === n) {
        // console.log(object);
        if(object["accepted"] == true) {
          alert("Shipment received!");
        }
      }
      else {
        console.log("no match");
      }
      // console.log(object["name"]);
    });
  });
}

function edit() {
  // var obj = {
  //   name: "something",
  //   food: ["crackers"],
  //   charities: [],
  //   accepted: false
  // };
  //
  // var blob = new Blob([JSON.stringify(obj)], {type : 'application/json'});
  // window.URL.revokeObjectURL("new.json");
  // var file = window.URL.createObjectURL(blob);

  //check if browser supports file api and filereader features
  if (window.File && window.FileReader && window.FileList && window.Blob) {
    var d = new Date(2013, 12, 5, 16, 23, 45, 600);
    var generatedFile = new File(["Rough Draft ...."], "Draft1.txt", {type: "text/plain"});
  }
  else {
    console.log("File/FileReader/FileList/Blob NOT SUPPORTED");
  }
  // console.log("edit");
}

// using a bunch of code from this StackOverflow page
// https://stackoverflow.com/questions/21012580/is-it-possible-to-write-data-to-file-using-only-javascript

function saveTextAsFile()
{
    var textToWrite = document.getElementById("inputTextToSave").value;
    var textFileAsBlob = new Blob([textToWrite], {type:'text/plain'});
    var fileNameToSaveAs = document.getElementById("inputFileNameToSaveAs").value;
    var downloadLink = document.createElement("a");
    downloadLink.download = fileNameToSaveAs;
    downloadLink.innerHTML = "Download File";

    if (window.webkitURL != null)
    {
        // Chrome allows the link to be clicked
        // without actually adding it to the DOM.
        downloadLink.href = window.webkitURL.createObjectURL(textFileAsBlob);
    }
    else
    {
        // Firefox requires the link to be added to the DOM
        // before it can be clicked.
        downloadLink.href = window.URL.createObjectURL(textFileAsBlob);
        downloadLink.onclick = destroyClickedElement;
        downloadLink.style.display = "none";
        document.body.appendChild(downloadLink);
    }

    downloadLink.click();
}

function getCityID(loc) {
  loc = loc.replace(/ /g, "%20");

  var reqURL = "https://developers.zomato.com/api/v2.1/cities?";
  reqURL = reqURL + "q=" + loc;

  var city_id = 306;

  $.ajax({
        url: reqURL,
        beforeSend: function(xhr) {
             xhr.setRequestHeader("user-key", zomato_key);
        }, success: function(data){
            // console.log(data);
            // get the city ID from the result
            city_id = data["location_suggestions"][0]["id"];
        }
  });

  return city_id;
}

function getSearchData() {
  var location = document.getElementById("zomato-input").value;
  var city_id = getCityID(location);
  var reqURL = "https://developers.zomato.com/api/v2.1/search?";
  reqURL = reqURL + "entity_id=" + city_id + "&entity_type=city";

  $.ajax({
        url: reqURL,
        beforeSend: function(xhr) {
             xhr.setRequestHeader("user-key", zomato_key);
        }, success: function(data){
            // console.log(data);
            // get restaurants array
            var all_rest = data["restaurants"];
            // console.log(all_rest);
            var name = all_rest[0]["restaurant"]["name"];
            var address = all_rest[0]["restaurant"]["location"]["address"];
            console.log(name + " at " + address);
        }
  });
}

function getBoba() {
  var location = document.getElementById("zomato-input").value;
  var city_id = getCityID(location);
  var reqURL = "https://developers.zomato.com/api/v2.1/search?";
  reqURL = reqURL + "entity_id=" + city_id + "&entity_type=city";
  reqURL = reqURL + "q=boba";

  $.ajax({
        url: reqURL,
        beforeSend: function(xhr) {
             xhr.setRequestHeader("user-key", zomato_key);
        }, success: function(data){
            // console.log(data);
            // get restaurants array
            var all_rest = data["restaurants"];
            console.log(all_rest);
            // var name = all_rest[0]["restaurant"]["name"];
            // var address = all_rest[0]["restaurant"]["location"]["address"];
            // console.log(name + " at " + address);
        }
  });
}

// USING OPEN CAGE DATA //

var apikey = 'aa4e018941454030abc16e5af760d2d3';

function getLongLat() {
  // var latitude = '51.0';
  // var longitude = '7.0';

  var api_url = 'https://api.opencagedata.com/geocode/v1/json'

  var placename = document.getElementById("place").value;
  placename = placename.replace(/ /g, "%20");

  var request_url = api_url
    + '?'
    + 'key=' + apikey
    + '&q=' + encodeURIComponent(placename)
    + '&pretty=1'
    + '&no_annotations=1';

  // see full list of required and optional parameters:
  // https://opencagedata.com/api#forward

  request = new XMLHttpRequest();
  request.open('GET', request_url, true);

  request.onload = longLatResult;

  request.onerror = function() {
    // There was a connection error of some sort
    console.log("unable to connect to server");
  };

  request.send();  // make the request
}

function longLatResult() {
    // see full list of possible response codes:
    // https://opencagedata.com/api#codes

    if (request.status == 200){
      // Success!
      var data = JSON.parse(request.responseText);
      // console.log(data);
      resultLoc = data.results[0]["geometry"];
      alert(resultLoc["lat"] + " , " + resultLoc["lng"]);

      sessionStorage.setItem("lat", resultLoc["lat"]);
      sessionStorage.setItem("lng", resultLoc["lng"]);
      // drawMap(lat, lng);

      // redirect with query parameters to pass data
      window.location = "other.html";
        // + "?lat=" + resultLoc["lat"]
        // + "&lng=" + resultLoc["lng"];

    } else if (request.status <= 500){
      // We reached our target server, but it returned an error

      console.log("unable to geocode! Response code: " + request.status);
      var data = JSON.parse(request.responseText);
      console.log(data.status.message);
    } else {
      console.log("server error");
    }
}

// https://www.codeproject.com/Questions/795191/Passing-JavaScript-data-values-between-HTML-pages
function getQParams() {
  var queryString = decodeURIComponent(window.location.search);
  queryString = queryString.substring(1);
  var queries = queryString.split("&");

  for (var i = 0; i < queries.length; i++)
  {
    document.write(queries[i] + "<br>");
  }

  alert(queries[0] + " , " + queries[1]);
}

function other() {
  var output = sessionStorage.getItem("lat")
    + " , " + sessionStorage.getItem("lng");

  alert(output);
}
