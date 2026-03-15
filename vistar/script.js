const balls = document.querySelectorAll('.ball');

document.addEventListener('mousemove', (e) => {
    const mouseX = e.clientX;
    const mouseY = e.clientY;

    // माउस के हिसाब से गोलों को धीरे से हिलाना
    balls.forEach((ball, index) => {
        const speed = (index + 1) * 20;
        const x = (window.innerWidth / 2 - mouseX) / speed;
        const y = (window.innerHeight / 2 - mouseY) / speed;

        ball.style.transform = `translate(${x}px, ${y}px)`;
    });
});
const symbols = ['✕', '○', '☐', '△'];
const container = document.getElementById('ps5-container');

function createSymbol() {
    if (!container) return;

    const span = document.createElement('span');
    span.classList.add('ps-symbol');
    
    // सिम्बल और लोकेशन
    span.innerText = symbols[Math.floor(Math.random() * symbols.length)];
    span.style.left = Math.random() * 100 + "vw";
    
    // साइज (20px से 40px)
    const size = Math.random() * 20 + 20;
    span.style.fontSize = size + "px";

    // गिरने की रफ़्तार (8 से 12 सेकंड - बहुत ही धीरे)
    const duration = Math.random() * 4 + 8;
    span.style.animationDuration = duration + "s";

    container.appendChild(span);

    // एनीमेशन खत्म होने पर हटाना
    setTimeout(() => {
        span.remove();
    }, duration * 1000);
}

// हर 700ms में एक नया सिम्बल
setInterval(createSymbol, 700);
