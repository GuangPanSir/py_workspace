/*nodejs中间件服务器*/
var express = require('express');
var app = express();

app.all('*', function (req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "X-Requested-With");
    res.header("Access-Control-Allow-Methods", "POST,GET,PUT,DELETE,OPTIONS");
    res.header("X-Powered-By", "3.2.1");
    res.header("Content-Type", "application/json;charset=utf-8");
    next();
});

app.get('/get_data', function (req, res) {
    var tabBtnList = ['推荐商品', '居家生活', '服饰鞋包', '美食酒水', '个护清洁', '母婴亲子', '运动旅行', '数码家电', '全球特色'];
    res.send(tabBtnList);
});

app.listen(5632, function () {
    console.log('中间件已经运行！');
});