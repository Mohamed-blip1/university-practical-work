const display = document.getElementById("display");

let first = "";
let operator = "";
let second = "";

function addToDisplay(input) {
    if (["+", "-", "*", "/"].includes(input)) {
        if (first !== "") {
            operator = input;
        }
    } else if (operator === "") {
        if (input === ".") {
            if (first.includes(".")) return;
            if (first === "") first = "0";
        }
        first += input;
    } else {
        if (input === ".") {
            if (second.includes(".")) return;
            if (first === "") first = "0";
        }
        second += input;
    }

    display.value = first + operator + second;
}

function clearDisplay() {
    display.value = "";
    first = "";
    operator = "";
    second = "";
}

function calculate() {
    if (first === "" || second === "" || operator === "") {
        return;
    }

    let result = 0;

    const num1 = Number(first);
    const num2 = Number(second);

    switch (operator) {
        case "+":
            result = num1 + num2;
            break;
        case "-":
            result = num1 - num2;
            break;
        case "*":
            result = num1 * num2;
            break;
        case "/":
            if (num2 == 0) {
                alert("Error: can't divide by 0.");
                clearDisplay();
                return;
            }
            result = num1 / num2;
            break;
    }

    first = String(result);
    second = "";

    display.value = first;
}
