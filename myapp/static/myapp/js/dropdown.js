const elements = document.querySelector("#myDiv");

function hi(){

    if(elements.style.display === "none"){
    elements.setAttribute('style', 'display: block');
} else {
    elements.setAttribute('style', 'display: none');

}
}

