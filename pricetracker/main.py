import requests

from bs4 import BeautifulSoup
url= f"https://www.amazon.in/Lenovo-7235HS-NVIDIA-Windows-83JC00HNIN/dp/B0F832WDMW/ref=sr_1_2_sspa?adgrpid=139727317401&dib=eyJ2IjoiMSJ9.B3PtivOvq-qDZVwW9AtfKMlQ2_zAWI85UTK-lbab4D__PpeqgD6LBXuLS5wowj76Ih9m1XMQZHwY5PXQw738KyPYVGmg4NluzJ9zyFYpCWvt5BTZgPM18WklFYcJ2OmbQSJJsGikHu8oEBmSaqesGQk_wctviPAMGum4EeMIRTFOLIUc_tvRXY_uBI1Ld2846iNQYPqIlyEhXDkcrV2g-j7vOPZOA9e6mlqysoofjGY.Ve3yy8JYwVHpSqMaqXZKvetRpTDAzCK_IuFTVMWqKpk&dib_tag=se&ext_vrnc=hi&hvadid=595561821817&hvdev=c&hvlocphy=9061656&hvnetw=g&hvqmt=e&hvrand=13393324105087864555&hvtargid=kwd-1707598348484&hydadcr=26891_2178119&keywords=asus%2Bvivobook%2Bryzen%2B7%2Brtx%2B3050&mcid=ecbdda4c8af635e5a6b1eebf937fb0a1&qid=1768930936&sr=8-2-spons&aref=72P9ElrrS8&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
response=requests.get(url=url)
soup=BeautifulSoup(response.text,"html.parser")
price=soup.find(name="span",class_="a-price-whole").getText() 
print(price)