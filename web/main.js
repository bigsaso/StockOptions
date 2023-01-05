//Build Tabulator
var table = new Tabulator("#options-table", {
    layout:"fitColumns",
    placeholder:"No Data Set",
    columns:[
        {title:"Ticker", field:"Ticker", width:200},
        {title:"Status", field:"Status"},
        {title:"Streak", field:"Streak"},
        {title:"Scan Date", field:"Scan Date"},
    ],
});

//trigger AJAX load on "Load Data via AJAX" button click
document.getElementById("getNASDAQ").addEventListener("click", function(){
    table.setData("http://localhost:5000/getNasdaq100");
});