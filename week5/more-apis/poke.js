function getType() {
  var outputArea = document.getElementById("output");
  var inputArea = document.getElementById("poke-name");

  // outputArea.value = "testing";

  var name = inputArea.value.toLowerCase();

  // check that there is something there
  if (name === "") {
    alert("You forgot to enter a pokemon!");
    return;
  }

  // build query and make request
  var query = "https://pokeapi.co/api/v2/pokemon/" + name;
  query = query.replace(/ /g, "%20");

  var pokeRequest = new XMLHttpRequest();
  pokeRequest.open('GET', query, false);
  pokeRequest.send();

  // exit if the request isn't ready
  if (pokeRequest.readyState != 4) {
    return;
  }

  // check for invalide states (200 is good)
  if (pokeRequest.status != 200) {
    alert("Invalid request. Did not receive code 200.");
    return;
  }

  var pokeInfo = JSON.parse(pokeRequest.responseText);
  console.log(pokeInfo);

  // place type data into output textarea
  var type = pokeInfo["types"][0]["type"]["name"];
  outputArea.value = name + "'s type is: " + type;
}
