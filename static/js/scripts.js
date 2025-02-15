document.getElementById('get-started-btn').addEventListener('click', () => {
  document.getElementById('home-screen').classList.remove('active');
  document.getElementById('session-setup').classList.add('active');
});
document.getElementById('back-btn').addEventListener('click', () => {
  document.getElementById('session-setup').classList.remove('active');
  document.getElementById('home-screen').classList.add('active');
});
document.getElementById('session-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const formData = {
    title: document.getElementById('goal').value,
    description: document.getElementById('description').value,
    max_tasks: document.getElementById('max-tasks').value,
    enable_voice_alerts: document.getElementById('voice-alerts').checked,
    enable_notifications: document.getElementById('notifications').checked,
  };

  try {
    await axios.post('/api/session-goal', formData);
    await axios.post('/api/settings', formData);
    alert('Session started successfully!');
    document.getElementById('session-setup').classList.remove('active');
    document.getElementById('home-screen').classList.add('active');
  } catch (error) {
    alert('Failed to start session. Please try again.');
    console.error(error);
  }
});
