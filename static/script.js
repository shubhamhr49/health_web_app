document.getElementById("toggleButton").addEventListener("click", function () {
  const sidebar = document.getElementById("sidebar");
  if (sidebar.style.width === "0px" || sidebar.style.width === "") {
    sidebar.style.width = "250px";
    const textElements = document.querySelectorAll("#sidebar .text");
    textElements.forEach((el) => (el.style.display = "inline"));
  } else {
    sidebar.style.width = "0px";
    const textElements = document.querySelectorAll("#sidebar .text");
    textElements.forEach((el) => (el.style.display = "none"));
  }
});

function formHandler(id) {
  const heart_container = document.getElementById("heart-container");
  const diabetes_container = document.getElementById("diabetes-container");

  if (id === "heart") {
    heart_container.style.display = "block";
    diabetes_container.style.display = "none";
  }

  if (id === "diabetes") {
    heart_container.style.display = "none";
    diabetes_container.style.display = "block";
  }
}
