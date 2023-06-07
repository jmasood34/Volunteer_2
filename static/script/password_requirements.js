const passwordField = document.getElementById('id_password1');
const passwordRequirements = document.getElementById('password-requirements');

passwordField.addEventListener('focus', () => {
  passwordRequirements.style.display = 'block';
});

passwordField.addEventListener('blur', () => {
  passwordRequirements.style.display = 'none';
});
