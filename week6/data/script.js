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
    $.each(result, function(name, object){
      // what to do for each item in dataFile
      var txt = document.createElement("p");  // Create with DOM
      txt.innerHTML = "Results: " + "\n" + name + " " + object;
      $("body").append(txt);   // Append the new elements
      // $("div").append(object + " ");
      // console.log(name + " " + object)
    });
  });
}

// function init() {
  $(document).ready(getData());
// }

// init();
