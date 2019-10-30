function setClickListeners(){
    cells = document.getElementsByClassName('cell')
    for(i = 0; i < cells.length; i++){
        cells[i].addEventListener('click', onClick);
    }
}

function onClick(event){
    path = event.path;
    console.log(path)
    request = new XMLHttpRequest();
    url = 'main.py?salamaleukym=True';
    request.open('GET', url);
    request.setRequestHeader('Content-Type', 'application/x-www-form-url');
    request.send();
}


window.onload = function(){
    setClickListeners();
}