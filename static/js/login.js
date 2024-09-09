document.getElementById('login-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    let username = document.getElementById('login-username').value;
    let password = document.getElementById('login-password').value;
  
    const response = await fetch('/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }),
    });
  
    if (response.ok) {
      alert('Login successful!');
    } else {
      alert('Login failed!');
    }
  });
  