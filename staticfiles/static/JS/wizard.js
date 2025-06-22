document.addEventListener('DOMContentLoaded', function() {
    const steps = document.querySelectorAll('.wizard-step');
    const nextBtn = document.getElementById('next-step');
    const prevBtn = document.getElementById('prev-step');
    const submitBtn = document.getElementById('submit-form');
    let currentStep = 0;
  
    function showStep(stepIndex) {
      steps.forEach((step, index) => {
        step.classList.toggle('active', index === stepIndex);
      });
      
      prevBtn.style.display = stepIndex === 0 ? 'none' : 'block';
      nextBtn.style.display = stepIndex === steps.length - 1 ? 'none' : 'block';
      submitBtn.style.display = stepIndex === steps.length - 1 ? 'block' : 'none';
    }
  
    nextBtn.addEventListener('click', () => {
      if (validateStep(currentStep)) {
        currentStep++;
        showStep(currentStep);
      }
    });
  
    prevBtn.addEventListener('click', () => {
      currentStep--;
      showStep(currentStep);
    });
  
    // Tag input functionality
    const tagInput = document.querySelector('.tag-input input');
    tagInput.addEventListener('keydown', function(e) {
      if (e.key === 'Enter' || e.key === ',') {
        e.preventDefault();
        const value = this.value.trim();
        if (value) {
          addTag(value);
          this.value = '';
        }
      }
    });
  
    function addTag(value) {
      const tag = document.createElement('span');
      tag.className = 'tag';
      tag.textContent = value;
      document.querySelector('.tag-container').appendChild(tag);
    }
  
    showStep(0);
  });