const COMPUTER = 'O'
const HUMAN = 'X'

function setClickListeners(){
    cells = document.getElementsByTagName('td') 
    for(i = 0; i < cells.length; i++){
        cells[i].addEventListener('click', onClick);
    }
}

function onClick(event){
    if(event.currentTarget.innerText != ''){
        return
    }

    event.currentTarget.innerText = 'X'
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

    datastr = JSON.stringify(data)
    

    request = new XMLHttpRequest();
    url = '/solve' + '*?data=' + datastr
    request.open('GET', url);
    request.send();
    request.onload = function() {
        resp = JSON.parse(request.response)
        time = resp.time

        move = resp.move.toString()
        document.getElementById(move).innerText = 'O'
      };
}   

window.onload = function(){
    setClickListeners();
}