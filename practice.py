import urllib.request
from urllib.parse import urlencode, quote_plus, unquote
import xml.etree.ElementTree as ET

decode_key = unquote("bsE5AeiHGFzKvS7n2oM6rZ8IQEOVLh/O8gKrORcpl3fl2ut8D2TfLcTIbYTmwFOvj3tCfdUBxigtsKCz16bNwA==")
#print(decode_key)

url = "http://openapi.price.go.kr/openApiImpl/ProductPriceInfoService/getStoreInfoSvc.do?ServiceKey="

queryParams = '?' + urlencode({ quote_plus('ServiceKey') : decode_key,
	# quote_plus('goodInspectDay') : '20100205',
	# quote_plus('entpId') : '100'	
		})

0 
#pagenum = '1'
req = urllib.request
body = req.urlopen(url + queryParams)
req.get_method = lambda : 'GET'
response_body = body.read()
print(response_body.decode('utf-8'))

#tree = elemTree.parse('totalGoosInfo.xml')
# goodsList = []
# for n in range(1, 10):
# 	pagenum = str(n)
# 	queryParams = '?' + urlencode({ quote_plus('ServiceKey') : decode_key,
# 	#quote_plus('goodId') : 335	
# 		})
# 	print(queryParams)
# 	body = req.urlopen(url + queryParams)
# 	req.get_method = lambda : 'GET'
# 	response_body = body.read()
# 	result = response_body.decode('utf-8')

# 	tree = ET.ElementTree(ET.fromstring(result))
# 	note = tree.getroot()

# 	for i in note.iter("goodId"):
# 		dog_place = i.text
# 		if '(' in dog_place:
# 			addrList.append(dog_place)
# 			print(addrList)
