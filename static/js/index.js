$(document).ready(function () {
    let aqi_data = ''
    let adcode = []
    $.ajax({
        url: '/api/get_lately_aqi/',
        type: 'GET',
        success: function (data) {
            aqi_data = data
            data_obj = JSON.parse(data)
            for (let i in data_obj) {
                adcode.push(i)
            }
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
                zooms: [4, 10],
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
                resizeEnable: true
            })
            map.setZoomAndCenter(4, [106, 38]);
            map.addControl(new AMap.Scale());
            map.addControl(new AMap.ToolBar({liteStyle: true}));
        },
    })

})
