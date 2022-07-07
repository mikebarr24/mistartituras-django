document.addEventListener("DOMContentLoaded", (e) => {
  const burgerButton = document.querySelector(".burger-button");
  const navList = document.querySelector(".nav-list");
  burgerButton.addEventListener("click", () => {
    navList.classList.toggle("open");
  });
});
