let aqi_data = null
let adcode = []
url = window.location.href;
var provinces = url.split('provinces=')[1] + '0000'
let qualitys = {
    '优': [0, '#37FF2F'],
    '良': [0, '#FFF20E'],
    '轻度污染': [0, '#FF9412'],
    '中度污染': [0, '#FF500A'],
    '重度污染': [0, '#FF16B5'],
    '严重污染': [0, '#48004E']
}
var city = $('caption span').text()
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
        showInLegend: true
    }
};
var series = [{
    type: 'pie',
    name: '',
}];


var getColorByAdcode = function (adcode) {
    var aqi = parseInt(data_obj[adcode][1])
    if (aqi <= 50) {
        return 'rgb(55,255,47)';
    } else if (aqi <= 100) {
        return 'rgb(255,242,14)';
    } else if (aqi <= 150) {
        return 'rgb(255,148,18)';
    } else if (aqi <= 200) {
        return 'rgb(255,80,10)';
    } else {
        return 'rgb(255,22,181)';
    }
};


$.ajax({
    url: '/api/get_lately_aqi/?provinces=' + provinces,
    type: 'GET',
    success: function (data) {
        aqi_data = JSON.parse(data)
        data_obj = JSON.parse(data)
        for (let i in data_obj) {
            adcode.push(i)
        }

    },
})


$(document).ready(function () {
    var disProvince = new AMap.DistrictLayer.Province({
        zIndex: 12,
        adcode: adcode,
        depth: 1,

        styles: {
            'fill': function (properties) {
                var adcode = properties.adcode;
                return getColorByAdcode(adcode);
            },
            'province-stroke': 'cornflowerblue',
            'city-stroke': 'white',//中国地级市边界
            'county-stroke': 'rgba(255,255,255,0.1)'//中国区县边界
        }
    })


    var map = new AMap.Map("indexmap", {
        zooms: [5, 10],
        showIndoorMap: false,
        isHotspot: false,
        defaultCursor: 'pointer',
        touchZoomCenter: 1,
        pitch: 0,
        layers: [
            disProvince,
            new AMap.TileLayer()
        ],

        viewMode: '2D',
        resizeEnable: false
    })
    map.setCity(provinces)
    map.addControl(new AMap.Scale());
    map.addControl(new AMap.ToolBar({liteStyle: true}));

    var data_obj = aqi_data
    for (let d in data_obj) {
        var aqi = data_obj[d][1]
        if (aqi <= 50) {
            qualitys['优'][0] += 1
        } else if (aqi <= 100) {
            qualitys['良'][0] += 1
        } else if (aqi <= 150) {
            qualitys['轻度污染'][0] += 1
        } else if (aqi <= 200) {
            qualitys['中度污染'][0] += 1
        } else if (aqi <= 300) {
            qualitys['重度污染'][0] += 1
        } else {
            qualitys['严重污染'][0] += 1
        }
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
})

var downloadAllDayDate = function () {
    alert('请联系管理员')
}
