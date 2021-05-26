from xml.dom.minidom import *
import urllib.request
import requests

serverKey = "bsE5AeiHGFzKvS7n2oM6rZ8IQEOVLh/O8gKrORcpl3fl2ut8D2TfLcTIbYTmwFOvj3tCfdUBxigtsKCz16bNwA=="

def base64_Encode(s):
    return base64.b64encode(s.encode('utf-8'))

def Base64_Decode(b):
    return base64.b64decode(b).decode('utf-8')

def urlencode(string):
    return urllib.parse.quote(string)

def urldecode(string):
    return urllib.parse.quote(string)

def openAPItoXML(server, key, value):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')]
    # ↑ User-Agent를 입력하지 않을경우 naver.com 에서 정상적인 접근이 아닌것으로 판단하여 차단을 한다.
    data = ""
    urlData = server + key + value
    with opener.open(urlData) as f:
        data = f.read(10000000).decode('utf-8') # 300000bytes 를 utf-8로 변환하여 읽어온다.  변환이 없을경우 unicode로 받아온다.
    return data

# 상픔 정보 파싱
def getParsingGoodsData(xmlData, motherData):
    doc = parseString(xmlData)
    goodsList = doc.getElementsByTagName(motherData)
    goodsSize = len(goodsList)
    goodslist = []
    global goodsContentData, goodsNameId
    goodsContentData = []
    goodsNameId = {}

    for index in range(goodsSize):
        mphmsName = goodsList[index].getElementsByTagName("goodName")
        mphmsId = goodsList[index].getElementsByTagName("goodId")
        goodsNameId[mphmsName[0].firstChild.data] = mphmsId[0].firstChild.data
        goodslist.append(str(mphmsName[0].firstChild.data + " (" + mphmsId[0].firstChild.data + ")"))
        goodsContentData.append([str(mphmsName[0].firstChild.data), str(mphmsId[0].firstChild.data)])
    return goodslist

# 판매점 정보 파싱
def getParsingMartData(xmlData, motherData):
    doc = parseString(xmlData)
    MartList = doc.getElementsByTagName(motherData)
    MartSize = len(MartList)
    martlist = []
    global martContentData, martNameId
    martContentData = ""
    martNameId = {}

    for index in range(MartSize):
        mphmsName = MartList[index].getElementsByTagName("entpName")
        mphmsAddr = MartList[index].getElementsByTagName("plmkAddrBasic")
        mphmsId = MartList[index].getElementsByTagName("entpId")
        martlist.append(str(mphmsName[0].firstChild.data + " (" + mphmsAddr[0].firstChild.data + ")" + " (" + mphmsId[0].firstChild.data + ")"))
        martNameId[mphmsName[0].firstChild.data] = mphmsId[0].firstChild.data
        martContentData += str(mphmsName[0].firstChild.data)
        martContentData += str(mphmsAddr[0].firstChild.data)
        martContentData += str(mphmsId[0].firstChild.data)
      
    return martlist

# 판매점 내 상품 정보 파싱



def getParsingGMData(xmlData, motherData):
    global goodsContentData, gmContentData
    doc = parseString(xmlData)
    gmList = doc.getElementsByTagName(motherData)
    gmSize = len(gmList)
    gmlist = []
    gmContentData = [[] for i in range(2)]

    for index in range(gmSize):
        mphmsId = gmList[index].getElementsByTagName("goodId")
        mphmsPrice = gmList[index].getElementsByTagName("goodPrice")
        for goods in goodsContentData:
            if mphmsId[0].firstChild.data in goods:
                gmName = str(goods[0])

        gmlist.append(str(gmName + " : " + mphmsPrice[0].firstChild.data + "원"))
        gmContentData[0].append(gmName)
        gmContentData[1].append(mphmsPrice[0].firstChild.data)

    return gmlist




def getParsingAllData():
    global goodsReq, martReq

    goodsServerUrl = "http://openapi.price.go.kr/openApiImpl/ProductPriceInfoService/getProductInfoSvc.do?ServiceKey="
    goodsServerValue = ""
    goodsAreaData = openAPItoXML(goodsServerUrl, serverKey, goodsServerValue)
    goodsReq = (getParsingGoodsData(goodsAreaData, "item"))

    MartServerUrl = "http://openapi.price.go.kr/openApiImpl/ProductPriceInfoService/getStoreInfoSvc.do?ServiceKey="
    MartServerValue = ""
    MartAreaData = openAPItoXML(MartServerUrl, serverKey, MartServerValue)
    martReq = (getParsingMartData(MartAreaData, "iros.openapi.service.vo.entpInfoVO"))
