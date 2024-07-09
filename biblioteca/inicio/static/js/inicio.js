// Creación de gráfica de pastel
// Se obtienen los estados registrados
let states = $('#chartPie').data('states')
Highcharts.chart('container', {
    chart: {
        type: 'pie'
    },
    title: {
        text: 'Cantidad por estado del libro',
        align: 'left'
    },
    accessibility: {
        announceNewData: {
            enabled: true
        },
    },

    plotOptions: {
        series: {
            borderRadius: 5,
            dataLabels: [{
                enabled: true,
                distance: 15,
                format: '{point.name}'
            }, {
                enabled: true,
                distance: '-30%',
                filter: {
                    property: 'percentage',
                    operator: '>',
                    value: 5
                },
                format: '{point.y:.0f}',
                style: {
                    fontSize: '0.9em',
                    textOutline: 'none'
                }
            }]
        }
    },

    tooltip: {
        headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
        pointFormat: '<span style="color:{point.color}">{point.name}</span>: ' +
            '<b>{point.y:.0f}</b> libro(s)<br/>'
    },

    series: [
        {
            name: 'Estatus',
            colorByPoint: true,
            data: [
                {
                    name: 'Excelente',
                    y: states[0],
                    drilldown: 'Excelente',
                    color: '#2ed255'
                },
                {
                    name: 'Bueno',
                    y: states[1],
                    drilldown: 'Bueno',
                    color: '#d26812'
                },
                {
                    name: 'Regular',
                    y: states[2],
                    drilldown: 'Regular',
                    color: '#ede057'
                },
                {
                    name: 'Malo',
                    y: states[3],
                    drilldown: 'Malo',
                    color: '#ff0000'
                }
            ]
        }
    ]
});

// Creación de gráfica de barras
let libros = $('#chartColum').data('libros')
let discos = $('#chartColum').data('discos')
Highcharts.chart('container_colum', {
    chart: {
        type: 'column'
    },
    title: {
        align: 'left',
        text: 'Gráfica de comparación'
    },
    subtitle: {
        align: 'left',
        text: 'Se muestra la cantidad de libros con respecto a la cantidad de discos registrados'
    },
    accessibility: {
        announceNewData: {
            enabled: true
        }
    },
    xAxis: {
        type: 'category'
    },
    yAxis: {
        title: {
            text: 'Total de elementos'
        }

    },
    legend: {
        enabled: false
    },
    plotOptions: {
        series: {
            borderWidth: 0,
            dataLabels: {
                enabled: true,
                format: '{point.y:.0f}'
            }
        }
    },

    tooltip: {
        headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
        pointFormat: '<span style="color:{point.color}">{point.name}</span>: ' +
            '<b>{point.y:.0f}</b> en total<br/>'
    },

    series: [
        {
            data: [
                {
                    name: 'libros',
                    y: libros,
                    drilldown: 'Libros',
                    color: 'red'
                },
                {
                    name: 'Discos',
                    y: discos,
                    drilldown: 'Discos',
                    color: '#007bff'
                }
            ]
        }
    ]
});
