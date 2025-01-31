const ball = document.getElementById('ball');
const sidebar = document.getElementById('sidebar');

// Function to toggle the sidebar
function toggleSidebar() {
  sidebar.classList.toggle('open');
}

// Function to start pulsating
function startPulsating() {
  ball.style.animationPlayState = 'running';
}

// Function to stop pulsating
function stopPulsating() {
  ball.style.animationPlayState = 'paused';
}

// Example: Trigger pulsating when speaking
function speak(text) {
  startPulsating();  // Start pulsating when model starts speaking
  
  // Simulate model speaking with text-to-speech (replace with actual TTS code)
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.onend = stopPulsating;  // Stop pulsating when speaking ends
  speechSynthesis.speak(utterance);
}

// Example usage
speak("Hello, I'm Eclipse.");