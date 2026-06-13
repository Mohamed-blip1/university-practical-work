document.write("<table>");

const a = 0;
const b = 9;

let firstLine = true;
let first = true;

let colNumber = 0;

document.write("<tr>");
document.write("<td>*</td>");
for (let i = 0; i <= 9; i++) {
    document.write(`<td>${i}</td>`);
}
document.write("</tr>");

for (let i = 0; i <= 9; i++) {
    document.write("<tr>");

    document.write(`<td>${i}</td>`);

    for (let j = 0; j <= 9; j++) {
        document.write(`<td>${i * j}</td>`);
    }

    document.write("</tr>");
}

document.write("</table>");
