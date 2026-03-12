const button = document.querySelector("button")
const p = document.querySelector("p");

button.addEventListener("click", function () {
    p.textContent = "¡Día fantástico para Elio! (Ref: ESDD)";
    p.style.color = "orange";
});

button.addEventListener("mouseover", function () {
    button.textContent = "¡Púlsame, Delgado!";
});

// extra
button.addEventListener("mouseleave", function() {
    button.textContent = "Cambiar ánimo";
})