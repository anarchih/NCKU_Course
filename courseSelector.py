import requests
from bs4 import BeautifulSoup
import os
# fileName = "test.png"
depNo = "F7"
seqNo = "107"
stu_no = ""
passwd = ""
s = requests.Session()


data = {
    "id_no": "a94a8fe5ccb19ba61c4c0873d391e987982fbbd3",
    "passwd": passwd,
    "stu_no": stu_no
}
r = s.post("http://course.ncku.edu.tw/course/login.php", data=data)
data = {
    "STEP": "1",
    "depNo": depNo,
    "seqNo": seqNo
}
r = s.post("http://course.ncku.edu.tw/course/second2.php", data=data)
r.encoding = "big5"
soup = BeautifulSoup(r.text)
url = "http://course.ncku.edu.tw/course/" + soup.select("img")[0]['src']

os.system('google-chrome ' + url)

cer = input("cer:")
# response = requests.get(url, stream=True)
# with open('img.png', 'wb') as out_file:
#   shutil.copyfileobj(response.raw, out_file)
# del response

data = {
    "STEP": "2",
    "cer": cer,
    "depNo": depNo,
    "seqNo": seqNo
}
r = s.post("http://course.ncku.edu.tw/course/second2.php", data=data)
r.encoding = "big5"
r.text
