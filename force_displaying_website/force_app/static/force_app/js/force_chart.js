document.addEventListener('DOMContentLoaded', function() {
    let forceChart = new forceChartClass('force-chart', 5, 10);

    /* Connect to WebSocket */
    let domain = window.location.host;
    domain = domain.replace('\/+$', '');    // Remove all slashes from end
    forceChartSocket = new WebSocket(
        `ws://${domain}/ws/force_chart/`
    );

    /* Message received from WebSocket */
    forceChartSocket.onmessage = function(e) {
        let data = JSON.parse(e.data);
        forceChart.update(data['force'])
    }
});

class forceChartClass {
    constructor(canvasId, timeInterval, samplingRate) {
        this.chart = this._createForceChart(canvasId, timeInterval, samplingRate);
    }

    update(value) {
        this.chart.data.datasets[0].data.shift();       // Drop old value from end (left)
        this.chart.data.datasets[0].data.push(value);   // Push new value to front (right)
        this.chart.update();                            // Render updates
    }

    _createForceChart(canvasId, timeInterval, samplingRate) {
        let ctx = document.getElementById(canvasId);
        let chart = new Chart(ctx, {
            type: 'line',

            data: {
                labels: this._linspace(-timeInterval, 0, timeInterval * samplingRate + 1),
                datasets: [{
                    label: 'Force (Newtons)',
                    borderColor: 'rgb(0,123,255)',
                    pointRadius: 0,
                    fill: false,
                    data: new Array(timeInterval * samplingRate + 1).fill(0),
                }],
            },

            options: {
                scales: {
                    xAxes: [{
                        ticks: {
                            /* Skip some x-axis labels */
                            callback: function(value, index, values) {
                                return (index % 10) ? '' : `${value} s`;
                            },
                            maxRotation: 0,
                            minRotation: 0,
                        },
                    }],
                    yAxes: [{
                        ticks: {
                            /* Skip some x-axis labels */
                            callback: function(value, index, values) {
                                return `${value} N`;
                            },
                            suggestedMin: 0,
                            suggestedMax: 100,
                        },
                    }],
                },
                tooltips: {
                    enabled: false,
                },
                animation: {
                    duration: 300,
                    easing: 'linear',
                },
            },
        });

        return chart;
    }

    _linspace(start, stop, sampleCount) {
        if(typeof sampleCount === 'undefined') {
            sampleCount = Math.max(Math.round(stop - start) + 1, 1);
        }
        if(sampleCount < 2) {
            return sampleCount === 1 ? [start]:[];
        }
        sampleCount--;
        let samples = Array(sampleCount);
        for(let i = sampleCount; i >= 0; i--) {
            samples[i] = (i * stop + (sampleCount - i) * start) / sampleCount;
        }
        return samples;
    }
}
