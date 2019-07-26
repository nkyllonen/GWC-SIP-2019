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

// (function () {
// var textFile = null,
//   makeTextFile = function (text) {
//     var data = new Blob([text], {type: 'text/plain'});
//
//     // If we are replacing a previously generated file we need to
//     // manually revoke the object URL to avoid memory leaks.
//     if (textFile !== null) {
//       window.URL.revokeObjectURL(textFile);
//     }
//
//     textFile = window.URL.createObjectURL(data);
//
//     return textFile;
//   };
//
//
//   var create = document.getElementById('create'),
//     textbox = document.getElementById('textbox');
//
//   create.addEventListener('click', function () {
//     var link = document.getElementById('downloadlink');
//     link.href = makeTextFile(textbox.value);
//     link.style.display = 'block';
//   }, false);
// })();


// do this when the document is ready
// $(document).ready(getData());
