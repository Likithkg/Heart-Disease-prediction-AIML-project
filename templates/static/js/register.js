document.addEventListener('DOMContentLoaded', function() {
    // Get the password input fields and the register button
    const passwordField = document.getElementById('password');
    const confirmPasswordField = document.getElementById('confirm-password');
    const passwordMatchBox = document.getElementById('password-match-text');

    // Function to check if passwords match and update message visibility
    function checkPasswords() {
        const password = passwordField.value;
        const confirmPassword = confirmPasswordField.value;
        if (password === confirmPassword && password.length > 0) {
            passwordMatchBox.textContent = 'Passwords match!';
            passwordMatchBox.style.display = 'block'; // Show the box
        } else {
            passwordMatchBox.textContent = 'Passwords do not match!';
            passwordMatchBox.style.display = 'block'; // Show the box even if passwords don't match
        }
    }

    // Add event listeners to password fields for input and change events
    passwordField.addEventListener('input', checkPasswords);
    confirmPasswordField.addEventListener('input', checkPasswords);
});