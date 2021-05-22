from tkinter import *
from tkinter import font
import tkinter.messagebox
from xml.dom.minidom import *
import urllib.request

BG_COLOR = 'light blue'

g_Tk = Tk()
g_Tk.geometry("505x640+750+200")
g_Tk.title("DANAWANG")
g_Tk['bg'] = BG_COLOR

var1 = IntVar()
var2 = IntVar()
searchText = StringVar()

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
        data = f.read(3000000).decode('utf-8') # 300000bytes 를 utf-8로 변환하여 읽어온다.  변환이 없을경우 unicode로 받아온다.
    return data

def getParsingGoodsData(xmlData, motherData):
    doc = parseString(xmlData)
    goodsList = doc.getElementsByTagName(motherData)
    goodsSize = len(goodsList)
    list = []
    global ContentData
    ContentData = ""

    for index in range(goodsSize):
        mphms = goodsList[index].getElementsByTagName("goodName")
        list.append(str("상품명 : " + mphms[0].firstChild.data))
        ContentData += str("상품명 : " + mphms[0].firstChild.data) + str('\n')
    return list

def getParsingMartData(xmlData, motherData):
    doc = parseString(xmlData)
    MartList = doc.getElementsByTagName(motherData)
    MartSize = len(goodsList)
    list = []
    global ContentData
    ContentData = ""

    # for index in range(goodsSize):
    #     mphms = MartList[index].getElementsByTagName("goodName")
    #     list.append(str("상품명 : " + mphms[0].firstChild.data))
    #     ContentData += str("상품명 : " + mphms[0].firstChild.data) + str('\n')
    # return list

# DANAWANG~ text 함수
def InitTopText():
    TempFont = font.Font(g_Tk, size=24, weight='bold', family='Consolas')
    MainText = Label(g_Tk, font=TempFont, text="[Danawang~]", bg = BG_COLOR)
    MainText.pack()
    MainText.place(x=160)

# 검색 버튼
def InitSearchButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family='Consolas')
    SearchButton = Button(g_Tk, font=TempFont, text="검색", command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=440, y=60)

# 마트/상품 검색 버튼
def MartSearchCheckBox():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family='Consolas')
    chkbox = Checkbutton(g_Tk, font=TempFont, bg = BG_COLOR, text='마트 검색', variable=var1)
    chkbox2 = Checkbutton(g_Tk, font=TempFont, bg = BG_COLOR, text='상품 검색', variable=var2)
    chkbox.pack()
    chkbox2.pack()
    chkbox.place(x=26, y=60)
    chkbox2.place(x=26, y=90)

# 마트/상품 검색 Entry
def InitInputEntry():
    global InputEntry
    TempFont = font.Font(g_Tk, size=11, weight='bold', family='Consolas')
    InputEntry = Entry(g_Tk, font=TempFont, width=38, borderwidth=6, relief='ridge')
    InputEntry.pack()
    InputEntry.place(x=120, y=60)

# 마트/상품 검색 시 실행되는 함수
def SearchButtonAction():
    global RenderText

    sText = InputEntry.get()
    s = []

    goodsServerUrl = "http://openapi.price.go.kr/openApiImpl/ProductPriceInfoService/getProductInfoSvc.do?ServiceKey="
    goodsServerValue = ""
    goodsAreaData = openAPItoXML(goodsServerUrl, serverKey, goodsServerValue)
    req = (getParsingGoodsData(goodsAreaData, "item"))

    # 마트 검색 체크
    if var1.get() == 1 and var2.get() == 0:
        pass
        # for child in martRoot:
        #     if sText in child[1].text:
        #         s = searchText.get()
        #         s += child[1].text

        #         RenderText.insert(INSERT,child[1].text)
        #         print(child[1].text)
        #     searchText.set(s)



    # 상품 검색 체크
    if var2.get() == 1 and var1.get() == 0:
        for item in req:
            if sText in item:
                s = searchText.get()
                s += item
                print(item)
                searchText.set(s)        
        # for child in goodsRoot:
        #     if sText in child[1].text:
        #         RenderText.insert(INSERT, child[1].text)
        #         print(child[1].text)


    #SearchResultRenderText()

# 마트/상품 검색한 것 보여주는 함수
def SearchResultRenderText():
    global RenderText

    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText = Label(g_Tk, width=50, height=9, borderwidth=6)
    RenderText.pack()
    RenderText.place(x=121, y=95)
    RenderText.configure(state='disabled')



# 상품 이미지 관련 함수
def RenderGoodsImage():
    goodsImg = PhotoImage(file="defaultGoodsImage.png").subsample(3)
    goodsLabel = Label(g_Tk, image=goodsImg)
    goodsLabel.image = goodsImg
    goodsLabel.pack()
    goodsLabel.place(x=15, y=125)

# 지도, 메일, 텔레그램 이미지 넣은 버튼 만드는 함수

def InitButton():
    mapImg = PhotoImage(file="map.png")
    Mapbtn = Button(g_Tk, image=mapImg)
    Mapbtn.image = mapImg
    Mapbtn.pack()
    Mapbtn.place(x=240, y=525)

    mailImg = PhotoImage(file="gmail.png").subsample(9, 9)
    Mailbtn = Button(g_Tk, image=mailImg,command=SendEmailTK)
    Mailbtn.image = mailImg
    Mailbtn.pack()
    Mailbtn.place(x=320, y=525)

    telegramImg = PhotoImage(file="telegram.png").subsample(4, 4)
    Telegrambtn = Button(g_Tk, image=telegramImg)
    Telegrambtn.image = telegramImg
    Telegrambtn.pack()
    Telegrambtn.place(x=387, y=525)

# 마트 선택 후 해당 마트에서 파는 상품 보여주는 곳
def InitRenderMartText():
    global RenderMartText

    frame = Frame(g_Tk)

    RenderMartTextScrollbar = Scrollbar(frame)
    RenderMartTextScrollbar.pack(side = RIGHT, fill = Y)

    TempFont = font.Font(frame, size=10, family='Consolas')
    RenderMartText = Listbox(frame, width=28, height=23, borderwidth=6, relief='ridge', yscrollcommand=RenderMartTextScrollbar.set)
    RenderMartText.pack(side = LEFT)

    RenderMartTextScrollbar['command'] = RenderMartText.yview
    RenderMartTextScrollbar.pack(side=RIGHT, fill=BOTH)

    frame.pack()
    frame.place(x = 10, y = 252)

# 장바구니를 들고갈 마트 입력 Entry, 안내문 label
def InitInputMartEntry():
    global InputMartEntry

    TempFont = font.Font(g_Tk, size=12, weight='bold', family='Consolas')
    MainText = Label(g_Tk, font=TempFont, bg = BG_COLOR, text="판매점 이름을 입력하세요")
    MainText.pack()
    MainText.place(x=245, y=252)

    TempFont = font.Font(g_Tk, size=10, weight='bold', family='Consolas')
    InputMartEntry = Entry(g_Tk, font=TempFont, width=31, borderwidth=6, relief='ridge')
    InputMartEntry.pack()
    InputMartEntry.place(x=245, y=273)

# 장바구니 버튼
def InitSbskButton():
    TempFont = font.Font(g_Tk, size=13, weight='bold', family='Consolas')
    selectbtn = Button(g_Tk, width = 16, font=TempFont, text="판매점 선택")
    selectbtn.pack()
    selectbtn.place(x=245, y=305)

    sbskImg = PhotoImage(file="장바구니.png").subsample(2)
    sbskbtn = Button(g_Tk, image=sbskImg)
    sbskbtn.image = sbskImg
    sbskbtn.pack()
    sbskbtn.place(x=410, y=305)

#이메일창 띄우는 함수
def SendEmailTK():
    nw = Tk()
    nw.title("Send Email")

    nw.geometry('300x300+300+100')

    TempFont = font.Font(nw, size=20, weight='bold', family='Consolas')
    MainText = Label(nw, font=TempFont,text="이메일을 입력하시오!!")
    MainText.pack()
    MainText.place(x=5)

    global EmailLabel
    TempFont = font.Font(nw, size=15, weight='bold', family='Consolas')
    EmailLabel = Entry(nw, font=TempFont, width=20, borderwidth=6, relief='ridge')
    EmailLabel.pack()
    EmailLabel.place(x=5, y=35)

    TempFont = font.Font(nw, size=12, weight='bold', family='Consolas')
    SearchButton = Button(nw, font=TempFont,  text="발송",command=SendEmail)
    SearchButton.pack()
    SearchButton.place(x=250, y=35)

    nw.mainloop()

#이메일 보내는 함수
def SendEmail():
    import mimetypes
    import mysmtplib
    from email.mime.base import MIMEBase
    from email.mime.text import MIMEText
    GetEmailLabel=EmailLabel.get()

    # global value
    host = "smtp.gmail.com"  # Gmail STMP 서버 주소.
    port = "587"
    htmlFileName = "totalGoodsInfo.xml"

    senderAddr = "bout3298@gmail.com" # 보내는 사람 email 주소.
    recipientAddr =GetEmailLabel  # 받는 사람 email 주소.

    msg = MIMEBase("multipart", "alternative")
    msg['Subject'] = "장바구니 내용"
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    # MIME 문서를 생성합니다.
    htmlFD = open(htmlFileName, 'rb')
    HtmlPart = MIMEText(htmlFD.read(), 'html', _charset='UTF-8')
    htmlFD.close()

    # 만들었던 mime을 MIMEBase에 첨부 시킨다.
    msg.attach(HtmlPart)

    # 메일을 발송한다.
    s = mysmtplib.MySMTP(host, port)
    # s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("bout3298@gmail.com","jj357741")
    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()


InitTopText()
MartSearchCheckBox()
InitInputEntry()
InitSearchButton()
RenderGoodsImage()
InitButton()
SearchResultRenderText()
InitRenderMartText()
InitInputMartEntry()
InitSbskButton()

g_Tk.mainloop()
