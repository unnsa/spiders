import json
import random
import re
import time

import requests

from aiqicha.spider_aiqicha_detail import getAndSaveCompanyDetail
from config import MysqlEnviron
from db.models import CompanySummary
from db.mysql_connector import save_company_summary


def get_proxy():
    # 需要根据自己ip代理服务构造一个函数
    # 返回一个ip地址
    # 格式"http://000.000.000.000:0000"
    return line


def req_get_proxy(url):
    global line

    # 代理不可用则直接换一个代理ip
    try:
        proxy = {
            'http': line,
            'https': line
        }
        resp = requests.get(url, headers=headers, timeout=10)
    except:
        line = get_proxy()
        resp = req_get(url)

    # 服务器禁用该代理ip，则再换一个
    if 'check' in resp.url:
        line = get_proxy()
        resp = req_get(url)

    return resp


t0 = time.time()


def req_get(url):
    # 每次禁用ip，1min后会解封
    global t0
    try:
        resp = requests.get(url, headers=headers, timeout=1000)
    except:
        resp = req_get(url)
    if 'check' in resp.url:
        t1 = time.time()
        dt = 60 - t1 + t0
        dtt = dt if dt >= 0 else 0
        time.sleep(dtt)
        resp = req_get(url)
        t0 = time.time()
    return resp


def write_comp(resp):
    # 直接存json格式
    jd = json.loads(resp.text)
    for comp in jd['data']['resultList']:
        asp = json.dumps(comp)
        # out_file.write(asp.encode('utf-8').decode("unicode_escape") + '\n')


def save_com(resp):
    jd = json.loads(resp.text)
    for comp in jd['data']['resultList']:
        companySummary = CompanySummary()
        companySummary.pid = comp['pid']
        companySummary.ent_name = json.dumps(comp['entName']).encode('utf-8').decode("unicode_escape") \
            .replace('<em>', '').replace('</em>', '')
        companySummary.ent_type = json.dumps(comp['entType']).encode('utf-8').decode("unicode_escape")
        companySummary.domicile = json.dumps(comp['domicile']).encode('utf-8').decode("unicode_escape") \
            .replace('<em>', '').replace('</em>', '')
        save_company_summary(companySummary.__dict__)
        getAndSaveCompanyDetail(comp['pid'])


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'BIDUPSID=29E6E4A348165538E4EFCC68889A3F6F; PSTM=1617936522; BAIDUID=29E6E4A34816553809EBF3AD698856BF:FG=1; __yjs_duid=1_54e7f2b066360ce221bcbedede23e8381617942933689; BDPPN=411183439b380c0046ae55d34418a222; log_guid=8fa1540916ee795c034886877ee3f294; _j47_ka8_=57; MCITY=-131%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=33801_33970_31254_34004_33772_33675_33607_26350; BDSFRCVID=ImIOJexroG382q3e6g3vrZw0HeKKg7jTDYrEZguiLEnlccDVJeC6EG0PtOqPGZu-EHtdogKK0mOTHUuF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tRKOoILKfIt3fP36qRQj-ICShUFsaMoWB2Q-XPoO3KO4hhOFbjjxXPKXWltjBPQiWKkfBfbgy4opOJPm2jorbTKOh4RpWJbpBmTxoUJ2fnbvVhQM-xOzX4AebPRiJPr9QgbPLlQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hDvpMJQE-Pk_qx5Ka43tHD7yWCvYalTcOR59K4nnDTvXKHb-tt-ebjrzLKJd5lvveI3F3MOZKxLlbpo0WUQXaI72KUQF5l8-sq0x0bOcKq81Wl_L0xvJ5IOMahkMal7xOM5GQlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3YjjISKx-_J5k8JbTP; Hm_lvt_ad52b306e1ae4557f5d3534cce8f8bbf=1620287915,1621567873; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; BDSFRCVID_BFESS=ImIOJexroG382q3e6g3vrZw0HeKKg7jTDYrEZguiLEnlccDVJeC6EG0PtOqPGZu-EHtdogKK0mOTHUuF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tRKOoILKfIt3fP36qRQj-ICShUFsaMoWB2Q-XPoO3KO4hhOFbjjxXPKXWltjBPQiWKkfBfbgy4opOJPm2jorbTKOh4RpWJbpBmTxoUJ2fnbvVhQM-xOzX4AebPRiJPr9QgbPLlQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hDvpMJQE-Pk_qx5Ka43tHD7yWCvYalTcOR59K4nnDTvXKHb-tt-ebjrzLKJd5lvveI3F3MOZKxLlbpo0WUQXaI72KUQF5l8-sq0x0bOcKq81Wl_L0xvJ5IOMahkMal7xOM5GQlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3YjjISKx-_J5k8JbTP; delPer=0; PSINO=5; BAIDUID_BFESS=29E6E4A34816553809EBF3AD698856BF:FG=1; BA_HECTOR=al85850l808185agqj1gaeloo0q; ZD_ENTRY=baidu; _fb537_=xlTM-TogKuTwCF0ktHXhf1QnYX%2ANG6d9JTiYVreoe3Z48QngTOxG1Xsmd; ZX_UNIQ_UID=b0a6fefddf97b3d99e26319f1942a49c; Hm_lpvt_ad52b306e1ae4557f5d3534cce8f8bbf=1621582281; __yjs_st=2_NzIyOWUyZGUxY2Q4YzgxOGJhMTI3YjAxNzBlZWYyMDNiZTI2NGUxODMxNmM1ZmRmY2NkYTFkNjJhYjQwODk4ODk0ZDg4NmQ0NWYzZjAzNDJjN2RmNjNiYTU4YTQ4ZDRlNWYwMTA0MWZlZjk1ZDM0MGUwNmNhOTJhNDhhZDRiMWJmYzBmMGE0ODkwOTkyMDZiYTRhYTAyMGNmZDg3NTY3NmZlOGUwMTY3ZTQ4YzFiYzFiYjk0MTYxYTQ4NjFkZTE2MjhmNzZlYmFiYzY4ZDAyNWY1MGJiZTFjMTIxY2EzYzkyOGQ2YzRmNTQ3YTdhNTlmYmEwMjVmNDNlNTVlNDI3ZF83XzAzZjUwZDI2; ab_sr=1.0.0_MmM1YTM2OTc4NmU0YmMzYTg5M2UzZTFlMzE4ZDUxN2Q1ZmE0NzgwMmMxOGM4NzNiMTYyZGQzYzdmZjIwOWJhYTVlODM4ZDBmZjdkZjlmYWYyZjljMGIzMGE4NmUwNzQ1; _s53_d91_=056ddb149824a8d208ac8ae78877123ef0f6696a0c1fdba54566ebc6004a57e33e56a43840742855c635cd2ad1ac1ed02c610ad2d35cf0d8f48dea1ae133c94ca6fd9a6e3772b8dd96fe2004cf56d1d0fa71ed2e19357c234b32d92cf0bbe6c739e1ccf123245b78cb280ff44a42baf5a37e754ab04569712bd3df9436fdb46deabf7a2fd943dcb5c3afd19cd8246d91ac458a623e9f03921583c19fac0712faf1fc2cff91a8e46708571c8f7fdb172028803bb9f7ed2de7be63a62ee334ab342dfef21d86bd50f336d94ca33e3dc929ed7698431d54fe69750a4f0358f4ec4f; _y18_s21_=1a8319ca',
    'Host': 'aiqicha.baidu.com'
}


def getDistrictList() -> set:
    districtListUrl = 'https://aiqicha.baidu.com/index/districtListAjax'
    districtListResponse = req_get(districtListUrl)
    districtListResponseJson = json.loads(districtListResponse.text)
    districtListData = districtListResponseJson['data']
    districtList = []
    for ds in districtListData:
        provinceList = ds['province']
        cityList = ds['city']
        if len(provinceList) > 0:
            for province in provinceList:
                if len(province) > 0:
                    districtList.append(province)
        if len(cityList) > 0:
            for city in cityList:
                if len(city) > 0:
                    districtList.append(city)
    return set(districtList)


# 有代理池的把use_proxy的值改成1
if __name__ == '__main__':
    use_proxy = 0
    kw = '北京市'
    host = MysqlEnviron.host
    if use_proxy == 1:
        line = get_proxy()
        req_get = req_get_proxy
    district_list = getDistrictList()
    for district in district_list:
        url0 = 'https://aiqicha.baidu.com/s?q=%s&t=3' % (district)
        resp = req_get(url0)
        pdAll = re.findall('pageData = ({.*})', resp.text)
        page_data = pdAll[0].encode("utf8")
        jd = json.loads(page_data)
        print(jd)
        tnum = int(jd['result']['totalNumFound'])
        page = tnum // 10 + 1
        for p in range(page):
            time.sleep(random.randint(1, 9))
            headers.setdefault('Referer', 'https://aiqicha.baidu.com/s?q=%E5%B9%BF%E4%B8%9C%E7%9C%81&t=3')
            url_page = 'https://aiqicha.baidu.com/s/l?q=%s&t=&p=%d&s=10&o=0&f={}' % (district, p + 1)
            try:
                resp = req_get(url_page)
                save_com(resp)
            except:
                line = get_proxy()
                resp = req_get(url_page)
                save_com(resp)
