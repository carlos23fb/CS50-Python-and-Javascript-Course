function hello(){
    alert('Hello onClick')
}


let counter = 0;

function count(){
    counter += 1;
    document.querySelector('h2').innerHTML = `Counter ${counter}`;
    
}

function heading(){
    document.querySelector('h1').innerHTML = `Change`;
}