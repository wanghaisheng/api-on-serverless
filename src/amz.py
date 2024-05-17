# 示例使用
# save_valid_proxies('path_to_proxy_file.txt', ['proxy1', 'proxy2', 'proxy3'])
import requests
import json

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,zh;q=0.8,zh-CN;q=0.7",
    "Origin": "chrome-extension://gobliffocflfaekfcaccndlffkhcafhb",
    "Priority": "u=1, i",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
}
def getSellerJson(sellerid):

        print("start to do", sellerid)
        url = "https://mercury.revseller.com/api/us/data5/"

        # time.sleep(lag)
        surl = url + sellerid + "?domain=1&seller=" + sellerid
        print(f"try without proxy {surl}")
        try:
            response = requests.get(
                surl,
                headers=headers,
                # proxies=proxies # 如果需要代理，取消注释并设置正确的代理

                                                # , verify=False

        )
            response.raise_for_status()  # 这将为4XX和5XX的响应抛出异常

            data = response.json()
        
            try:
                data['sellers'][sellerid]

                print(f"Data saved for sellerid: {sellerid}")

                return json.dump(data, ensure_ascii=False, indent=4)


# 保存更新后的代理列表
            except:
                print('no seller json')
                raise
                
        except Exception as e:  # 捕获请求相关的异常
        # print(f"Attempt failed with error: {e}")

            return None


def get_proxy():
    return requests.get("http://demo.spiderpy.cn/get").json()
