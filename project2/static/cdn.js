document.addEventListener('DOMContentLoaded', () => {
  // changes the display name by accessing local storage
  document.getElementById("hubber").onclick = function () {
  var name = document.getElementById("dName").value;
  localStorage.setItem('name', name);
  // redirects to channels page 
  window.location.href=("http://127.0.0.1:5000/channels");
  }
});
