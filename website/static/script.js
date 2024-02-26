const currentLocation = location.href;
const btnBar = document.getElementById("btn-bar");
const menuItem = btnBar.querySelectorAll("a");

for (let i = 0; i < menuItem.length; i++) {
    if (menuItem[i].href === currentLocation) {
        menuItem[i].className = "active";
    }
}