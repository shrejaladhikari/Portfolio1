document.addEventListener("DOMContentLoaded", function () {
  var typed = new Typed("#typed-output", {
    strings: ["Hi There, I'm Shrejal Adhikari."],
    typeSpeed: 50, // Typing speed
    backSpeed: 30, // Backspacing speed
    loop: true, // Do not loop
    showCursor: true, // Show blinking cursor
    cursorChar: "|", // Cursor character
  });
});

// script.js
document.addEventListener("DOMContentLoaded", function () {
  const navLinks = document.querySelectorAll(".nav-link");

  // Get the current page path
  const currentPage = window.location.pathname;

  // Add 'active' class to the current page link
  navLinks.forEach((link) => {
    if (link.getAttribute("href") === currentPage) {
      link.classList.add("active");
    } else {
      link.classList.remove("active");
    }
  });
});
