window.addEventListener("DOMContentLoaded", () => {
  const addButton = document.querySelector(".piece-add-student");
  const addForm = document.querySelector(".add-form");
  const submitButton = document.querySelector(".student-submit");
  const selectOption = document.querySelector(".student-select");

  addButton.addEventListener("click", () => {
    addForm.classList.toggle("active");
  });

  submitButton.addEventListener("click", () => {
    const studentId = selectOption.options[selectOption.selectedIndex].value;
    const queryString = window.location.href.split("/").pop();
    fetch("/api", {
      method: "PUT",
      body: JSON.stringify({
        studentId: studentId,
        part: queryString,
      }),
    });
  });
});
