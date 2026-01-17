document.querySelectorAll("input, select").forEach((el) => {
  el.addEventListener("focus", () => {
    el.style.borderColor = "#38bdf8";
  });
});
