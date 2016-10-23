var da = JSON.parse(sessionStorage.bt);
da = da['emo']
da = JSON.parse(da);
console.log(da);
var config = {
  type: 'doughnut',
  data: {
    datasets: [{
      data: da,
      backgroundColor: [
        "#EEEEEE",
        "#000E77",
        "#773344",
        "#E3B5A4",
        "#0B0014",
      ],
      label: 'Dataset 1'
    }],
  labels: [
            "Anger",
            "Disgust",
            "Fear",
            "Joy",
            "Sadness"
          ]
},
options: {
      responsive: true,
      legend: {
                position: 'top',
              },
      title: {
                display: true,
                text: 'Chart.js Doughnut Chart'
              },
      animation: {
                animateScale: true,
                animateRotate: true
              }
    }
};
var ctx = document.getElementById("chart-area").getContext("2d");
window.myDoughnut = new Chart(ctx, config);
