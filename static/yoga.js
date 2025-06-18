const form = document.querySelector('form'); // Use form tag to select the form
const formContainer = document.getElementById("formContainer");
const resultPage = document.getElementById("resultPage");
const resultContent = document.getElementById("resultContent");

function showForm() {
  formContainer.style.display = 'block';
  document.querySelector('.main-content').style.display = 'none';
}


