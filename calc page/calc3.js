const mathInput = document.getElementById('mathInput');
const resultDiv = document.getElementById('result');

// Initialize SpeechRecognition object
const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();

// Set properties for speech recognition
recognition.interimResults = false;
recognition.maxAlternatives = 1;

// Event listener for speech recognition result
recognition.onresult = function(event) {
    const spokenExpression = event.results[0][0].transcript;
    mathInput.value = spokenExpression;
    acknowledgeInput(spokenExpression);
};

// Function to acknowledge the user's input
function acknowledgeInput(input) {
    speak(`You said: ${input}`);
}

function solveMathProblem() {
    const mathProblem = mathInput.value;
    try {
        const result = math.evaluate(mathProblem);
        speak(`The answer is ${result}`);
        resultDiv.textContent = `Answer: ${result}`;
    } catch (error) {
        speak('Invalid math problem. Please try again.');
        resultDiv.textContent = 'Invalid math problem. Please try again.';
    }
}

// Function to start speech recognition
function startSpeechRecognition() {
    recognition.start();
}

// Function to convert text to speech
function speak(message) {
    const speechSynthesis = window.speechSynthesis;
    const speechMessage = new SpeechSynthesisUtterance(message);
    speechSynthesis.speak(speechMessage);
}

