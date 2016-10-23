var all = JSON.parse(sessionStorage.bt);
console.log(all);
var da = all['emo'];
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

window.onload = function() {
  var ctx = document.getElementById("chart-area").getContext("2d");
  window.myDoughnut = new Chart(ctx, config);

  var text = "";

  if (da[3] > .5) {
    text = "Your doing a great job being positive! Your best tweet was: \"" + all['mm']['max']['text'] + "\" with a positivity score of " + all['mm']['max']['v'];
  } else {
    text = "Try to be more considerate of other in your tweets, try to do more like this one: \"" + all['mm']['max']['text'] + "\" it has a positivity score of " + all['mm']['max']['v'];
  }

  console.log(text);
    
  $("#analysis").html(text);
};
