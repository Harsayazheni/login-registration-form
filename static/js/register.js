document.getElementById('register-form').addEventListener('submit', async function(event) {
  event.preventDefault();
  let username = document.getElementById('username').value;
  let email = document.getElementById('email').value;
  let password = document.getElementById('password').value;

  const response = await fetch('/register', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ username, email, password }),
  });

  if (response.ok) {
    alert('Registration successful!');
  } else {
    alert('Registration failed!');
  }
});
