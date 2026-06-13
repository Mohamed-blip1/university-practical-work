let rate = {
    Dollar: 1,
    Dirham: 9.22,
    Yen: 159.18,
    Euro: 0.86,
};

function convert() {
    let startCurrency = document.getElementById("startCurrency");
    let desCurrency = document.getElementById("desCurrency");
    let result = document.getElementById("result");
    let amount = document.getElementById("amount");

    if (amount.value == "") {
        alert("Error: Please enter a valid number.");
        return false;
    }

    amount = amount.value;

    let toDollar = amount / rate[startCurrency.value];

    result.value = toDollar * rate[desCurrency.value];
}
