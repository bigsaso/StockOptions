const ticker1 = document.querySelector('#ticker1');
const tickerList1 = ticker1.querySelector('ul');

function updateTickerWidth() {
  let tickerWidth1 = 0;
  tickerList1.querySelectorAll('li').forEach(item => {
    tickerWidth1 += item.offsetWidth;
  });
  ticker1.style.width = `${tickerWidth1}px`;
}

ticker1.addEventListener('animationiteration', () => {
  ticker1.style.animation = 'ticker linear infinite';
});

updateTickerWidth()
