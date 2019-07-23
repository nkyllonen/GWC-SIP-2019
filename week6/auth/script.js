// initialize
// gapi.load('auth2', function () {
//   gapi.auth2.init();
// });
//
// function onSignIn(googleUser) {
//   var profile = googleUser.getBasicProfile();
//   console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
//   console.log('Name: ' + profile.getName());
//   console.log('Image URL: ' + profile.getImageUrl());
//   console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
// }
//
// function signOut() {
//   var auth2 = gapi.auth2.getAuthInstance();
//   auth2.signOut().then(function () {
//     console.log('User signed out.');
//   });
// }

function init() {
  // 1. Get code for permissions request
  var query = "https://accounts.google.com/o/oauth2/v2/auth?";
  query = query + "client_id=852432978600-1b6mpfj1tven4p1dcqqbgpudgcpjv90k.apps.googleusercontent.com";
  query = query + "&" + "response_type=code";
  var googleRequest = new XMLHttpRequest();
  googleRequest.open('GET', query, false);
  googleRequest.send();

  if (googleRequest.readyState != 4) {
    // init();
    console.log("NOT READY");
    return;
  }

  if (googleRequest.status != 200) {
    alert("Invalid request. Did not receive code 200.");
    return;
  }


}
