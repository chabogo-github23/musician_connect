document.addEventListener('DOMContentLoaded', function() {
    const passwordInput = document.getElementById('id_password1');
    const strengthBar = document.querySelector('.strength-bar');
    const hints = document.querySelectorAll('.hint');
  
    if (passwordInput) {
      passwordInput.addEventListener('input', function() {
        const password = this.value;
        let strength = 0;
        
        // Check length
        if (password.length >= 8) {
          strength += 1;
          hints[0].classList.add('valid');
        } else {
          hints[0].classList.remove('valid');
        }
        
        // Check for numbers
        if (/\d/.test(password)) {
          strength += 1;
          hints[1].classList.add('valid');
        } else {
          hints[1].classList.remove('valid');
        }
        
        // Check for special chars
        if (/[!@#$%^&*(),.?":{}|<>]/.test(password)) {
          strength += 1;
          hints[2].classList.add('valid');
        } else {
          hints[2].classList.remove('valid');
        }
        
        // Update strength meter
        const width = (strength / 3) * 100;
        strengthBar.style.width = `${width}%`;
        
        // Update color
        if (strength === 1) {
          strengthBar.style.backgroundColor = '#ff4757';
        } else if (strength === 2) {
          strengthBar.style.backgroundColor = '#ffa502';
        } else if (strength === 3) {
          strengthBar.style.backgroundColor = '#2ed573';
        }
      });
    }
  
    // Toggle password visibility
    document.querySelectorAll('.toggle-password').forEach(function(button) {
      button.addEventListener('click', function() {
        const icon = this.querySelector('i');
        const input = this.parentElement.querySelector('input');
        
        if (input.type === 'password') {
          input.type = 'text';
          icon.classList.remove('fa-eye');
          icon.classList.add('fa-eye-slash');
        } else {
          input.type = 'password';
          icon.classList.remove('fa-eye-slash');
          icon.classList.add('fa-eye');
        }
      });
    });
  });