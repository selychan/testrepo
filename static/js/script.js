document.addEventListener("DOMContentLoaded", function() {
    const animal = document.querySelector(".animal");

    animal.addEventListener("click", function() {
        animal.classList.add("shake");
        setTimeout(function() {
            animal.classList.remove("shake");
        }, 500); 
    });
});
