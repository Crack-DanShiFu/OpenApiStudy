import time

import xlrd

city = ['阿坝州', '安康', '阿克苏地区', '阿里地区', '阿拉善盟', '阿勒泰地区', '安庆', '安顺', '鞍山', '克孜勒苏州', '安阳', '蚌埠', '白城', '保定', '北海', '宝鸡',
        '北京', '毕节', '博州', '白山', '百色', '保山', '白沙', '包头', '保亭', '本溪', '巴彦淖尔', '白银', '巴中', '滨州', '亳州', '长春', '昌都', '常德',
        '成都', '承德', '赤峰', '昌吉州', '五家渠', '昌江', '澄迈', '重庆', '长沙', '常熟', '楚雄州', '朝阳', '沧州', '长治', '常州', '潮州', '郴州', '池州',
        '崇左', '滁州', '定安', '丹东', '东方', '东莞', '德宏州', '大理州', '大连', '大庆', '大同', '定西', '大兴安岭地区', '德阳', '东营', '黔南州', '达州',
        '德州', '儋州', '鄂尔多斯', '恩施州', '鄂州', '防城港', '佛山', '抚顺', '阜新', '阜阳', '富阳', '抚州', '福州', '广安', '贵港', '桂林', '果洛州',
        '甘南州', '固原', '广元', '贵阳', '甘孜州', '赣州', '广州', '淮安', '海北州', '鹤壁', '淮北', '河池', '海东地区', '邯郸', '哈尔滨', '合肥', '鹤岗',
        '黄冈', '黑河', '红河州', '怀化', '呼和浩特', '海口', '呼伦贝尔', '葫芦岛', '哈密地区', '海门', '海南州', '淮南', '黄南州', '衡水', '黄山', '黄石',
        '和田地区', '海西州', '河源', '衡阳', '汉中', '杭州', '菏泽', '贺州', '湖州', '惠州', '吉安', '金昌', '晋城', '景德镇', '金华', '西双版纳州', '九江',
        '吉林', '即墨', '江门', '荆门', '佳木斯', '济南', '济宁', '胶南', '酒泉', '句容', '湘西州', '金坛', '鸡西', '嘉兴', '江阴', '揭阳', '济源', '嘉峪关',
        '胶州', '焦作', '锦州', '晋中', '荆州', '库尔勒', '开封', '黔东南州', '克拉玛依', '昆明', '喀什地区', '昆山', '临安', '六安', '来宾', '聊城', '临沧',
        '娄底', '乐东', '廊坊', '临汾', '临高', '漯河', '丽江', '吕梁', '陇南', '六盘水', '拉萨', '乐山', '丽水', '凉山州', '陵水', '莱芜', '莱西', '临夏州',
        '溧阳', '辽阳', '辽源', '临沂', '龙岩', '洛阳', '连云港', '莱州', '兰州', '林芝', '柳州', '泸州', '马鞍山', '牡丹江', '茂名', '眉山', '绵阳', '梅州',
        '宁波', '南昌', '南充', '宁德', '内江', '南京', '怒江州', '南宁', '南平', '那曲地区', '南通', '南阳', '平度', '平顶山', '普洱', '盘锦', '蓬莱', '平凉',
        '莆田', '萍乡', '濮阳', '攀枝花', '青岛', '琼海', '秦皇岛', '曲靖', '齐齐哈尔', '七台河', '黔西南州', '清远', '庆阳', '钦州', '衢州', '泉州', '琼中',
        '荣成', '日喀则', '乳山', '日照', '韶关', '寿光', '上海', '绥化', '石河子', '石家庄', '商洛', '三明', '三门峡', '山南', '遂宁', '四平', '商丘', '宿迁',
        '上饶', '汕头', '汕尾', '绍兴', '三亚', '邵阳', '沈阳', '十堰', '松原', '双鸭山', '深圳', '朔州', '宿州', '随州', '苏州', '石嘴山', '泰安', '塔城地区',
        '太仓', '铜川', '屯昌', '通化', '天津', '铁岭', '通辽', '铜陵', '吐鲁番地区', '铜仁地区', '唐山', '天水', '太原', '台州', '泰州', '文昌', '文登', '潍坊',
        '瓦房店', '威海', '乌海', '芜湖', '武汉', '吴江', '乌兰察布', '乌鲁木齐', '渭南', '万宁', '文山州', '武威', '无锡', '温州', '吴忠', '梧州', '五指山',
        '西安', '兴安盟', '许昌', '宣城', '襄阳', '孝感', '迪庆州', '锡林郭勒盟', '厦门', '西宁', '咸宁', '湘潭', '邢台', '新乡', '咸阳', '新余', '信阳', '忻州',
        '徐州', '雅安', '延安', '延边州', '宜宾', '盐城', '宜昌', '宜春', '银川', '运城', '伊春', '云浮', '阳江', '营口', '榆林', '玉林', '伊犁哈萨克州', '阳泉',
        '玉树州', '烟台', '鹰潭', '义乌', '宜兴', '玉溪', '益阳', '岳阳', '扬州', '永州', '淄博', '自贡', '珠海', '湛江', '镇江', '诸暨', '张家港', '张家界',
        '张家口', '周口', '驻马店', '章丘', '肇庆', '中山', '舟山', '昭通', '中卫', '张掖', '招远', '资阳', '遵义', '枣庄', '漳州', '郑州', '株洲']

file_path = r'1.xlsx'

data = xlrd.open_workbook(file_path)

table = data.sheet_by_name('Sheet1')

nrows = table.nrows

result = []

for i in range(nrows):
    cell_value = table.row_values(i)
    # print(cell_value)
    result.append(cell_value)

su = {}

for i in city:
    su[i] = []
    for j in result:
        if i[:2] in j[0] and '市辖区' not in j[0]:
            su[i].append(j)

# print(su)

citys = {'阿坝州': [['阿坝藏族羌族自治州', '513200', '0837']], '安康': [['安康市', '610900', '0915']],
         '阿克苏地区': [['阿克苏地区', '652900', '0997']], '阿里地区': [['阿里地区', '542500', '0897']],
         '阿拉善盟': [['阿拉善盟', '152900', '0483']],
         '阿勒泰地区': [['阿勒泰地区', '654300', '0906']], '安庆': [['安庆市', '340800', '0556']],
         '安顺': [['安顺市', '520400', '0853']], '鞍山': [['鞍山市', '210300', '0412']],
         '克孜勒苏州': [['克孜勒苏柯尔克孜自治州', '653000', '0908']], '安阳': [['安阳市', '410500', '0372']],
         '蚌埠': [['蚌埠市', '340300', '0552']], '白城': [['白城市', '220800', '0436']], '保定': [['保定市', '130600', '0312']],
         '北海': [['北海市', '450500', '0779']], '宝鸡': [['宝鸡市', '610300', '0917']], '北京': [['北京市', '110000', '010']],
         '毕节': [['毕节市', '520500', '0857']], '博州': [['博尔塔拉蒙古自治州', '652700', '0909']], '白山': [['白山市', '220600', '0439']],
         '百色': [['百色市', '451000', '0776']], '保山': [['保山市', '530500', '0875']], '白沙': [['白沙黎族自治县', '469025', '0802']],
         '包头': [['包头市', '150200', '0472']], '保亭': [['保亭黎族苗族自治县', '469029', '0801']],
         '本溪': [['本溪市', '210500', '0414']],
         '巴彦淖尔': [['巴彦淖尔市', '150800', '0478']],
         '白银': [['白银市', '620400', '0943']], '巴中': [['巴中市', '511900', '0827']],
         '滨州': [['滨州市', '371600', '0543']], '亳州': [['亳州市', '341600', '0558']], '长春': [['长春市', '220100', '0431']],
         '昌都': [['昌都市', '540300', '0895']], '常德': [['常德市', '430700', '0736']], '成都': [['成都市', '510100', '028']],
         '承德': [['承德市', '130800', '0314']], '赤峰': [['赤峰市', '150400', '0476']],
         '昌吉州': [['昌吉回族自治州', '652300', '0994']], '五家渠': [['五家渠市', '659004', '1994']],
         '昌江': [['昌江黎族自治县', '469026', '0803']], '澄迈': [['澄迈县', '469023', '0804']],
         '重庆': [['重庆市', '500000', '023']],
         '长沙': [['长沙市', '430100', '0731']], '常熟': [['常熟市', '320581', '0512']],
         '楚雄州': [['楚雄彝族自治州', '532300', '0878']],
         '朝阳': [['朝阳市', '211300', '0421']], '沧州': [['沧州市', '130900', '0317']], '长治': [['长治市', '140400', '0355']],
         '常州': [['常州市', '320400', '0519']], '潮州': [['潮州市', '445100', '0768']], '郴州': [['郴州市', '431000', '0735']],
         '池州': [['池州市', '341700', '0566']], '崇左': [['崇左市', '451400', '1771']], '滁州': [['滁州市', '341100', '0550']],
         '定安': [['定安县', '469021', '0806']], '丹东': [['丹东市', '210600', '0415']], '东方': [['东方市', '469007', '0807']],
         '东莞': [['东莞市', '441900', '0769']], '德宏州': [['德宏傣族景颇族自治州', '533100', '0692']],
         '大理州': [['大理白族自治州', '532900', '0872']],
         '大连': [['大连市', '210200', '0411']], '大庆': [['大庆市', '230600', '0459']],
         '大同': [['大同市', '140200', '0352']], '定西': [['定西市', '621100', '0932']],
         '大兴安岭地区': [['大兴安岭地区', '232700', '0457']], '德阳': [['德阳市', '510600', '0838']],
         '东营': [['东营市', '370500', '0546']], '黔南州': [['黔南布依族苗族自治州', '522700', '0854']],
         '达州': [['达州市', '511700', '0818']], '德州': [['德州市', '371400', '0534']], '儋州': [['儋州市', '460400', '0805']],
         '鄂尔多斯': [['鄂尔多斯市', '150600', '0477']], '恩施州': [['恩施土家族苗族自治州', '422800', '0718']],
         '鄂州': [['鄂州市', '420700', '0711']], '防城港': [['防城港市', '450600', '0770']],
         '佛山': [['佛山市', '440600', '0757']], '抚顺': [['抚顺市', '210400', '0413']],
         '阜新': [['阜新市', '210900', '0418']], '阜阳': [['阜阳市', '341200', '1558']],
         '富阳': [['富阳区', '330111', '0571']], '抚州': [['抚州市', '361000', '0794']], '福州': [['福州市', '350100', '0591']],
         '广安': [['广安市', '511600', '0826']], '贵港': [['贵港市', '450800', '1755']],
         '桂林': [['桂林市', '450300', '0773']], '果洛州': [['果洛藏族自治州', '632600', '0975']],
         '甘南州': [['甘南藏族自治州', '623000', '0941']], '固原': [['固原市', '640400', '0954']],
         '广元': [['广元市', '510800', '0839']], '贵阳': [['贵阳市', '520100', '0851']],
         '甘孜州': [['甘孜藏族自治州', '513300', '0836']], '赣州': [['赣州市', '360700', '0797']],
         '广州': [['广州市', '440100', '020']], '淮安': [['淮安市', '320800', '0517']],
         '海北州': [['海北藏族自治州', '632200', '0970']], '鹤壁': [['鹤壁市', '410600', '0392']], '淮北': [['淮北市', '340600', '0561']],
         '河池': [['河池市', '451200', '0778']], '海东地区': [['海东市', '630200', '0972']], '邯郸': [['邯郸市', '130400', '0310']],
         '哈尔滨': [['哈尔滨市', '230100', '0451']], '合肥': [['合肥市', '340100', '0551']],
         '鹤岗': [['鹤岗市', '230400', '0468']], '黄冈': [['黄冈市', '421100', '0713']], '黑河': [['黑河市', '231100', '0456']],
         '红河州': [['红河哈尼族彝族自治州', '532500', '0873']], '怀化': [['怀化市', '431200', '0745']],
         '呼和浩特': [['呼和浩特市', '150100', '0471']], '海口': [['海口市', '460100', '0898']],
         '呼伦贝尔': [['呼伦贝尔市', '150700', '0470']], '葫芦岛': [['葫芦岛市', '211400', '0429']],
         '哈密地区': [['哈密市', '650500', '0902']], '海门': [['海门市', '320684', '0513']],
         '海南州': [['海南藏族自治州', '632500', '0974']],
         '淮南': [['淮南市', '340400', '0554']], '黄南州': [['黄南藏族自治州', '632300', '0973']], '衡水': [['衡水市', '131100', '0318']],
         '黄山': [['黄山市', '341000', '0559']],
         '黄石': [['黄石市', '420200', '0714']],
         '和田地区': [['和田地区', '653200', '0903']],
         '海西州': [['海西蒙古族藏族自治州', '632800', '0977']],
         '河源': [['河源市', '441600', '0762']], '衡阳': [['衡阳市', '430400', '0734']],
         '河源': [['河源市', '441600', '0762']], '衡阳': [['衡阳市', '430400', '0734']],
         '汉中': [['汉中市', '610700', '0916']], '杭州': [['杭州市', '330100', '0571']], '菏泽': [['菏泽市', '371700', '0530']],
         '贺州': [['贺州市', '451100', '1774']], '湖州': [['湖州市', '330500', '0572']], '惠州': [['惠州市', '441300', '0752']],
         '吉安': [['吉安市', '360800', '0796']], '金昌': [['金昌市', '620300', '0935']],
         '晋城': [['晋城市', '140500', '0356']], '景德镇': [['景德镇市', '360200', '0798']], '金华': [['金华市', '330700', '0579']],
         '西双版纳州': [['西双版纳傣族自治州', '532800', '0691']], '九江': [['九江市', '360400', '0792']],
         '吉林': [['吉林市', '220200', '0432']], '即墨': [['即墨区', '370215', '0532']],
         '江门': [['江门市', '440700', '0750']], '荆门': [['荆门市', '420800', '0724']], '佳木斯': [['佳木斯市', '230800', '0454']],
         '济南': [['济南市', '370100', '0531']], '济宁': [['济宁市', '370800', '0537']],
         '酒泉': [['酒泉市', '620900', '0937']], '句容': [['句容市', '321183', '0511']],
         '湘西州': [['湘西土家族苗族自治州', '433100', '0743']], '金坛': [['金坛区', '320413', '0519']],
         '鸡西': [['鸡西市', '230300', '0467']], '嘉兴': [['嘉兴市', '330400', '0573']], '江阴': [['江阴市', '320281', '0510']],
         '揭阳': [['揭阳市', '445200', '0663']], '济源': [['济源市', '419001', '1391']], '嘉峪关': [['嘉峪关市', '620200', '1937']],
         '胶州': [['胶州市', '370281', '0532']], '焦作': [['焦作市', '410800', '0391']], '锦州': [['锦州市', '210700', '0416']],
         '晋中': [['晋中市', '140700', '0354']], '荆州': [['荆州市', '421000', '0716']],
         '库尔勒': [['库尔勒市', '652801', '0996']], '开封': [['开封市', '410200', '0378']],
         '黔东南州': [['黔东南苗族侗族自治州', '522600', '0855']], '克拉玛依': [['克拉玛依市', '650200', '0990']],
         '昆明': [['昆明市', '530100', '0871']], '喀什地区': [['喀什地区', '653100', '0998']],
         '昆山': [['昆山市', '320583', '0512']], '临安': [['临安区', '330112', '0571']], '六安': [['六安市', '341500', '0564']],
         '来宾': [['来宾市', '451300', '1772']], '聊城': [['聊城市', '371500', '0635']], '临沧': [['临沧市', '530900', '0883']],
         '娄底': [['娄底市', '431300', '0738']], '乐东': [['乐东黎族自治县', '469027', '2802']], '廊坊': [['廊坊市', '131000', '0316']],
         '临汾': [['临汾市', '141000', '0357']], '临高': [['临高县', '469024', '1896']], '漯河': [['漯河市', '411100', '0395']],
         '丽江': [['丽江市', '530700', '0888']], '吕梁': [['吕梁市', '141100', '0358']], '陇南': [['陇南市', '621200', '2935']],
         '六盘水': [['六盘水市', '520200', '0858']], '拉萨': [['拉萨市', '540100', '0891']], '乐山': [['乐山市', '511100', '0833']],
         '丽水': [['丽水市', '331100', '0578']], '凉山州': [['凉山彝族自治州', '513400', '0834']],
         '陵水': [['陵水黎族自治县', '469028', '0809']], '莱芜': [['莱芜区', '370116', '0531']], '莱西': [['莱西市', '370285', '0532']],
         '临夏州': [['临夏回族自治州', '622900', '0930']],
         '溧阳': [['溧阳市', '320481', '0519']], '辽阳': [['辽阳市', '211000', '0419']],
         '辽源': [['辽源市', '220400', '0437']], '临沂': [['临沂市', '371300', '0539']], '龙岩': [['龙岩市', '350800', '0597']],
         '洛阳': [['洛阳市', '410300', '0379']], '连云港': [['连云港市', '320700', '0518']],
         '莱州': [['莱州市', '370683', '0535']], '兰州': [['兰州市', '620100', '0931']], '林芝': [['林芝市', '540400', '0894']],
         '柳州': [['柳州市', '450200', '0772']], '泸州': [['泸州市', '510500', '0830']], '马鞍山': [['马鞍山市', '340500', '0555']],
         '牡丹江': [['牡丹江市', '231000', '0453']], '茂名': [['茂名市', '440900', '0668']],
         '眉山': [['眉山市', '511400', '1833']], '绵阳': [['绵阳市', '510700', '0816']],
         '梅州': [['梅州市', '441400', '0753']], '宁波': [['宁波市', '330200', '0574']],
         '南昌': [['南昌市', '360100', '0791']], '南充': [['南充市', '511300', '0817']],
         '宁德': [['宁德市', '350900', '0593']], '内江': [['内江市', '511000', '1832']], '南京': [['南京市', '320100', '025']],
         '怒江州': [['怒江傈僳族自治州', '533300', '0886']], '南宁': [['南宁市', '450100', '0771']], '南平': [['南平市', '350700', '0599']],
         '那曲地区': [['那曲市', '540600', '0896']], '南通': [['南通市', '320600', '0513']], '南阳': [['南阳市', '411300', '0377']],
         '平度': [['平度市', '370283', '0532']], '平顶山': [['平顶山市', '410400', '0375']], '普洱': [['普洱市', '530800', '0879']],
         '盘锦': [['盘锦市', '211100', '0427']], '蓬莱': [['蓬莱市', '370684', '0535']], '平凉': [['平凉市', '620800', '0933']],
         '莆田': [['莆田市', '350300', '0594']], '萍乡': [['萍乡市', '360300', '0799']],
         '濮阳': [['濮阳市', '410900', '0393']], '攀枝花': [['攀枝花市', '510400', '0812']],
         '青岛': [['青岛市', '370200', '0532']], '琼海': [['琼海市', '469002', '1894']], '秦皇岛': [['秦皇岛市', '130300', '0335']],
         '曲靖': [['曲靖市', '530300', '0874']], '齐齐哈尔': [['齐齐哈尔市', '230200', '0452']], '七台河': [['七台河市', '230900', '0464']],
         '黔西南州': [['黔西南布依族苗族自治州', '522300', '0859']], '清远': [['清远市', '441800', '0763']],
         '庆阳': [['庆阳市', '621000', '0934']], '钦州': [['钦州市', '450700', '0777']], '衢州': [['衢州市', '330800', '0570']],
         '泉州': [['泉州市', '350500', '0595']], '琼中': [['琼中黎族苗族自治县', '469030', '1899']], '荣成': [['荣成市', '371082', '0631']],
         '日喀则': [['日喀则市', '540200', '0892']], '乳山': [['乳山市', '371083', '0631']], '日照': [['日照市', '371100', '0633']],
         '韶关': [['韶关市', '440200', '0751']], '寿光': [['寿光市', '370783', '0536']], '上海': [['上海市', '310000', '021']],
         '绥化': [['绥化市', '231200', '0455']], '石河子': [['石河子市', '659001', '0993']], '石家庄': [['石家庄市', '130100', '0311']],
         '商洛': [['商洛市', '611000', '0914']], '三明': [['三明市', '350400', '0598']],
         '三门峡': [['三门峡市', '411200', '0398']], '山南': [['山南市', '540500', '0893']],
         '遂宁': [['遂宁市', '510900', '0825']], '四平': [['四平市', '220300', '0434']], '商丘': [['商丘市', '411400', '0370']],
         '宿迁': [['宿迁市', '321300', '0527']], '上饶': [['上饶市', '361100', '0793']],
         '汕头': [['汕头市', '440500', '0754']], '汕尾': [['汕尾市', '441500', '0660']], '绍兴': [['绍兴市', '330600', '0575']],
         '三亚': [['三亚市', '460200', '0899']], '邵阳': [['邵阳市', '430500', '0739']],
         '沈阳': [['沈阳市', '210100', '024']], '十堰': [['十堰市', '420300', '0719']], '松原': [['松原市', '220700', '0438']],
         '双鸭山': [['双鸭山市', '230500', '0469']], '深圳': [['深圳市', '440300', '0755']], '朔州': [['朔州市', '140600', '0349']],
         '宿州': [['宿州市', '341300', '0557']], '随州': [['随州市', '421300', '0722']],
         '苏州': [['苏州市', '320500', '0512']], '石嘴山': [['石嘴山市', '640200', '0952']],
         '泰安': [['泰安市', '370900', '0538']], '塔城地区': [['塔城地区', '654200', '0901']],
         '太仓': [['太仓市', '320585', '0512']], '铜川': [['铜川市', '610200', '0919']], '屯昌': [['屯昌县', '469022', '1892']],
         '通化': [['通化市', '220500', '0435']], '天津': [['天津市', '120000', '022']],
         '铁岭': [['铁岭市', '211200', '0410']], '通辽': [['通辽市', '150500', '0475']],
         '铜陵': [['铜陵市', '340700', '0562']], '吐鲁番地区': [['吐鲁番市', '650400', '0995']], '铜仁地区': [['铜仁市', '520600', '0856']],
         '唐山': [['唐山市', '130200', '0315']], '天水': [['天水市', '620500', '0938']], '太原': [['太原市', '140100', '0351']],
         '台州': [['台州市', '331000', '0576']], '泰州': [['泰州市', '321200', '0523']], '文昌': [['文昌市', '469005', '1893']],
         '文登': [['文登区', '371003', '0631']], '潍坊': [['潍坊市', '370700', '0536']], '瓦房店': [['瓦房店市', '210281', '0411']],
         '威海': [['威海市', '371000', '0631']], '乌海': [['乌海市', '150300', '0473']],
         '芜湖': [['芜湖市', '340200', '0553']], '武汉': [['武汉市', '420100', '027']],
         '吴江': [['吴江区', '320509', '0512']],
         '乌兰察布': [['乌兰察布市', '150900', '0474']],
         '乌鲁木齐': [['乌鲁木齐市', '650100', '0991']], '渭南': [['渭南市', '610500', '0913']],
         '万宁': [['万宁市', '469006', '1898']], '文山州': [['文山壮族苗族自治州', '532600', '0876']],
         '武威': [['武威市', '620600', '1935']], '无锡': [['无锡市', '320200', '0510']], '温州': [['温州市', '330300', '0577']],
         '吴忠': [['吴忠市', '640300', '0953']], '梧州': [['梧州市', '450400', '0774']], '五指山': [['五指山市', '469001', '1897']],
         '西安': [['西安市', '610100', '029']],
         '兴安盟': [['兴安盟', '152200', '0482']], '许昌': [['许昌市', '411000', '0374']], '宣城': [['宣城市', '341800', '0563']],
         '襄阳': [['襄阳市', '420600', '0710']], '孝感': [['孝感市', '420900', '0712']], '迪庆州': [['迪庆藏族自治州', '533400', '0887']],
         '锡林郭勒盟': [['锡林郭勒盟', '152500', '0479']], '厦门': [['厦门市', '350200', '0592']],
         '西宁': [['西宁市', '630100', '0971']], '咸宁': [['咸宁市', '421200', '0715']],
         '湘潭': [['湘潭市', '430300', '0732']],
         '邢台': [['邢台市', '130500', '0319']],
         '新乡': [['新乡市', '410700', '0373']], '咸阳': [['咸阳市', '610400', '0910']],
         '新余': [['新余市', '360500', '0790']], '信阳': [['信阳市', '411500', '0376']], '忻州': [['忻州市', '140900', '0350']],
         '徐州': [['徐州市', '320300', '0516']], '雅安': [['雅安市', '511800', '0835']], '延安': [['延安市', '610600', '0911']],
         '延边州': [['延边朝鲜族自治州', '222400', '1433']], '宜宾': [['宜宾市', '511500', '0831']], '盐城': [['盐城市', '320900', '0515']],
         '宜昌': [['宜昌市', '420500', '0717']], '宜春': [['宜春市', '360900', '0795']], '银川': [['银川市', '640100', '0951']],
         '运城': [['运城市', '140800', '0359']], '伊春': [['伊春市', '230700', '0458']],
         '云浮': [['云浮市', '445300', '0766']], '阳江': [['阳江市', '441700', '0662']], '营口': [['营口市', '210800', '0417']],
         '榆林': [['榆林市', '610800', '0912']], '玉林': [['玉林市', '450900', '0775']],
         '伊犁哈萨克州': [['伊犁哈萨克自治州', '654000', '0999']], '阳泉': [['阳泉市', '140300', '0353']],
         '玉树州': [['玉树藏族自治州', '632700', '0976']], '烟台': [['烟台市', '370600', '0535']],
         '鹰潭': [['鹰潭市', '360600', '0701']], '义乌': [['义乌市', '330782', '0579']], '宜兴': [['宜兴市', '320282', '0510']],
         '玉溪': [['玉溪市', '530400', '0877']], '益阳': [['益阳市', '430900', '0737']],
         '岳阳': [['岳阳市', '430600', '0730']],
         '扬州': [['扬州市', '321000', '0514']], '永州': [['永州市', '431100', '0746']], '淄博': [['淄博市', '370300', '0533']],
         '自贡': [['自贡市', '510300', '0813']], '珠海': [['珠海市', '440400', '0756']], '湛江': [['湛江市', '440800', '0759']],
         '镇江': [['镇江市', '321100', '0511']], '诸暨': [['诸暨市', '330681', '0575']],
         '张家港': [['张家口市', '130700', '0313']],
         '张家界': [['张家界市', '430800', '0744']],
         '张家口': [['张家口市', '130700', '0313']], '周口': [['周口市', '411600', '0394']],
         '驻马店': [['驻马店市', '411700', '0396']], '章丘': [['章丘区', '370114', '0531']], '肇庆': [['肇庆市', '441200', '0758']],
         '中山': [['中山市', '442000', '0760']], '舟山': [['舟山市', '330900', '0580']],
         '昭通': [['昭通市', '530600', '0870']], '中卫': [['中卫市', '640500', '1953']], '张掖': [['张掖市', '620700', '0936']],
         '招远': [['招远市', '370685', '0535']], '资阳': [['资阳市', '512000', '0832']],
         '遵义': [['遵义市', '520300', '0852']], '枣庄': [['枣庄市', '370400', '0632']], '漳州': [['漳州市', '350600', '0596']],
         '郑州': [['郑州市', '410100', '0371']], '株洲': [['株洲市', '430200', '0733']]}
import pymysql as mdb




result = []
for i in citys:
    result.append(citys[i][0][1][:2] + '0000')

result2 = sorted(list(set(result)))

res = []

for i in range(nrows):
    cell_value = table.row_values(i)
    if cell_value[1] in result2:
        print(cell_value[0], cell_value[1])

