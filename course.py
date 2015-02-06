import os
import urllib.request
from bs4 import BeautifulSoup
import requests
i = 0
depNo = "F7"
seqNo = "107"
passwd = ""
stu_no = ""

def test(depNo, seqNo):
    try:
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
        url = "http://course.ncku.edu.tw/course/" +\
              soup.select("img")[0]['src']

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
        print(r.text)
    except:
        pass
    r = s.get("http://course.ncku.edu.tw/course/logout.php")
    return

opener = urllib.request.build_opener()
while 1:
    r = opener.open("http://140.116.165.74/qry/qry001.php?dept_no=F7",
                    timeout=100)
    org_str = r.read().decode("utf-8", "ignore")
    soup = BeautifulSoup(org_str)
    a = soup.select('.course_y3')
    if len(a) < 4:
        continue
    b = a[3].select("td")
    if b[15].getText() != '額滿':
        test(depNo, seqNo)
        # os.system('google-chrome http://i.ncku.edu.tw')
        break
    else:
        print(str(i))
        i += 1
