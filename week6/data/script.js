var dataFile = "data.json";

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
  console.log("getRestaurant");
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

// do this when the document is ready
// $(document).ready(getData());
