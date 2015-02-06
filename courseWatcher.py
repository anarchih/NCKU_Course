import os
import urllib.request
from bs4 import BeautifulSoup
opener = urllib.request.build_opener()
depNo = "F7"
seqNo = "123"

i = 0
while 1:
    r = opener.open("http://140.116.165.74/qry/qry001.php?dept_no=" + depNo,
                    timeout=100)
    org_str = r.read().decode("utf-8", "ignore")
    soup = BeautifulSoup(org_str)
    a = soup.select('.course_y2')
    if len(a) < 10:
        continue
    b = a[3].select("td")
    if b[15].getText() != '額滿':
        os.system('google-chrome http://i.ncku.edu.tw')
        break
    else:
        print(str(i))
        i += 1
