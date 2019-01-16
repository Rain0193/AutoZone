#coding:utf-8
import re
import difflib

# def get_token(result):
#     global token
#     regx = "'token':'(.*?)',"
#     token = re.findall(regx, result)[0]
#     if token != '':
#         return token
#
# if __name__ == '__main__':
#     result = {"msg":"成功","data":{"sex":"0","token":"side3y7uio156415444rtmuygh826yug2984005","niceName":"test1"},"state": 0}
#     result = str(result).replace(' ', '')
#     value = get_token(result)
#     print(value)
url1 = "www_token=986a8258195f25a48b836bd216a37bb3; Hm_lvt_cde2ca53bcf3a8674541df9912d3a49b=1541984559; s=5A529G9y; __ozlvd1868=1541984825; __utma=152562790.591494845.1541984826.1541984826.1541984826.1; __utmc=152562790; __utmz=152562790.1541984826.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=152562790.1.10.1541984826; c=Z6JG56Bs; sc=0; verify_number='+pgPuWOg18YeZ5G+JBhl5w==_1541984799408'; Hm_lpvt_cde2ca53bcf3a8674541df9912d3a49b=1541984834; v=wx_e4rbn1srl5; p=1702172437%261541984809000%26WaYZ4kMno1P4uzQr33m0WA%3D%3D"
url2 = "www_token=986a8258195f25a48b836bd216a37bb3; Hm_lvt_cde2ca53bcf3a8674541df9912d3a49b=1541984559; s=5A529G9y; verify_number='bQGV3krVPBDy9ZfOcZdKoQ==_1541984669766'; sc=1; Hm_lpvt_cde2ca53bcf3a8674541df9912d3a49b=1541984825; __ozlvd1868=1541984825; __utma=152562790.591494845.1541984826.1541984826.1541984826.1; __utmc=152562790; __utmz=152562790.1541984826.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=152562790.1.10.1541984826"
d=difflib.Differ()
diff=d.compare(url1.splitlines(),url2.splitlines())
print("\n".join(list(diff)))