import requests
import json
import urllib
import openpyxl
import datetime
import time


def write_excel_xlsx(path, sheet_name, value):
    index = len(value)
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = sheet_name
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.cell(row=i+1, column=j+1, value=str(value[i][j]))
    workbook.save(path)


def main():
    headers = {
        'authority': 'www.okcupid.com',
        'method': 'GET',
        'path': '/1/apitun/profile/8682176196122051737/answer_filters',
        'scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
        'cache-control': 'no-cache',
        'cookie': '__cfduid=d0112423b354148b60f0ad304bb8e12c61582789448; ua=531227642bc86f3b5fd7103a0c0b4fd6; ab.storage.deviceId.719f8d59-40d7-4abf-b9c3-fa4bf5b7cf54=%7B%22g%22%3A%2251d083d1-cd69-8665-3653-9f55779cdd19%22%2C%22c%22%3A1582789451379%2C%22l%22%3A1582789451379%7D; _fbp=fb.1.1582789451424.357395099; __ssid=b5dca68db7a66261e187ff7117a445e; override_session=0; secure_check=1; _ga=GA1.2.808932242.1582789599; _gid=GA1.2.412142388.1582789599; kppid_managed=Mzz8BZdh; crfgL0cSt0r=true; __gads=ID=b1fe17a3343f30c8:T=1582789603:S=ALNI_MYXHsyPqQtByKCnP5TSNOwwHyuVZw; OptanonAlertBoxClosed=2020-02-27T07:59:35.774Z; eupubconsent=BOvaqUNOvaqUNAcABBENC3-AAAAtR7__f__3_8_v3_9_NuzvOv_j_ef93VW8fvYvcEvzhY9d_u_Uzxc4m_0vRc9ycgx85eprGsoxQ7KasG-VOgd_7t__3ziX9oxP6wkcprz33bEw-ro2v-ZzICGN_AA; siftsession=16037455942230659753; secure_login=1; session=8682176196122051737%3A10221058595715747946; authlink=13d3e09cce1ca925; ab.storage.userId.719f8d59-40d7-4abf-b9c3-fa4bf5b7cf54=%7B%22g%22%3A%228682176196122051737%22%2C%22c%22%3A1582806811211%2C%22l%22%3A1582806811211%7D; OptanonConsent=isIABGlobal=false&datestamp=Thu+Feb+27+2020+22%3A32%3A25+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=5.10.0&landingPath=NotLandingPage&groups=1%3A1%2C3%3A1%2C4%3A1%2C0_175959%3A1%2C0_175960%3A1%2C0_175961%3A1%2C0_183847%3A1%2C0_183846%3A1%2C0_183848%3A1%2C101%3A1%2C102%3A1%2C103%3A1%2C104%3A1%2C105%3A1&AwaitingReconsent=false; nano=k%3Diframe_prefix_lock_1%2Ce%3D1582814016592%2Cv%3D1; _gat=1; ab.storage.sessionId.719f8d59-40d7-4abf-b9c3-fa4bf5b7cf54=%7B%22g%22%3A%22192fea88-1191-48f6-d9cf-99a2a709bade%22%2C%22e%22%3A1582815747013%2C%22c%22%3A1582813947014%2C%22l%22%3A1582813947014%7D; amplitude_id_f90f10ee203f3f5f1e142ad0a976ee20_desktopokcupid.com=eyJkZXZpY2VJZCI6ImVjMTYzNWViLTI0OWUtNGNlNC05MWYzLTFjMjdhOTI5M2E4MVIiLCJ1c2VySWQiOiI4NjgyMTc2MTk2MTIyMDUxNzM3Iiwib3B0T3V0IjpmYWxzZSwic2Vzc2lvbklkIjoxNTgyODEzOTQ0OTI4LCJsYXN0RXZlbnRUaW1lIjoxNTgyODEzOTY3MjY3LCJldmVudElkIjo5NCwiaWRlbnRpZnlJZCI6Miwic2VxdWVuY2VOdW1iZXIiOjk2fQ==',
        'pragma': 'no-cache',
        'referer': 'https://www.okcupid.com/profile/8682176196122051737/questions?rqid=35',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'x-okcupid-platform': 'DESKTOP'
    }
    # path, cookie, refer需要每次调整（）；其它按照电脑浏览器调一次之后不需调整
    res = requests.get('https://www.okcupid.com/1/apitun/profile/8682176196122051737/answers?filter=1', headers=headers)
    data = json.loads(res.content).get('data')
    paging = json.loads(res.content).get('paging')
    final_list = []
    while len(final_list) != paging['total']:
        for item in data:
            temp_list = []
            try:
                temp_list.append(item['question']['genre'])
                temp_list.append(item['question']['text'])
                for answer in item['question']['answers']:
                    temp_list.append(answer)
            except:
                pass
            if len(temp_list) != 0:
                final_list.append(temp_list)
        after_cursor = urllib.parse.quote(paging['cursors']['after'])
        time.sleep(1)
        res = requests.get(f'https://www.okcupid.com/1/apitun/profile/8437071393684167093/answers?after={after_cursor}&filter=1', headers=headers)
        data = json.loads(res.content).get('data')
        paging = json.loads(res.content).get('paging')
    print(len(final_list))
    print(final_list)

    save_path = 'okcupid_question.xlsx'
    sheet_name = f"question_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
    write_excel_xlsx(save_path, sheet_name, final_list)


if __name__ == '__main__':
    main()