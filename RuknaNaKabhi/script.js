const startBtn = document.getElementById("startBtn");
const player = document.getElementById("player");
const obstacle = document.getElementById("obstacle");
const result = document.getElementById("result");
const entryBox = document.getElementById("entry-question");
const feedback = document.getElementById("entry-feedback");
const options = document.querySelectorAll(".entry-option");

let gameStarted = false;
let isJumping = false;
let grounded = true;
let entryAnswered = false;
let controlsAdded = false; // ✅ Avoid adding keydown more than once

// ✅ Start button logic
startBtn.addEventListener("click", () => {
  startBtn.style.display = "none";

  if (!entryAnswered) {
    entryBox.style.display = "block";
  } else {
    startGame();
  }
});

// ✅ Entry question
options.forEach((btn) => {
  btn.addEventListener("click", () => {
    if (entryAnswered) return;

    const correct = btn.getAttribute("data-answer") === "true";

    if (correct) {
      entryBox.style.display = "none";
      entryAnswered = true;

      // Disable further button input
      options.forEach((b) => (b.disabled = true));

      startGame();
    } else {
      feedback.textContent = "❌ गलत उत्तर! फिर से सोचो।";
    }
  });
});

// ✅ Start game
function startGame() {
  gameStarted = true;
  result.textContent = "";
  obstacle.style.animation = "moveObstacle 3s linear infinite";

  // ✅ Add controls ONCE
  if (!controlsAdded) {
    controlsAdded = true;

    document.addEventListener("keydown", (e) => {
      if (!gameStarted) return;

      const left = parseInt(window.getComputedStyle(player).getPropertyValue("left"));
      const bottom = parseInt(window.getComputedStyle(player).getPropertyValue("bottom"));

      if (e.key === "ArrowRight" && left < window.innerWidth - 60) {
        player.style.left = left + 20 + "px";
      } else if (e.key === "ArrowLeft" && left > 0) {
        player.style.left = left - 20 + "px";
      } else if (e.key === "ArrowUp" && grounded) {
        isJumping = true;
        grounded = false;

        player.style.bottom = bottom + 80 + "px";

        setTimeout(() => {
          player.style.bottom = bottom + "px";
          isJumping = false;
          grounded = true;
        }, 500);
      }
    });
  }

  // ✅ Collision check
  const collisionInterval = setInterval(() => {
    if (!gameStarted) {
      clearInterval(collisionInterval);
      return;
    }

    const playerLeft = parseInt(window.getComputedStyle(player).getPropertyValue("left"));
    const playerBottom = parseInt(window.getComputedStyle(player).getPropertyValue("bottom"));
    const obstacleRight = parseInt(window.getComputedStyle(obstacle).getPropertyValue("right"));
    const obstacleLeft = window.innerWidth - obstacleRight - 50;

    const overlapHorizontally = playerLeft + 40 > obstacleLeft && playerLeft < obstacleLeft + 50;
    const overlapVertically = playerBottom < 130;

    if (overlapHorizontally && overlapVertically) {
      result.textContent = "😵 ओह! तुम टकरा गए!";
      obstacle.style.animation = "none";
      gameStarted = false;
    }
  }, 100);
}
