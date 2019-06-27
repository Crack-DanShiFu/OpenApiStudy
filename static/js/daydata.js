$(document).ready(function () {
    let qualitys = {
        '优': [0, '#37FF2F'],
        '良': [0, '#FFF20E'],
        '轻度污染': [0, '#FF9412'],
        '中度污染': [0, '#FF500A'],
        '重度污染': [0, '#FF16B5'],
        '严重污染': [0, '#48004E']
    }
    var city = $('caption span:first').text()
    var month = $('caption span:last').text()

    var chart = {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,

    };
    var title = {
        text: ''
    };
    var tooltip = {
        pointFormat: '{series.name}:<b>{point.percentage:.1f}%</b>'
    };
    var plotOptions = {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: false
            },
            showInLegend: false
        }
    };
    var series = [{
        type: 'pie',
        name: '',
    }];
    $.ajax({
        url: '/api/get_day_data/?city=' + city + '&month=' + month,
        type: 'GET',
        success: function (data) {
            var data_obj = JSON.parse(data)
            for (let d in data_obj) {
                qualitys[data_obj[d]['quality']][0] += 1
            }
            var chart_data = []
            for (let q in qualitys) {
                chart_data.push({
                    name: q,
                    y: qualitys[q][0],
                    color: qualitys[q][1],
                })
            }

            series[0].data = chart_data
            var json = {};
            json.chart = chart;
            json.title = title;
            json.tooltip = tooltip;
            json.series = series;
            json.plotOptions = plotOptions;
            json.credits = {
                enabled: false
            }
            $('#container').highcharts(json);

        }
    })

})

var creat_excel = function (city, month, jsonData) {
    let str = '地区,日期,AQI,PM2.5,PM10,SO2,CO,NO2,O3,rank,空气质量\n';
    let strKey = ['cityName', 'time_point', 'aqi', 'pm2_5', 'pm10', 'so2', 'co', 'no2', 'o3', 'rank', 'quality'];
    //增加\t为了不让表格显示科学计数法或者其他格式
    for (let i = 0; i < jsonData.length; i++) {
        for (let k = 0; k < strKey.length; k++) {
            str += `${jsonData[i][strKey[k]] + '\t'},`;
        }
        str += '\n';
    }
    //encodeURIComponent解决中文乱码
    let uri = 'data:text/csv;charset=utf-8,\ufeff' + encodeURIComponent(str);
    //通过创建a标签实现
    let link = document.createElement("a");
    link.href = uri;
    //对下载的文件命名
    link.download = city + month + "空气质量日数据.csv";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}


var downloadDayDate = function () {
    var city = $('caption span:first').text()
    var month = $('caption span:last').text()
    $.ajax({
        url: '/api/get_day_data/?city=' + city + '&month=' + month,
        type: 'GET',
        success: function (data) {
            var data_obj = JSON.parse(data)
            creat_excel(city, month, data_obj)
        }
    })

}