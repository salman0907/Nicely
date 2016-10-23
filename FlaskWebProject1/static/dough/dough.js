var randomScalingFactor = 5;
var randomColorFactor = 100;
var randomColor = function(opacity) {
	return 'rgba(' + randomColorFactor() + ',' + randomColorFactor() + ',' + randomColorFactor() + ',' + (opacity || '.3') + ')';
};

var config = {
	type: 'doughnut',
	data: {
		datasets: [{
			data: [
				randomScalingFactor,
				randomScalingFactor,
				randomScalingFactor,
				randomScalingFactor,
				randomScalingFactor,
			],
			backgroundColor: [
				"#EEEEEE",
				"#000E77",
				"#773344",
				"#E3B5A4",
				"#0B0014",
			],
			label: 'Dataset 1'
		}, {
			hidden: true,
			data: [
				randomScalingFactor,
				randomScalingFactor,
				randomScalingFactor,
				randomScalingFactor,
				randomScalingFactor,
			],
			backgroundColor: [
				"#9CBEE5",
				"#D29CD3",
				"#FF7F9B",
				"#EFE3A0",
				"#91FFCF",
			],
			label: 'Dataset 2'
		}, {
			data: [
				randomScalingFactor,
				randomScalingFactor,
				randomScalingFactor,
				randomScalingFactor,
				randomScalingFactor,
				],
			backgroundColor: [
									"#F7464A",
									"#46BFBD",
									"#FDB45C",
									"#949FB1",
									"#4D5360",
								],
			label: 'Dataset 3'
		}],
	labels: [
						"Red",
						"Green",
						"Yellow",
						"Grey",
						"Dark Grey"
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
};
//$('#randomizeData').click(function() {
//$.each(config.data.datasets, function(i, dataset) {
				//dataset.data = dataset.data.map(function() {
									//return randomScalingFactor();
								//});
				//dataset.backgroundColor = dataset.backgroundColor.map(function() {
									//return randomColor(0.7);
								//});
			//});
//window.myDoughnut.update();
//});
//$('#addDataset').click(function() {
//var newDataset = {
				//backgroundColor: [],
				//data: [],
				//label: 'New dataset ' + config.data.datasets.length,
			//};
//for (var index = 0; index < config.data.labels.length; ++index) {
				//newDataset.data.push(randomScalingFactor());
				//newDataset.backgroundColor.push(randomColor(0.7));
			//}
//config.data.datasets.push(newDataset);
//window.myDoughnut.update();
//});
//$('#addData').click(function() {
//if (config.data.datasets.length > 0) {
				//config.data.labels.push('data #' + config.data.labels.length);
				//$.each(config.data.datasets, function(index, dataset) {
									//dataset.data.push(randomScalingFactor());
									//dataset.backgroundColor.push(randomColor(0.7));
								//});
				//window.myDoughnut.update();
			//}
//});
//$('#removeDataset').click(function() {
//config.data.datasets.splice(0, 1);
//window.myDoughnut.update();
//});
//$('#removeData').click(function() {
//config.data.labels.splice(-1, 1); // remove the label first
//config.data.datasets.forEach(function(dataset, datasetIndex) {
				//dataset.data.pop();
				//dataset.backgroundColor.pop();
			//});
//window.myDoughnut.update();
//});
