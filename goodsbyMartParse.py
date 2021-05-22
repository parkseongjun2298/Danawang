import urllib.request
from urllib.parse import urlencode, quote_plus, unquote
import xml.etree.ElementTree as ET
from main import selectMart

decode_key = unquote("bsE5AeiHGFzKvS7n2oM6rZ8IQEOVLh/O8gKrORcpl3fl2ut8D2TfLcTIbYTmwFOvj3tCfdUBxigtsKCz16bNwA==")

url = "http://openapi.price.go.kr/openApiImpl/ProductPriceInfoService/getProductPriceInfoSvc.do"

for 

queryParams = '?' + urlencode({ quote_plus('ServiceKey') : decode_key,
	quote_plus('goodInspectDay') : '20210521',
	quote_plus('entpId') : selectMart
		})

0 
#pagenum = '1'
req = urllib.request
body = req.urlopen(url + queryParams)
req.get_method = lambda : 'GET'
response_body = body.read()
print(response_body.decode('utf-8'))