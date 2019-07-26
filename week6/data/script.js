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

function zomato() {
  var loc = document.getElementById("zomato-input").value;
  loc = loc.replace(/ /g, "%20");

  var reqURL = "https://developers.zomato.com/api/v2.1/cities?";
  reqURL = reqURL + "q=" + loc;

  console.log("req: " + reqURL);

  var zomato_key = "54b0eda3d9055df127947076b27dbd2c";

  $.ajax({
        url: reqURL,
        beforeSend: function(xhr) {
             xhr.setRequestHeader("user-key", zomato_key);
        }, success: function(data){
            console.log(data);
            //process the JSON data etc
        }
  });
}
