// retreives name from localstorage to display on page.
var name = localStorage.getItem("name");
document.getElementById("dName").innerHTML = name;

// forgets the page it's on because it's not a chat page 
localStorage.removeItem("last");
