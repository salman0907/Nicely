Chart.defaults.global.legend.display = false;
var all = JSON.parse(sessionStorage.bt);
console.log(all);
var da = all['emo'];
var config = {
  type: 'doughnut',
  data: {
    datasets: [{
      data: da,
      backgroundColor: [
        "#FFB2CF",
        "#FFC7B2",
        "#C7B2FF",
        "#FFEEB2",
        "#B2EAFF",
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
      //legend: {
                //position: 'top',
              //},
      title: {
                display: false,
                text: 'Tweet Emotions'
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
    text = "Your doing a great job being positive! <br>Continue to tweet like this: " 
  } else {
    text = "Try to be more considerate of others in your tweets, <br>try to tweet like this: ";
  }

  console.log(text);
    
  $("#analysis").html(text);
  $("#turl").attr("href", all['mm']['max']['url'])
};
