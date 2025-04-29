<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Emotion Detection Chatbot</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f9fafb;
      margin: 0;
      padding: 0;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      height: 100vh;
      text-align: center;
    }

    h1 {
      color: #333;
      font-size: 30px;
      margin-bottom: 10px;
    }

    p {
      font-size: 16px;
      margin-bottom: 30px;
      color: #555;
    }

    .chatbot-container {
      background-color: #fff;
      padding: 30px;
      border-radius: 8px;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
      width: 320px;
    }

    .chatbot-container h2 {
      font-size: 20px;
      margin-bottom: 20px;
      color: #444;
    }

    .chatbot-container textarea {
      width: 100%;
      padding: 12px;
      font-size: 15px;
      border-radius: 6px;
      border: 1px solid #ccc;
      resize: none;
      margin-bottom: 10px;
      box-sizing: border-box;
    }

    .chatbot-container button {
      background-color: #4CAF50;
      color: white;
      padding: 10px;
      border: none;
      border-radius: 6px;
      width: 100%;
      cursor: pointer;
      font-size: 15px;
    }

    .chatbot-container button:hover {
      background-color: #45a049;
    }

    footer {
      margin-top: 20px;
      color: #777;
      font-size: 13px;
    }

    footer a {
      color: #4CAF50;
      text-decoration: none;
    }

    /* Modal styles */
    #modal {
      display: none;
      position: fixed;
      top: 0; left: 0;
      width: 100%; height: 100%;
      background-color: rgba(0, 0, 0, 0.6);
      justify-content: center;
      align-items: center;
    }

    #modalContent {
      background: white;
      padding: 25px;
      border-radius: 8px;
      text-align: center;
      width: 80%;
      max-width: 400px;
    }

    #modal button {
      background-color: #f44336;
      color: white;
      border: none;
      padding: 8px 18px;
      margin-top: 20px;
      border-radius: 5px;
      cursor: pointer;
      font-size: 14px;
    }

    #modal h3 {
      margin-bottom: 10px;
    }

    #emotionText, #feedbackText {
      margin: 5px 0;
    }
  </style>
</head>
<body>

<h1>Welcome to Emotion Detection Chatbot 🤖</h1>
<p>I'm here to detect the emotion in your text and provide you with some feedback.</p>

<div class="chatbot-container">
  <h2>Let's Get Started!</h2>
  <form id="emotionForm">
    <textarea rows="4" cols="30" id="text_input" name="text_input" placeholder="Type something..."></textarea>
    <p style="font-size: 12px; color: #888;">Note: Please enter a sentence for emotion detection.</p>
    <button type="submit">Predict Emotion</button>
  </form>
</div>

<!-- Modal Dialog -->
<div id="modal">
  <div id="modalContent">
    <h3>Emotion Result</h3>
    <p id="emotionText"></p>
    <p id="feedbackText"></p>
    <button onclick="document.getElementById('modal').style.display='none'">Close</button>
  </div>
</div>

<footer>
  <p>Created with ❤️ by Jubayer Hossain | <a href="https://github.com/jubayerhossain625">GitHub</a></p>
</footer>

<script>
document.getElementById('emotionForm').addEventListener('submit', function(e) {
  e.preventDefault();
  const textInput = document.getElementById('text_input').value;

  fetch('http://127.0.0.1:5000/api/predict', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text_input: textInput })
  })
  .then(response => response.json())
  .then(data => {
    document.getElementById('emotionText').textContent = `Emotion: ${data.emotion}`;
    document.getElementById('feedbackText').textContent = data.feedback;
    document.getElementById('modal').style.display = 'flex';
  })
  .catch(error => {
    alert("Error connecting to the server.");
    console.error(error);
  });
});
</script>

</body>
</html>
