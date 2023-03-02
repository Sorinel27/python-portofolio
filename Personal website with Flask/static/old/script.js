"use strict";
const presentYear = new Date();
var footer_text = "&copy; Fratean Sorin, Cluj-Napoca, Romania - ";
footer_text += presentYear.getUTCFullYear();
document.getElementById("copy_p").innerHTML = footer_text;

// var screenWidth = (window.innerWidth > 0) ? window.innerWidth : screen.width;

// var img1 = document.getElementById('top-cloud');
// var img1_width = img1.width;
// var pos1 = img1_width;

// var img2 = document.getElementById('bottom-cloud');
// var img2_width = img2.clientWidth;
// var pos2 = img2_width;
// function moveClouds(){
//     var step = 1;
//     var speedCloud1 = img1.offsetLeft;
//     console.log(img1.offsetLeft)
//     if(img1_width >= speedCloud1){
//         speedCloud1 += step;
//         img1.style.left = speedCloud1 + "px";
//     }
//     else{
//         speedCloud1 -= step;
//         img1.style.left = speedCloud1 + "px";
//     }

// }
// function stopClouds(){
//     img1.style.right = pos1 + "px";
//     img2.style.left = pos2 + "px";
// }
// function timer(){
//     moveClouds();
//     my_time=setTimeout('timer()',10000);
// }


// document.getElementById("first_h1").addEventListener("mouseover", moveClouds);
// document.getElementById("top-container").addEventListener("mouseout", stopClouds);