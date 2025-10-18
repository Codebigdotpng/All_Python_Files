const car = document.getElementById('car');
const gameContainer = document.getElementById('game-container');
const scoreElement = document.getElementById('score');

let carPosition = 185;
let score = 0;
let gameLoop;

function moveCar(e) {
    if (e.key === 'ArrowUp' && carPosition < 370) {
        carPosition += 10;
    } else if (e.key === 'ArrowDown' && carPosition > 0) {
        carPosition -= 10;
    }
    car.style.bottom = carPosition + 'px';
}

function createObstacle() {
    const obstacle = document.createElement('div');
    obstacle.classList.add('obstacle');
    obstacle.style.bottom = Math.floor(Math.random() * 370) + 'px';
    gameContainer.appendChild(obstacle);

    let position = 800;
    const moveObstacle = setInterval(() => {
        if (position < -30) {
            clearInterval(moveObstacle);
            gameContainer.removeChild(obstacle);
            score++;
            scoreElement.textContent = `Score: ${score}`;
        } else {
            position -= 5;
            obstacle.style.right = position + 'px';

            if (checkCollision(car, obstacle)) {
                clearInterval(moveObstacle);
                endGame();
            }
        }
    }, 20);
}

function checkCollision(car, obstacle) {
    const carRect = car.getBoundingClientRect();
    const obstacleRect = obstacle.getBoundingClientRect();

    return !(carRect.right < obstacleRect.left || 
             carRect.left > obstacleRect.right || 
             carRect.bottom < obstacleRect.top || 
             carRect.top > obstacleRect.bottom);
}

function endGame() {
    clearInterval(gameLoop);
    alert(`Game Over! Your score: ${score}`);
    location.reload();
}

document.addEventListener('keydown', moveCar);
gameLoop = setInterval(createObstacle, 2000);