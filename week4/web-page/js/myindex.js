/* NOTE: remember to add <script src="myindex.js"></script> to the <head> of HTML doc */

/* create an alert popup BEFORE the DOM is loaded */
alert("Welcome to my page about Aussies!");
console.log("Hello!")

function changeFontSize() {
  /* debugging statement to make sure I was entering
      this function */
  // console.log("within changeFontSize");

  var button = document.getElementById("change-font");
  var cur_size = button.style.fontSize;

  if (cur_size == "14px") {
    button.style.fontSize = "20px";
  }
  else {
    button.style.fontSize = "14px";
  }
}

function changeBodyFontSize() {
  var body = document.body;
  var cur_size = body.style.fontSize;

  if (cur_size == "12px") {
    body.style.fontSize = "20px";
  }
  else {
    body.style.fontSize = "12px";
  }
}
