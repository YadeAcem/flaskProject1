if (document.URL.includes("/")){
    navbutton = document.getElementById("home")
}
if ( document.URL.includes("info") ) {
    navbutton = document.getElementById("info")
}
if ( document.URL.includes("options") ) {
    navbutton = document.getElementById("option")
}
if ( document.URL.includes("result") ) {
    navbutton = document.getElementById("result")
}
if (document.URL.includes("graph")){
    navbutton = document.getElementById(null)
}

navbutton.style.backgroundColor = "#ddd";