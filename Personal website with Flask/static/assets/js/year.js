"use strict";
const presentYear = new Date();
var footer_text = "&copy; Fratean Sorin, Cluj-Napoca, Romania - ";
footer_text += presentYear.getUTCFullYear();
document.getElementById("copy_p").innerHTML = footer_text;
