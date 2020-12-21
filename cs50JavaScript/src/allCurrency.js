document.addEventListener('DOMContentLoaded', () => {
    const allCurrency = async () =>{
        const res = await fetch('https://api.exchangeratesapi.io/latest?base=USD')
        const currencies = await res.json();
        console.log(currencies);
        const rates = currencies.rates;
        for(let index in rates){
            const currency = index;
            const value = rates[index];
            createLi(currency, value)
        }
    }
    allCurrency()
    const createLi = (currency, value) =>{
        let currencyLi = document.createElement('li')
        let liCurrency = `
        <li>${currency}: ${value}</li>
        `;
        currencyLi.innerHTML = liCurrency;
        document.querySelector('#currencies').appendChild(currencyLi)

    } 
})