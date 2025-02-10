document.addEventListener("DOMContentLoaded", () => {
    const hamburger = document.getElementById("hamburger");
    const menu = document.getElementById("nav-links");

    function toggleMenu() {
        menu.classList.toggle("active");
        menu.classList.toggle("hidden");
        hamburger.classList.toggle("open");
    }

    hamburger.addEventListener("click", toggleMenu);
});
