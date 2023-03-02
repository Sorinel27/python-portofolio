var particlesQuantity = 2100;


var positionX = new Array(particlesQuantity);
var positionY = new Array(particlesQuantity);
var velocityX = new Array(particlesQuantity).fill(0);
var velocityY = new Array(particlesQuantity).fill(0);

function setup() {
    var container = document.getElementById("top-container");
    var height_of_a_div = container.offsetHeight;
    var width_of_a_div = container.offsetWidth;  
    let c = createCanvas(width_of_a_div, height_of_a_div);
    c.position(0, 0);

    for (var particle = 1; particle < particlesQuantity; particle++) {
        stroke(random(150, 255), random(150, 255), random(150, 255));
        strokeWeight(3);
        positionX[particle] = random(0, width);
        positionY[particle] = random(0, height);
    }

    positionX[0] = 0;
    positionY[0] = 0;
}

function draw() {
    //   background(255, 255, 255);
    clear(color(255, 255, 255, 0));
    velocityX[0] = velocityX[0] * 0.5 + (mouseX - positionX[0]) * 0.1;
    velocityY[0] = velocityY[0] * 0.5 + (mouseY - positionY[0]) * 0.1;

    positionX[0] += velocityX[0];
    positionY[0] += velocityY[0];

    for (var particle = 1; particle < particlesQuantity; particle++) {
        var whatever = 1024 / (sq(positionX[0] - positionX[particle]) + sq(positionY[0] - positionY[particle]));

        velocityX[particle] = velocityX[particle] * 0.95 + (velocityX[0] - velocityX[particle]) * whatever;
        velocityY[particle] = velocityY[particle] * 0.95 + (velocityY[0] - velocityY[particle]) * whatever;

        positionX[particle] += velocityX[particle];
        positionY[particle] += velocityY[particle];

        if ((positionX[particle] < 0 && velocityX[particle] < 0) || (positionX[particle] > width && velocityX[particle] > 0)) {
            velocityX[particle] = -velocityX[particle];
        }

        if ((positionY[particle] < 0 && velocityY[particle] < 0) || (positionY[particle] > height && velocityY[particle] > 0)) {
            velocityY[particle] = -velocityY[particle];
        }

        point(positionX[particle], positionY[particle]);
    }

}
function mousePressed() {
    for (var particle = 1; particle < particlesQuantity; particle++) {
        positionX[particle] = random(0, width);
        positionY[particle] = random(0, height);
    }
}
function windowResized() {
    var container = document.getElementById("top-container");
    var height_of_a_div = container.offsetHeight;
    var width_of_a_div = container.offsetWidth;  
    resizeCanvas(width_of_a_div, height_of_a_div);  // resize the canvas to fit the new window size
}