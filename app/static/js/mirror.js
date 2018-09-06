(function () {
  var myDrop = document.getElementById("location_code"), // Drop down
    mirror = document.getElementById("location_name"); // "Mirror" text box
  myDrop.onchange = function(){
    dropValue = myDrop.options[myDrop.selectedIndex].text;
    mirror.value = dropValue;
  }
})();

(function () {
  var myDrop = document.getElementById("alternate_pickup_location_code"), // Drop down
    mirror = document.getElementById("alternate_pickup_location"); // "Mirror" text box
  myDrop.onchange = function(){
    dropValue = myDrop.options[myDrop.selectedIndex].text;
    mirror.value = dropValue;
  }
})();  
  
  
(function () {
  var myDrop = document.getElementById("alternate_bookdrop_location_code"), // Drop down
    mirror = document.getElementById("alternate_bookdrop_location"); // "Mirror" text box
  myDrop.onchange = function(){
    dropValue = myDrop.options[myDrop.selectedIndex].text;
    mirror.value = dropValue;
  }
})(); 