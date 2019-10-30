function setClickListeners(){
    cells = document.getElementsByClassName('cell')
    for(i = 0; i < cells.length; i++){
        cells[i].addEventListener('click', onClick);
    }
}

function onClick(event){
    path = event.path;
    console.log(path)
}


window.onload = function(){
    setClickListeners();
}