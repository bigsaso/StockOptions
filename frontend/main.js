//Build Tabulator
var table = new Tabulator("#options-table", {
    ajaxURL:"http://localhost:5000/getNasdaq100",
    layout:"fitColumns",
    placeholder:"NASDAQ100 Not Scanned",
    columns:[
        {title:"Ticker",headerHozAlign:"center", field:"Ticker", hozAlign: 'center', width:200},
        {title:"Status",headerHozAlign:"center", field:"Status", hozAlign: 'center', formatter: CallPutFormat, width:100},
        {title:"Streak",headerHozAlign:"center", field:"Streak", hozAlign: 'center', width:100},
        // {title:"RSI",headerHozAlign:"center", field:"RSI", width:80},
        {title:"ST Sentiment",headerHozAlign:"center", field:"ST Sentiment", hozAlign: 'center', formatter: SentimentFormat, width:150},
        {title:"LT Analysis",headerHozAlign:"center", field:"LT Analysis"},
        {title:"Warnings",headerHozAlign:"center", field:"Warnings"},
        {title:"Scan Date",headerHozAlign:"center", field:"Scan Date", hozAlign: 'center', width:150},
    ],
});

//Load data into table
document.getElementById("getNASDAQ").addEventListener("click", function(){
    table.setData("http://localhost:5000/getNasdaq100");
});

//Update data
let checkButton = document.getElementById("checkNASDAQ")
checkButton.addEventListener("click", function(){
    checkButton.innerHTML = 'Updating...';
    fetch("http://localhost:5000/checkNasdaq100", {method: 'POST'})
    .then(checkButton.innerHTML = 'Update tickers')
    .catch(error => console.log(error))
});

//Formatter for Call/Put Column
function CallPutFormat(cell) {
    let status = cell.getRow().getData()['Status'];
    let cellElement = cell.getElement();
    let rowIndex = cell.getRow().getPosition(true) + 1;

    // Define green (Call) colour for row
    if (rowIndex % 2 == 0){
        var green = '#5ef286';
    }else{
        var green = '#a6ffbe'; 
    }

    // Define red (Put) colour for row
    if (rowIndex % 2 == 0){
        var red = '#ff9191';
    }else{
        var red = '#ffa3a3'; 
    }

    if (status == 'Call'){
        cellElement.style.backgroundColor = green;
        return 'Call'
    }
    else if(status == 'Put'){
        cellElement.style.backgroundColor = red;
        return 'Put'
    }
}

//Formatter for Sentiment Column
function SentimentFormat(cell) {
    let sentiment = cell.getRow().getData()['ST Sentiment'];
    let cellElement = cell.getElement();
    let rowIndex = cell.getRow().getPosition(true) + 1;
    
    // Define green (Buy) colour for row
    if (rowIndex % 2 == 0){
        var green = '#5ef286';
    }else{
        var green = '#a6ffbe'; 
    }

    // Define red (Sell) colour for row
    if (rowIndex % 2 == 0){
        var red = '#ff9191';
    }else{
        var red = '#ffa3a3'; 
    }

    if (sentiment == '  buy '){
        cellElement.style.backgroundColor = green;
        return 'Buy'
    }
    else if(sentiment == '  Weak   buy '){
        cellElement.style.backgroundColor = green;
        return 'Weak Buy'
    }
    else if(sentiment == '  Strong   buy '){
        cellElement.style.backgroundColor = green;
        return 'Strong Buy'
    }
    else if(sentiment == '  sell '){
        cellElement.style.backgroundColor = red;
        return 'Sell'
    }
    else if(sentiment == '  Weak   sell '){
        cellElement.style.backgroundColor = red;
        return 'Weak Sell'
    }
    else if(sentiment == '  Strong   sell '){
        cellElement.style.backgroundColor = red;
        return 'Strong Sell'
    }
}