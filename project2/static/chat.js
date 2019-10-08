document.addEventListener('DOMContentLoaded', () => {
    // to store previous and new chats in, to be pushed to localstorage for specific chat channel
    var chats = new Array;
    // gets chat name and user name
    const chatName = document.getElementById("chatName");
    document.getElementById("name").innerHTML = localStorage.getItem("name");
    // if localstorage already has chats stored under this name, retreives and displays them
    if (localStorage.getItem(chatName.innerHTML)) {
      var existingChats = localStorage.getItem(chatName.innerHTML);
      var j = JSON.parse(existingChats).length;
      var i;
      for (i = 0; i < j; i++) {
        chats.push(JSON.parse(existingChats)[i]);
        const li = document.createElement('li');
        li.innerHTML = JSON.parse(existingChats)[i];
        document.querySelector('#chats').append(li);
      }
    }
    // page remembers the location of this chat page so that if user exits, when they reopen this page will show up
    prev = window.location;
    localStorage.setItem("last", prev);

    // submit chat function
    function submitChat(){
      const chat = document.getElementById("chat").value;
      const user = localStorage.getItem("name");
      // sends to flask application
      socket.emit('submit chat', {'chat': chat, 'user': user, 'chatName': chatName});
      document.getElementById("chat").value = "";
    };
    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    // When connected, allow user to push enter to submit chats
    socket.on('connect', () => {

      // from stackoverflow
        document.onkeydown=function(evt){
          var keyCode = evt ? (evt.which ? evt.which : evt.keyCode) : event.keyCode;
          if (keyCode == 13){
            submitChat();
          }
        }
    });

    // When a new chat is announced, add to the unordered list
    socket.on("chats", data => {
      // from stackoverflow, date and time properly formatted
      var d = new Date();
      var hr = d.getHours();
      var min = d.getMinutes();
      if (min < 10) {
          min = "0" + min;
      }
      var ampm = "am";
      if( hr > 12 ) {
          hr -= 12;
          ampm = "pm";
      }
      var date = d.getDate();
      var year = d.getFullYear();
      var mil = d.getMilliseconds();
      var n = hr + ":" + min + ":" + mil + ampm + " " + date + " " + year;
      // formats all the correct information and adds it dynamically to page
      const li = document.createElement('li');
      li.innerHTML = `${data.user} at ` + n + `: ${data.chat}`;
      chats.push(li.innerHTML);
      localStorage.setItem(chatName.innerHTML, JSON.stringify(chats));
      // if there are more than 100 chats, deletes the first one 
      if (chats.length > 100) {
        chats.shift();
      }
      document.querySelector('#chats').append(li);
    });
});
