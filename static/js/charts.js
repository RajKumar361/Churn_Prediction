const ctx = document.getElementById("riskChart");

new Chart(ctx, {
  type: "doughnut",
  data: {
    labels: ["High", "Medium", "Low"],
    datasets: [
      {
        data: [30, 40, 30],
      },
    ],
  },
});
