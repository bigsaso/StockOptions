const tickerCallsDiv = document.querySelector('#ticker-calls');
const tickerCallsUl = tickerCallsDiv.querySelector('ul');
const tickerPutsDiv = document.querySelector('#ticker-puts');
const tickerPutsUl = tickerPutsDiv.querySelector('ul');
const tickerOnesDiv = document.querySelector('#ticker-ones');
const tickerOnesUl = tickerOnesDiv.querySelector('ul');
const tickerTwosDiv = document.querySelector('#ticker-twos');
const tickerTwosUl = tickerTwosDiv.querySelector('ul');
const tickerThreesDiv = document.querySelector('#ticker-threes');
const tickerThreesUl = tickerThreesDiv.querySelector('ul');
const tickerFoursDiv = document.querySelector('#ticker-fours');
const tickerFoursUl = tickerFoursDiv.querySelector('ul');

document.getElementById('getNASDAQ').addEventListener('click', function(){
    let xhr = new XMLHttpRequest();
    xhr.onload = function(){
        let JSONdata = xhr.response;
        let data = JSON.parse(JSONdata);

        data.Calls.forEach(function(key, val) {
            var li = document.createElement("li")
            li.appendChild(document.createTextNode(key))
            tickerCallsUl.appendChild(li);
        });
        data.Puts.forEach(function(key, val) {
            var li = document.createElement("li")
            li.appendChild(document.createTextNode(key))
            tickerPutsUl.appendChild(li);
        });
        data.OneDayStreak.forEach(function(key, val) {
            var li = document.createElement("li")
            li.appendChild(document.createTextNode(key))
            tickerOnesUl.appendChild(li);
        });
        data.TwoDaysStreak.forEach(function(key, val) {
            var li = document.createElement("li")
            li.appendChild(document.createTextNode(key))
            tickerTwosUl.appendChild(li);
        });
        data.ThreeDaysStreak.forEach(function(key, val) {
            var li = document.createElement("li")
            li.appendChild(document.createTextNode(key))
            tickerThreesUl.appendChild(li);
        });
        data.FourDaysStreak.forEach(function(key, val) {
            var li = document.createElement("li")
            li.appendChild(document.createTextNode(key))
            tickerFoursUl.appendChild(li);
        });

    }
    xhr.open("GET", "http://localhost:5000/getNasdaq100", true);
    xhr.send();
});