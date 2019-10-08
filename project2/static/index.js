document.addEventListener('DOMContentLoaded', () => {
      // if name isn't already in localstorage, allows user to pick new name
      if (!localStorage.getItem("name")){
        document.getElementById("hubber").onclick = function () {
        var name = document.getElementById("dName").value;
      	localStorage.setItem('name', name);
        // redirects to channels page
        window.location.href=("http://127.0.0.1:5000/channels");
        }
      }
      else {
        // if the last page the user was on was a chat page, redirects to that page
        if (localStorage.getItem("last")){
          window.location.href=localStorage.getItem("last");
        }
        // otherwise just to the channels page 
        else {
          window.location.href=("http://127.0.0.1:5000/channels");
        }
      }
});
