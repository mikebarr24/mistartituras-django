window.addEventListener("DOMContentLoaded", () => {
  const addButton = document.querySelector(".piece-add-student");
  const addForm = document.querySelector(".add-form");
  const submitButton = document.querySelector(".student-submit");
  const selectOption = document.querySelector(".student-select");
  const removeButon = document.querySelector(".remove-part");

  if (removeButon) {
    removeButon.addEventListener("click", () => {
      const queryString = window.location.href.split("/").pop();
      fetch("/api", {
        method: "PUT",
        body: JSON.stringify({
          type: "remove",
          part: queryString,
        }),
      });
      removeButon.remove();
    });
  }

  if (addButton) {
    addButton.addEventListener("click", () => {
      addForm.classList.toggle("active");
    });
  }
  if (submitButton) {
    submitButton.addEventListener("click", () => {
      const studentId = selectOption.options[selectOption.selectedIndex].value;
      const queryString = window.location.href.split("/").pop();
      fetch("/api", {
        method: "PUT",
        body: JSON.stringify({
          type: "add",
          studentId: studentId,
          part: queryString,
        }),
      });
    });
  }
});
