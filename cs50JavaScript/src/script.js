function hello() {
	alert('Hello onClick')
}


let counter = 0;

function count() {
	counter += 1;
	document.querySelector('h2').innerHTML = `Counter ${counter}`;

}

function heading() {
	document.querySelector('h1').innerHTML = `Change`;
}


document.addEventListener('DOMContentLoaded', function () {
	document.querySelector('button').onclick = count;
})

document.addEventListener('DOMContentLoaded', function () {
	document.querySelector('form').onsubmit = function(){
		const name = document.querySelector('#name').value;
		alert(name)
	};
})