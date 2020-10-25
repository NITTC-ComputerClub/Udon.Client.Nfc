eel.expose(changeDisplay);
function changeDisplay(elementId){
    document.getElementsByClassName("components").style.display="none";
    document.getElementById(elementId).style.display="block";
}