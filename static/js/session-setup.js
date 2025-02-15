// session-setup.js
document.addEventListener('DOMContentLoaded', () => {
  const backBtn = document.getElementById('back-btn');
  const continueBtn = document.getElementById('continue-btn');
  const form = document.getElementById('session-form');
  const step1 = document.getElementById('step-1');
  const step2 = document.getElementById('step-2');

  backBtn.addEventListener('click', () => {
    window.history.back();
  });

  continueBtn.addEventListener('click', () => {
    if (document.getElementById('goal').value.trim() === '') {
      alert('Please enter your main goal for this session.');
      return;
    }
    step1.classList.remove('active');
    step2.classList.add('active');
  });

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const sessionData = {
      title: document.getElementById('goal').value,
      description: document.getElementById('description').value,
      max_tasks: document.getElementById('max-tasks').value,
      enable_voice_alerts: document.getElementById('voice-alerts').checked,
      enable_notifications: document.getElementById('notifications').checked,
    };

    try {
      await axios.post('/api/session-goal', sessionData);
      await axios.post('/api/settings', sessionData);
      alert('Session started successfully!');
      window.location.href = '/';
    } catch (error) {
      console.error('Error setting up session:', error);
      alert('Failed to set up session. Please try again.');
    }
  });
});
