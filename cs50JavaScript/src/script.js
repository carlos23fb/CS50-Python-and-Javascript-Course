function hello() {
	alert('Hello onClick')
}

if (!localStorage.getItem('counter')) {
	localStorage.setItem('counter', 0)
}

function count() {

	let counter = localStorage.getItem('counter');
	counter = parseInt(counter)
	counter += 1;
	dataType = typeof (counter)
	document.querySelector('h2').innerHTML = `${dataType} ${counter}`;
	localStorage.setItem('counter', counter);
}

function heading() {
	document.querySelector('h1').innerHTML = `Change`;
}


document.addEventListener('DOMContentLoaded', function () {
	document.querySelector('button').onclick = count;
})

document.addEventListener('DOMContentLoaded', function () {
	document.querySelector('form').onsubmit = function () {
		const name = document.querySelector('#name').value;
		alert(name)
	};
})


document.addEventListener('DOMContentLoaded', () => {
	let current = localStorage.getItem('counter');
	current = parseInt(current);
	let dataType = typeof(current);
	document.querySelector('h2').innerHTML = `${dataType} ${current}`;
})


// * Change font color to red
document.addEventListener('DOMContentLoaded', () => {


// TODO:
	document.querySelectorAll('#button').forEach(input => {
		input.onclick = () => {
			document.querySelector('#hello').style.color = input.dataset.color;
		}
	})
});


document.addEventListener('DOMContentLoaded', () => {

})

document.addEventListener('DOMContentLoaded', () => {
	document.querySelector('select').onchange = function () {
		document.querySelector('#dropHello').style.color = this.value;
	}
});