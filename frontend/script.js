function setClickListeners(){
    cells = document.getElementsByTagName('td') 
    for(i = 0; i < cells.length; i++){
        cells[i].addEventListener('click', onClick);
    }
}

function onClick(event){
    let arr = []
    tds = document.getElementsByTagName('td')
    for(var i = 0; i < 9; i++){
        symbol = tds[i].innerText
        if(symbol == 'X'){
            arr[i] = 1;
        }
        else if(symbol == 'O'){
            arr[i] = 2
        }
        else{
            arr[i] = 0
        }
    }
    move = event.path[0].id;

    let data = {
        field: arr,
        move: move
    }

    console.log(JSON.stringify(data));
    



    request = new XMLHttpRequest();
    url = 'ain.py';
    request.open('GET', url);
    request.setRequestHeader('Content-Type', 'application/x-www-form-url');
    request.send();
}   

window.onload = function(){
    setClickListeners();
}