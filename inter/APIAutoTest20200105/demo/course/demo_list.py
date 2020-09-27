#【案例2】：教管系统-列出课程
from config import HOST
import requests
# r 表示响应消息  r.text表示响应消息体的文本格式
payload={"action":"list_course",
         "pagenum":1,
         "pagesize":20
         }
r1=requests.get(f'{HOST}/api/mgr/sq_mgr/',params=payload)
print(r1.text)


