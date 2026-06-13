let products = [
    {
        name: "computer",
        price: 899.99,
    },
    {
        name: "mouse",
        price: 25.0,
    },
    {
        name: "keyboard",
        price: 45.0,
    },
];

function printProducts() {
    document.write("<h3>Products list</h3>");
    for (let i = 0; i < products.length; i++) {
        document.write(`<p>${products[i].name} : ${products[i].price}$</p>`);
    }
}

function addProduct(pName, pPrice) {
    if (pName in products) {
        alert("Error: Product already exist.");
    }
    products.push({ name: pName, price: pPrice });
}

function calculateTotalPrice() {
    let sum = 0;

    for (let i = 0; i < products.length; i++) {
        sum += products[i].price;
    }

    document.write(`<p>Prix total: ${sum}$</p>`);

    return sum;
}

function searchProduct() {
    let name = prompt("Enter product name:");

    let exist = false;

    for (let i = 0; i < products.length; i++) {
        if (products[i].name === name) {
            alert(`${products[i].name} : ${products[i].price}$`);

            exist = true;
            break;
        }
    }

    if (!exist) {
        alert("Product not found!");
    }
}

function printExpensive() {
    document.write("<h3>Products > 30$</h3>");

    for (let i = 0; i < products.length; i++) {
        if (products[i].price > 30) {
            document.write(`<p>${products[i].name} : ${products[i].price}</p>`);
        }
    }
}

// test:

let choice = Number(
    prompt(
        "Enter a choice:\n" +
            "1. Display products.\n" +
            "2. Add product.\n" +
            "3. Search product\n" +
            "4. Display total price\n" +
            "5. Display expensive products\n",
    ),
);

switch (choice) {
    case 1:
        printProducts();
        break;
    case 2:
        let pName = prompt("Enter product name:");
        let pPrice = Number(prompt("Enter product price:"));

        addProduct(pName, pPrice);
        printProducts();
        break;
    case 3:
        searchProduct();
        break;
    case 4:
        calculateTotalPrice();
        break;
    case 5:
        printExpensive();
        break;
}
