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
	document.querySelector('form').onsubmit = function () {
		const name = document.querySelector('#name').value;
		alert(name)
	};
})


// * Change font color to red
document.addEventListener('DOMContentLoaded', () => {

	// document.querySelector('#red').onclick = function () {
	// 	document.querySelector('#hello').style.color = 'red';
	// }

	// document.querySelector('#blue').onclick = function () {
	// 	document.querySelector('#hello').style.color = 'blue';
	// }

	// document.querySelector('#green').onclick = function () {
	// 	document.querySelector('#hello').style.color = 'green';
	// }


	document.querySelectorAll('#button').forEach(input => {
		input.onclick = () =>{
			document.querySelector('#hello').style.color = input.dataset.color;
		}
	}) 
});
document.addEventListener('DOMContentLoaded', () => {
	
})

document.addEventListener('DOMContentLoaded', () => {
	document.querySelector('select').onchange =  function()  {
		document.querySelector('#dropHello').style.color = this.value;
	}
})