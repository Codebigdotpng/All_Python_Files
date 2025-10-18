// Game elements
const emojis = ['🐶', '🐱', '🐭', '🐹', '🐰', '🦊', '🐻', '🐼'];
const gameBoard = document.querySelector('.game-board');
const movesCount = document.getElementById('moves-count');
const timerElement = document.getElementById('timer');
const restartButton = document.getElementById('restart-button');
const backButton = document.getElementById('back-button');
const modeSelection = document.getElementById('mode-selection');
const gameArea = document.getElementById('game-area');
const singlePlayerBtn = document.getElementById('single-player-btn');
const twoPlayerBtn = document.getElementById('two-player-btn');
const playerOne = document.getElementById('player-one');
const playerTwo = document.getElementById('player-two');
const scoreOne = document.getElementById('score-one');
const scoreTwo = document.getElementById('score-two');
const playerDisplay = document.getElementById('player-display');
const soundButton = document.getElementById('sound-button');

// Sound variables
let audioContext;
let soundsEnabled = true;

// Game state variables
let cards = [];
let flippedCards = [];
let moves = 0;
let matchedPairs = 0;
let timer = 0;
let timerInterval;
let gameStarted = false;
let isTwoPlayerMode = false;
let currentPlayer = 1;
let playerOneScore = 0;
let playerTwoScore = 0;

// Initialize audio context
function initAudio() {
    // Create audio context on first user interaction (browser requirement)
    if (!audioContext) {
        audioContext = new (window.AudioContext || window.webkitAudioContext)();
    }
}

// Toggle sounds on/off
function toggleSounds() {
    soundsEnabled = !soundsEnabled;
    
    if (soundsEnabled) {
        soundButton.textContent = '🔊';
        soundButton.classList.remove('muted');
    } else {
        soundButton.textContent = '🔇';
        soundButton.classList.add('muted');
    }
}

// Generate card flip sound
function playFlipSound() {
    if (!soundsEnabled || !audioContext) return;
    
    const oscillator = audioContext.createOscillator();
    const gainNode = audioContext.createGain();
    
    oscillator.type = 'sine';
    oscillator.frequency.setValueAtTime(300, audioContext.currentTime);
    oscillator.frequency.exponentialRampToValueAtTime(200, audioContext.currentTime + 0.2);
    
    gainNode.gain.setValueAtTime(0.1, audioContext.currentTime);
    gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.2);
    
    oscillator.connect(gainNode);
    gainNode.connect(audioContext.destination);
    
    oscillator.start();
    oscillator.stop(audioContext.currentTime + 0.2);
}

// Generate match sound
function playMatchSound() {
    if (!soundsEnabled || !audioContext) return;
    
    const oscillator = audioContext.createOscillator();
    const gainNode = audioContext.createGain();
    
    oscillator.type = 'sine';
    oscillator.frequency.setValueAtTime(600, audioContext.currentTime);
    oscillator.frequency.exponentialRampToValueAtTime(800, audioContext.currentTime + 0.1);
    
    gainNode.gain.setValueAtTime(0.2, audioContext.currentTime);
    gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.3);
    
    oscillator.connect(gainNode);
    gainNode.connect(audioContext.destination);
    
    oscillator.start();
    oscillator.stop(audioContext.currentTime + 0.3);
}

// Generate victory sound
function playVictorySound() {
    if (!soundsEnabled || !audioContext) return;
    
    // Play a little victory melody
    const notes = [400, 500, 600, 800];
    const duration = 0.15;
    
    notes.forEach((freq, index) => {
        const oscillator = audioContext.createOscillator();
        const gainNode = audioContext.createGain();
        
        oscillator.type = 'sine';
        oscillator.frequency.value = freq;
        
        gainNode.gain.setValueAtTime(0.2, audioContext.currentTime + index * duration);
        gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + (index + 1) * duration);
        
        oscillator.connect(gainNode);
        gainNode.connect(audioContext.destination);
        
        oscillator.start(audioContext.currentTime + index * duration);
        oscillator.stop(audioContext.currentTime + (index + 1) * duration);
    });
}

// Mode selection
singlePlayerBtn.addEventListener('click', () => {
    isTwoPlayerMode = false;
    startNewGame();
});

twoPlayerBtn.addEventListener('click', () => {
    isTwoPlayerMode = true;
    startNewGame();
});

// Start a new game based on selected mode
function startNewGame() {
    modeSelection.classList.add('hidden');
    gameArea.classList.remove('hidden');
    
    // Show/hide player display based on mode
    if (isTwoPlayerMode) {
        playerDisplay.style.display = 'flex';
        setCurrentPlayer(1);
    } else {
        playerDisplay.style.display = 'none';
    }
    
    restartGame();
}

// Set current player and update UI
function setCurrentPlayer(player) {
    currentPlayer = player;
    
    if (player === 1) {
        playerOne.classList.add('active');
        playerTwo.classList.remove('active');
    } else {
        playerOne.classList.remove('active');
        playerTwo.classList.add('active');
    }
}

// Create game board
function createBoard() {
    // Double the emojis to create pairs
    const cardValues = [...emojis, ...emojis];
    
    // Shuffle the cards
    for (let i = cardValues.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [cardValues[i], cardValues[j]] = [cardValues[j], cardValues[i]];
    }
    
    // Create card elements
    cardValues.forEach((value, index) => {
        const card = document.createElement('div');
        card.classList.add('card');
        card.dataset.value = value;
        card.dataset.index = index;
        
        card.addEventListener('click', flipCard);
        gameBoard.appendChild(card);
        cards.push(card);
    });
}

// Flip a card
function flipCard() {
    const selectedCard = this;
    
    // Initialize audio on first interaction
    initAudio();
    
    // Ignore if card is already flipped or matched
    if (selectedCard.classList.contains('flipped') || 
        selectedCard.classList.contains('matched')) {
        return;
    }
    
    // Start timer on first card flip (single player mode)
    if (!gameStarted && !isTwoPlayerMode) {
        startTimer();
        gameStarted = true;
    }
    
    // Play flip sound
    playFlipSound();
    
    // Flip the card
    selectedCard.classList.add('flipped');
    selectedCard.textContent = selectedCard.dataset.value;
    
    flippedCards.push(selectedCard);
    
    // Check for match if two cards are flipped
    if (flippedCards.length === 2) {
        moves++;
        movesCount.textContent = moves;
        
        checkForMatch();
    }
}

// Animate matched cards
function animateMatch(card1, card2) {
    // Play match sound
    playMatchSound();
    
    card1.classList.add('animate__animated', 'animate__pulse');
    card2.classList.add('animate__animated', 'animate__pulse');
}

// Show confetti celebration
function showConfetti() {
    // Basic confetti explosion
    confetti({
        particleCount: 100,
        spread: 70,
        origin: { y: 0.6 }
    });
    
    // Create colorful confetti shower that lasts longer
    setTimeout(() => {
        const duration = 3000;
        const end = Date.now() + duration;
        
        (function frame() {
            confetti({
                particleCount: 2,
                angle: 60,
                spread: 55,
                origin: { x: 0 },
                colors: ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ff00ff']
            });
            
            confetti({
                particleCount: 2,
                angle: 120,
                spread: 55,
                origin: { x: 1 },
                colors: ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ff00ff']
            });
            
            if (Date.now() < end) {
                requestAnimationFrame(frame);
            }
        })();
    }, 250);
}

// Display winner message with animation
function displayWinnerMessage(message) {
    const winnerText = document.createElement('div');
    winnerText.classList.add('winner-text', 'animate__animated', 'animate__bounceIn');
    winnerText.textContent = message;
    
    // Insert the message before the button panel
    const buttonPanel = document.querySelector('.button-panel');
    gameArea.insertBefore(winnerText, buttonPanel);
}

// Check if the two flipped cards match
function checkForMatch() {
    const [card1, card2] = flippedCards;
    
    if (card1.dataset.value === card2.dataset.value) {
        // Cards match
        card1.classList.add('matched');
        card2.classList.add('matched');
        
        // Add match animation
        animateMatch(card1, card2);
        
        matchedPairs++;
        
        // Update score in two-player mode
        if (isTwoPlayerMode) {
            if (currentPlayer === 1) {
                playerOneScore++;
                scoreOne.textContent = playerOneScore;
            } else {
                playerTwoScore++;
                scoreTwo.textContent = playerTwoScore;
            }
        }
        
        // Check if all pairs are matched
        if (matchedPairs === emojis.length) {
            endGame();
        }
    } else {
        // Cards don't match, flip them back
        setTimeout(() => {
            card1.classList.remove('flipped');
            card2.classList.remove('flipped');
            card1.textContent = '';
            card2.textContent = '';
            
            // Switch player in two-player mode
            if (isTwoPlayerMode) {
                setCurrentPlayer(currentPlayer === 1 ? 2 : 1);
            }
        }, 1000);
    }
    
    // Reset flipped cards array
    flippedCards = [];
}

// Start the timer
function startTimer() {
    timerInterval = setInterval(() => {
        timer++;
        timerElement.textContent = timer;
    }, 1000);
}

// End the game
function endGame() {
    clearInterval(timerInterval);
    
    // Play victory sound
    playVictorySound();
    
    // Show confetti celebration
    showConfetti();
    
    setTimeout(() => {
        let message;
        if (isTwoPlayerMode) {
            if (playerOneScore > playerTwoScore) {
                message = `Player 1 wins with ${playerOneScore} pairs!`;
            } else if (playerTwoScore > playerOneScore) {
                message = `Player 2 wins with ${playerTwoScore} pairs!`;
            } else {
                message = `It's a tie! Both players found ${playerOneScore} pairs.`;
            }
        } else {
            message = `Congratulations! You completed the game in ${moves} moves and ${timer} seconds!`;
        }
        
        // Display animated winner message
        displayWinnerMessage(message);
    }, 500);
}

// Restart the game
function restartGame() {
    // Clear the board
    gameBoard.innerHTML = '';
    
    // Reset variables
    cards = [];
    flippedCards = [];
    moves = 0;
    matchedPairs = 0;
    timer = 0;
    gameStarted = false;
    playerOneScore = 0;
    playerTwoScore = 0;
    
    // Reset display
    movesCount.textContent = '0';
    timerElement.textContent = '0';
    scoreOne.textContent = '0';
    scoreTwo.textContent = '0';
    
    // Remove winner message if it exists
    const winnerText = document.querySelector('.winner-text');
    if (winnerText) {
        winnerText.remove();
    }
    
    if (isTwoPlayerMode) {
        setCurrentPlayer(1);
    }
    
    // Clear timer
    clearInterval(timerInterval);
    
    // Create new board
    createBoard();
}

// Go back to mode selection
backButton.addEventListener('click', () => {
    clearInterval(timerInterval);
    gameArea.classList.add('hidden');
    modeSelection.classList.remove('hidden');
});

// Event listeners for buttons
restartButton.addEventListener('click', restartGame);
soundButton.addEventListener('click', toggleSounds);