const chatLog = document.getElementById("chat-log");
const userInput = document.getElementById("user-input");
const sendButton = document.getElementById("send-button");

let userName = "";
let songType = "";
let messageQueue = [];

function updateChatLog(message, isUserMessage) {
  const messageDiv = document.createElement("div");
  messageDiv.className = isUserMessage ? "user-message" : "bot-message";
  messageDiv.textContent = message;

  if (isUserMessage) {
    messageDiv.classList.add("left");
  } else {
    messageDiv.classList.add("right");
  }

  chatLog.appendChild(messageDiv);
}

function sendAutomaticMessage(message) {
  messageQueue.push(message);
  processMessageQueue();
}

function processMessageQueue() {
  if (messageQueue.length > 0) {
    const message = messageQueue.shift();
    updateChatLog(message, false);
    setTimeout(processMessageQueue, 1000); 
  }
}

sendAutomaticMessage("Welcome to Musicana. What is your name?");

sendButton.addEventListener("click", () => {
  const userMessage = userInput.value;

  if (!userName) {
    userName = userMessage;
    updateChatLog(`${userName}: ${userMessage}`, true);
    sendAutomaticMessage(`Hi dear ${userName}, I hope you are doing great. What type of songs you want to listen?`);
  } else if (!songType) {
    songType = userMessage;
    updateChatLog(`${userName}: ${userMessage}`, true);
    sendAutomaticMessage("Thanks for chatting! Please click the Fetch Recommendation button, I will recommend you some songs.");
    sendUserMessageToBackend(userName, songType);
  }

  userInput.value = "";
});

function sendUserMessageToBackend(userName, songType) {
  const data = {
    userName: userName,
    songType: songType
  };

  fetch("/save_song_type", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  })
  .then(response => response.json())
  .then(responseData => {
    // Handle response if needed
  })
  .catch(error => {
    console.error("Error sending data to backend:", error);
  });
}

const fetchRecommendationsButton = document.getElementById("fetch-recommendations-button");
fetchRecommendationsButton.addEventListener("click", () => {
  fetchRecommendations(songType);
});

function fetchRecommendations(songType) {
  // Check if the selected song type is valid
  const validSongTypes = ["hindi", "punjabi", "english", "sad", "rock", "classical", "pop", "western", "romantic", "happy", "angry"];
  if (validSongTypes.includes(songType)) {
    // Redirect to the recommendations page with the song type as a query parameter
    window.location.href = `/recommendation?songType=${songType}`;
  } else {
    console.error("Invalid song type:", songType);
  }
}
