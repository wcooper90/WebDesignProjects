document.addEventListener('DOMContentLoaded', () => {
      // if name isn't already in localstorage, allows user to pick new name
        document.getElementById("submit").onclick = function () {
        // use bootbox js to confirm user wants to place order
        var txt;
        if (confirm("Place Order?")) {
          txt = "Order Placed";
        }
        else {
          event.preventDefault()
        }
      }
});
