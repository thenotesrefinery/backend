var openNav;

$( document ).ready(function() {
    openNav = false;
});

function toggleNav() {
    if (!openNav) {
        openNav = true;
        document.getElementById("mySidenav").style.width = "180px";
        document.getElementsByTagName("body")[0].style.marginLeft = "180px";
        // document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
    } else {
        openNav = false;
        document.getElementById("mySidenav").style.width = "0";
        document.getElementsByTagName("body")[0].style.marginLeft= "0";
        // document.body.style.backgroundColor = "white";
    }
}
