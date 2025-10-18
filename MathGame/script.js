let currentChallenge = {};
let challenges = [
  { question: "7 × _ = 56", answer: 8 },
  { question: "LCM of 12, 18 and 24", answer: 72 },
  { question: "Prime number less than 20", answer: 13 },
  { question: "4, 8, 16, __", answer: 32 },
  { question: "Next number: 5, 10, 20, 40, __", answer: 80 }
];
let currentIndex = 0;

function startGame() {
  document.getElementById('start-button').style.display = 'none';
  document.getElementById('game-screen').style.display = 'block';
  currentIndex = 0;
  loadChallenge();
}

function loadChallenge() {
  if (currentIndex >= challenges.length) {
    document.getElementById('challenge').innerText = "🎉 You beat the Mathrix! Well done, ZeroByte!";
    document.getElementById('answer').style.display = 'none';
    return;
  }
  currentChallenge = challenges[currentIndex];
  document.getElementById('challenge').innerText = currentChallenge.question;
  document.getElementById('feedback').innerText = "";
  document.getElementById('answer').value = "";
  document.getElementById('answer').focus();
}

function submitAnswer() {
  let userAnswer = parseInt(document.getElementById('answer').value);
  if (userAnswer === currentChallenge.answer) {
    document.getElementById('feedback').innerText = "✅ Correct! Moving on...";
    currentIndex++;
    setTimeout(loadChallenge, 1000);
  } else {
    document.getElementById('feedback').innerText = "❌ Incorrect. Try again.";
  }
}
