# 这里的可以自己添加修改，目前只支持 Ollama 框架 和 gpt

import json
import requests


# # POST 请求
# def data_post(pageNum, pageSize, appsecret, url):
#     # 以字典形式编辑请求体
#     data_value = {'pageNum':pageNum, 'pageSize':pageSize, 'appsecret':appsecret}
#     # 发送 POST 请求，返回一个包含服务器响应信息的 response 对象
#     response = requests.post(url = url, data = data_value)
    
#     if response.status_code == 200:
#         # 响应信息中status为1，表示成功获取数据
#         if response.json()['status'] == 1:
#             data = pd.DataFrame(response.json()['data'])
#         else:
#             print(response.json())
#     else:
#         raise Exception('URL未正常响应请求')
#     return data

    
post_json = {
  "model": "llama3:8b",
  "prompt": "Hello",
  "stream": False # type: ignore
}

x = requests.post("http://localhost:11434/api/generate", json=post_json)

a =  print(x.json()['response'])