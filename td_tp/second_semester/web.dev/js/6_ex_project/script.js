function updateClock() {
    let now = new Date();

    let dDate = document.getElementById("dDate");
    let dTime = document.getElementById("dTime");

    let hours = String(now.getHours()).padStart(2, "0");
    let minutes = String(now.getMinutes()).padStart(2, "0");
    let seconds = String(now.getSeconds()).padStart(2, "0");

    let day = String(now.getDate()).padStart(2, "0");
    let month = String(now.getMonth() + 1).padStart(2, "0");
    let year = now.getFullYear();

    let time = `${hours}:${minutes}:${seconds}`;
    let date = `${day}/${month}/${year}`;

    // console.log(now);

    dDate.textContent = date;
    dTime.textContent = time;
}

updateClock();
setInterval(updateClock, 1000);

function toggleLightMode() {
    let body = document.body;
    if (body) {
        body.classList.toggle("darck");
    }

    let button = document.getElementById("mode-button");
    if (button) {
        button.classList.toggle("darck");
        button.textContent =
            button.textContent === "Clair" ? "Sombre" : "Clair";
    }

    let defaultColorButton = document.getElementById("color-button-default");
    if (defaultColorButton) {
        defaultColorButton.classList.toggle("darck");
    }

    let clock = document.getElementById("clock");
    if (clock) clock.classList.toggle("darck");

    let adress = document.getElementById("uni-link");
    if (adress) adress.classList.toggle("darck");

    // let footerContent = document.getElementById("footer-content");
    // footerContent.color("#eee");

    let footerP = document.querySelector("footer p");
    if (footerP) footerP.classList.toggle("darck");

    let more = document.getElementById("more-button");
    let less = document.getElementById("less-button");
    if (more) {
        more.classList.toggle("more-less-light");
        more.classList.toggle("more-less-darck");
    }
    if (less) {
        less.classList.toggle("more-less-light");
        less.classList.toggle("more-less-darck");
    }
}

function toggleMoreLess() {
    let p = document.getElementById("masked-p");
    // console.log(p);
    if (p) p.classList.toggle("show");

    let more = document.getElementById("more-button");
    if (more) more.classList.toggle("mask");

    let less = document.getElementById("less-button");
    if (less) less.classList.toggle("show");
}

function toggleColor(colorType) {
    let body = document.querySelector("body");

    if (body) {
        body.style.color = colorType;
    }
}

function hoverBar() {
    let elements = document.querySelectorAll("#nav-bar ul li a");

    for (let i = 0; i < elements.length; i++) {
        elements[i].style.transition = "0.3s";
    }
    // console.log(elements);

    for (let i = 0; i < elements.length; i++) {
        elements[i].addEventListener("mouseenter", () => {
            elements[i].style.backgroundColor = "orange";
        });
        // console.log("Hello");
    }

    for (let i = 0; i < elements.length; i++) {
        elements[i].addEventListener("mouseleave", () => {
            elements[i].style.backgroundColor = "";
        });
    }
}

hoverBar();

let hobbies = [];

function getHobbies() {
    let hobbiesElements = document.querySelectorAll("#hobbies li");
    // console.log(hobbiesElements);

    for (let i = 0; i < 2; i++) {
        hobbies.push(hobbiesElements[i].textContent);
    }
}

getHobbies();
// console.log(hobbies);

function addHobbie() {
    let hobbieName = document.getElementById("newHobbie");
    let oList = document.getElementById("hobbies");
    let exist = false;

    if (hobbieName.value === "") return false;

    for (let i = 0; i < hobbies.length; i++) {
        if (hobbieName.value === hobbies[i]) {
            exist = true;
        }
    }

    if (exist) return false;

    let newListItem = document.createElement("li");
    newListItem.innerHTML = `<strong>${hobbieName.value}<strong>`;
    oList.appendChild(newListItem);

    hobbieName.value = "";
    addRemoveHobbiesEffect();
}

function addRemoveHobbiesEffect() {
    let oList = document.getElementById("hobbies");
    let lItems = document.querySelectorAll("#hobbies li");

    for (let i = 0; i < lItems.length; i++) {
        console.log(lItems[i]);
        lItems[i].style.cursor = "pointer";

        lItems[i].addEventListener("click", () => {
            oList.removeChild(lItems[i]);
        });
    }
}

addRemoveHobbiesEffect();

// let userName = String(prompt("Entre Vos Nom:"));

// alert(`Bienvenue ${userName}.`);
