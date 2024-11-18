const titulo = document.getElementById('titulo');
const destinatario = document.getElementById('destinatario');
const asunto = document.getElementById('asunto');
const cuerpo = document.getElementById('cuerpo');

const form = document.querySelector('form');
form.addEventListener('submit', (event) => {
  event.preventDefault();
  const data = {
    destinatario: destinatario.value,
    asunto: asunto.value,
    cuerpo: cuerpo.value
  };
  console.log(data);
  fetch('/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
  .then(response => response.json())
  .then(data => {
    console.log('Success:', data);
    titulo.innerHTML = 'Correo enviado';
    destinatario.value = '';
    asunto.value = '';
    cuerpo.value = '';
  })
  .catch((error) => {
    console.error('Error:', error);
    titulo.innerHTML = 'Error al enviar el correo';
  });
});