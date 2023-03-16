/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function myFunction() {
    document.getElementById("MyNavDown").classList.toggle("show");
}
function myFunction2() {
  document.getElementById("MyNavDown2").classList.toggle("show");
}
function myFunction3() {
  document.getElementById("MyNavDown3").classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.nav-btn')) {

    var dropdowns = document.getElementsByClassName("nav-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}