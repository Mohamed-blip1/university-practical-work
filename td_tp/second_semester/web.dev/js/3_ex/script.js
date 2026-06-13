function validateForm() {
    const name = document.getElementById("name");
    const email = document.getElementById("email");
    const password = document.getElementById("password");
    const confirm = document.getElementById("confirm");

    if (name.value.length === 0) {
        alert("Error: Empty name.");
        return false;
    }

    if (!email.value.includes("@") || !email.value.includes(".")) {
        alert("Error: Invalid email.");
        return false;
    }

    if (password.value.length < 6) {
        alert("Error: Password should contain at least 6 caracters.");
        return false;
    }

    if (password.value !== confirm.value) {
        alert("Error: Invalid password confirmation.");
        return false;
    }
    alert("Inscription réussie 🎉");
    return true;
}
