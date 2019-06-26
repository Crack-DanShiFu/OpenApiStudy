$(document).ready(function () {

    var colors = {};
    var getColorByAdcode = function (adcode) {
        if (!colors[adcode]) {
            var gb = Math.random() * 155 + 50;
            colors[adcode] = 'rgb(' + gb + ',' + gb + ',255)';
        }
        return colors[adcode];
    };


    var disProvince = new AMap.DistrictLayer.Province({
        zIndex: 12,
        adcode: ['130000','140000','150000','160000','170000','180000'],
        depth: 1,
        styles: {
            'fill': function (properties) {
                var adcode = properties.adcode;
                return getColorByAdcode(adcode);
            },
            'province-stroke': 'cornflowerblue',
            'city-stroke': 'white',//中国地级市边界
            'county-stroke': 'rgba(255,255,255,0.5)'//中国区县边界
        }
    })


    var map = new AMap.Map("indexmap", {
        zooms: [3, 10],
        showIndoorMap: false,
        zoom: 4,
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
    map.addControl(new AMap.Scale());
    map.addControl(new AMap.ToolBar({liteStyle: true}));


})
