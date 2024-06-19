// Game constants
const WIDTH = 400;
const HEIGHT = 600;
const WHITE = '#ffffff';
const BLACK = '#000000';
const GOLD = '#ffd700';

// Initialize canvas and context
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

// Load coin image
const coinImg = new Image();
coinImg.src = 'coin.png'; // Update with your coin image path

// Initialize game variables
let score = 0;
let coinRect = { x: WIDTH / 2 - 50, y: HEIGHT / 2 - 50, width: 100, height: 100 };

// Function to draw text on canvas
function drawText(text, x, y, color, font = '36px Arial') {
    ctx.fillStyle = color;
    ctx.font = font;
    ctx.fillText(text, x, y);
}

// Function to handle mouse click
function handleClick(event) {
    const rect = canvas.getBoundingClientRect();
    const mouseX = event.clientX - rect.left;
    const mouseY = event.clientY - rect.top;

    // Check if click is inside the coin area
    if (mouseX >= coinRect.x && mouseX <= coinRect.x + coinRect.width &&
        mouseY >= coinRect.y && mouseY <= coinRect.y + coinRect.height) {
        score++;
    }
}

// Add event listener for mouse click
canvas.addEventListener('click', handleClick);

// Game loop function
function gameLoop() {
    // Clear canvas
    ctx.clearRect(0, 0, WIDTH, HEIGHT);

    // Draw coin image
    ctx.drawImage(coinImg, coinRect.x, coinRect.y, coinRect.width, coinRect.height);

    // Draw score and rank
    drawText(`Score: ${score}`, WIDTH / 2 - 50, 50, BLACK);
    drawText(`Rank: ${getRank(score)}`, WIDTH / 2 - 50, 100, GOLD);

    // Request next frame
    requestAnimationFrame(gameLoop);
}

// Start the game loop
gameLoop();

// Function to determine rank based on score
function getRank(score) {
    const RANKS = [
        { name: 'Bronze', threshold: 0 },
        { name: 'Silver', threshold: 45 },
        { name: 'Platinum', threshold: 65 },
        { name: 'Diamond', threshold: 100 }
    ];

    for (let i = RANKS.length - 1; i >= 0; i--) {
        if (score >= RANKS[i].threshold) {
            return RANKS[i].name;
        }
    }

    return 'Bronze';
}
