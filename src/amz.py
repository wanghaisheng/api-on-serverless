# 示例使用
# save_valid_proxies('path_to_proxy_file.txt', ['proxy1', 'proxy2', 'proxy3'])
import requests
import json
def getSellerJson(sellerid):

        print("start to do", sellerid)
        url = "https://mercury.revseller.com/api/us/data5/"

        # time.sleep(lag)
        surl = url + sellerid + "?domain=1&seller=" + sellerid
        # print(f"try without proxy {sellerid}")


                # valid_proxies.remove(pro_str)
        max_retries = 5

        proxies=None
        pro_str=None
        for i in range(max_retries):

            if i==0:
                
                # print('without proxy')
                pass
                
            else:
                pro_str = get_proxy()["proxy"]

                proxy = "http://{}".format(pro_str)

                # proxy = f"http://{rand_proxies()}"
                proxies = {"http": proxy, "https": proxy.replace("http", "https")}
                print(f"{i}========get new proxy======= {proxies}")
                try:
                    response = requests.get(
                        surl,
                        headers=headers,
                        proxies=proxies # 如果需要代理，取消注释并设置正确的代理

                                                        # , verify=False

                )
                    response.raise_for_status()  # 这将为4XX和5XX的响应抛出异常

                    data = response.json()
                
                    try:
                        data['sellers'][sellerid]

                        print('found seller with proxy',pro_str)
                        print(f"Data saved for sellerid: {sellerid}")

                        return json.dump(data, ensure_ascii=False, indent=4)


        # 保存更新后的代理列表
                    except:
                        print('no seller json')
                        raise
                        
                except Exception as e:  # 捕获请求相关的异常
                # print(f"Attempt failed with error: {e}")

                        print(f"Attempt {i+1} failed with error:{e}")

                        if i < max_retries - 1:
                                # time.sleep(2**i)  # 指数退避策略
                                print("Retrying...")
                                continue  # 继续下一次重试
                        else:
                                print(
                                "Max retries reached. Exiting without a successful response."
                                )
                                break  # 最大重试次数达到，退出循环


def get_proxy():
    return requests.get("http://demo.spiderpy.cn/get").json()
