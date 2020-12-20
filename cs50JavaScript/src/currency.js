document.addEventListener('DOMContentLoaded', () => {

    document.querySelector('form').onsubmit = () => {
        fetch('https://api.exchangeratesapi.io/latest?base=USD')
            .then((response) => {
                return response.json()
            }).then(data => {
                const currency = document.querySelector('#currency').value.toUpperCase();
                const rate = data.rates[currency];
                if (rate !== undefined ) {
                    document.querySelector('#result').innerHTML = `${rate} ${currency}` ;
                    
                }else{
                    document.querySelector('#result').innerHTML = '404 Not Defined';
                }
            }).catch(error => {
                console.log(`Error: ${error}`);
            })
        return false;
    }
})