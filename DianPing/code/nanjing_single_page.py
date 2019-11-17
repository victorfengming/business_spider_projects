#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by 秋叶夏风

# 本模块的功能:<>
# TODO 大众点评详情页:本页面爬取的时候返回了一个python-requests,凉凉
import re
from requests import get

class Single_page:
    def __init__(self,url):
        self.url = url
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'cy=18; cye=shenyang; _lx_utm=utm_source%3Dbing%26utm_medium%3Dorganic; _lxsdk_cuid=16e790e79f8c8-038d795d750a27-7711a3e-1fa400-16e790e79f8c8; _lxsdk=16e790e79f8c8-038d795d750a27-7711a3e-1fa400-16e790e79f8c8; _hc.v=4deccfc7-5e47-90b6-4e04-c4fa5f04fa52.1573989023; dper=787e722a04789af45b427ca35bbec77181b34798d90839accfa5e0a18d0502963399c73db5deb3b27efefd7c0287e85b22a33f57cbbb589e24320b28c213e8f312b3022c75e4fb53c10f00c75e7f3d4bb3383c4d80b1005ac16862677b4e8321; ll=7fd06e815b796be3df069dec7836c3df; ua=%E6%B8%85%E6%99%A8%E7%9A%84%E7%AC%AC%E4%B8%80%E7%BC%95%E9%98%B3%E5%85%89; ctu=db66980f435a78ed85b78178324c2e61fe832ac34177aa8fdacf19f749dc1117; s_ViewType=10; _lxsdk_s=16e790e79fa-ca7-356-747%7C%7C79',
            'Host': 'www.dianping.com',
            'If-Modified-Since': 'Sun, 17 Nov 2019 01:45:42 GMT',
            'If-None-Match': '"8b8f9444258bb61b05f5d9bcadca98eb"',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
        }
        self._get_single_page_html()
    def _get_single_page_html(self):
        resp = get(self.url)
        resp = resp.content.decode("utf-8")
        self.txt = resp


if __name__ == '__main__':

    sp = Single_page("http://www.dianping.com/shop/67824544")
    print(sp.txt)