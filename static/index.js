document.addEventListener("DOMContentLoaded", () => {
    const hamburger = document.getElementById("hamburger");
    const menu = document.getElementById("nav-links");
    const alertCloseButtons = document.querySelectorAll(".close-alert");

    const toggleMenu = () => {
        menu.classList.toggle("active");
        menu.classList.toggle("hidden");
        hamburger.classList.toggle("open");
    };

    const alertCloseButtonHandler = function() {
        this.closest(".alert-box").remove();
    };

    hamburger.addEventListener("click", toggleMenu);
    alertCloseButtons.forEach(button => button.addEventListener("click", alertCloseButtonHandler));
});

