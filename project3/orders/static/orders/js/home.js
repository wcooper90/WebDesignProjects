document.addEventListener('DOMContentLoaded', () => {
  // changes the display name by accessing local storage
  var name = document.getElementById("name").value;
  localStorage.setItem('name', name);
  }
});
