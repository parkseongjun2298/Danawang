import urllib.request
from urllib.parse import urlencode, quote_plus, unquote
import xml.etree.ElementTree

 

result = list()

Nene_URL = 'http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s' % (quote_plus('전체'), quote_plus('전체'))

 

rcv_data = urlencode(Nene_URL)

rcv_data = rcv_data.read()

 

root = xml.etree.ElementTree.fromstring(rcv_data) #XML 파싱 

for element in root.getiterator("item"):

    storelist = list()

    storelist.append(element.findtext('aname1')) #<aname1>태그의 텍스트 값 가져오기

    storelist.append(element.findtext('aname2'))

    storelist.append(element.findtext('aname5'))

    storelist.append(element.findtext('aname7'))

    result.append(storelist)

MyPrettyPrinter().pprint(result) #결과리스트 한글로 출력하기