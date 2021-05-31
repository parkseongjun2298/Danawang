
from tkinter import *
from tkinter import font
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk
import parsing
import renderImage
from random import*
import smtplib
import pickle

from email.mime.text import MIMEText
from selenium import webdriver
from bs4 import BeautifulSoup as soups

import threading
import sys
import folium
from cefpython3 import cefpython as cef

BG_COLOR = 'light blue'

g_Tk = Tk()
g_Tk.geometry("505x640+750+200")
g_Tk.title("DANAWANG")
g_Tk['bg'] = BG_COLOR

var1 = IntVar()
var2 = IntVar()

notebook = tkinter.ttk.Notebook(g_Tk, width = 505, height = 600)
style = ttk.Style()
style.theme_create("yummy", parent = "alt", settings={
    "TNotebook" : {"configure" :{"tabmargins": [2, 5, 2, 0], "background" : BG_COLOR } },
        "TNotebook.Tab": {
            "configure": {"padding": [5, 1], "background": "SteelBlue1" },
            "map":       {"background": [("selected", "RoyalBlue1")],
                          "expand": [("selected", [1, 1, 1, 0])] } } } )

style.theme_use("yummy")

note = ttk.Notebook(g_Tk)

frame1 = ttk.Frame(note, width=505, height=500, style = "TNotebook")
note.add(frame1, text="메인")

frame2 = ttk.Frame(note, width=505, height=500, style = "TNotebook")
note.add(frame2, text="장바구니")

note.pack(expand=1, fill=BOTH, padx=5, pady=5)

global inNum
inNum=-1

#notebook['background'] = 'royalblue'
#notebook.pack(side=BOTTOM)

# frame1 = Frame(g_Tk)
# frame1['bg'] = BG_COLOR
# notebook.add(frame1, text="메인")

# frame2 = Frame(g_Tk)
# notebook.add(frame2, text="장바구니")

# DANAWANG~ text 함수
def InitTopText():
    TempFont = font.Font(g_Tk, size=24, weight='bold', family='Consolas')
    MainText = Label(g_Tk, font=TempFont, text="[Danawang~]", bg = BG_COLOR)
    MainText.pack()
    MainText.place(x=160)

# 검색 버튼
def InitSearchButton():
    TempFont = font.Font(frame1, size=12, weight='bold', family='Consolas')
    SearchButton = Button(frame1, font=TempFont, text="검색", command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=440, y=60)

# 마트/상품 검색 버튼
def MartSearchCheckBox():
    TempFont = font.Font(frame1, size=11, weight='bold', family='Consolas')
    chkbox = Checkbutton(frame1, font=TempFont, bg = BG_COLOR, text='마트 검색', variable=var1)
    chkbox2 = Checkbutton(frame1, font=TempFont, bg = BG_COLOR, text='상품 검색', variable=var2)
    chkbox.pack()
    chkbox2.pack()
    chkbox.place(x=20, y=45)
    chkbox2.place(x=20, y=70)

# 마트/상품 검색 Entry
def InitInputEntry():
    global InputEntry
    TempFont = font.Font(frame1, size=11, weight='bold', family='Consolas')
    InputEntry = Entry(frame1, font=TempFont, width=38, borderwidth=6, relief='ridge')
    InputEntry.pack()
    InputEntry.place(x=120, y=60)

# 마트/상품 검색 시 실행되는 함수
def SearchButtonAction():
    global RenderText
    global parsing
    global martSelectedData, goodsSelectedData

    RenderText.delete(0, END)

    sText = InputEntry.get()
    s = []
    martSelectedData = [[] for i in range(6)]
    goodsSelectedData = []

   # 마트 검색 체크
    if var1.get() == 1 and var2.get() == 0:
        for i in range(len(parsing.martContentData[0])):
            if sText in parsing.martContentData[0][i] or sText in parsing.martContentData[1][i]:
                martSelectedData[0].append(parsing.martContentData[0][i])
                martSelectedData[1].append(parsing.martContentData[1][i])
                martSelectedData[2].append(parsing.martContentData[2][i])
                martSelectedData[3].append(parsing.martContentData[3][i])
                martSelectedData[4].append(parsing.martContentData[4][i])
                martSelectedData[5].append(parsing.martContentData[5][i])
                textMessage = str(parsing.martContentData[0][i] + " : " + parsing.martContentData[1][i] + " (" + parsing.martContentData[3][i] + ")\n")
                RenderText.insert(END, textMessage) 


    # 상품 검색 체크
    if var2.get() == 1 and var1.get() == 0:
        for item in parsing.goodsContentData[0]:
            if sText in item:
                goodsSelectedData.append(item)
                RenderText.insert(END, item) 

# 마트/상품 검색한 것 보여주는 함수
def RenderSearchResultText():
    global RenderText

    rframe = Frame(frame1)

    RenderTextYScrollbar = Scrollbar(rframe)
    RenderTextYScrollbar.pack(side = RIGHT, fill = Y)

    TempFont = font.Font(rframe, size=10, family='Consolas')
    RenderText = Listbox(rframe, width=65, height=9, borderwidth=4, relief='ridge', yscrollcommand=RenderTextYScrollbar.set)
    RenderText.pack(side = TOP)

    RenderTextYScrollbar['command'] = RenderText.yview
    RenderTextYScrollbar.pack(side=RIGHT, fill=BOTH)

    rframe.pack()
    rframe.place(x = 10, y = 95)

# 마트 선택 후 해당 마트에서 파는 상품 보여주는 곳
def InitRenderGMText():
    global RenderGMText

    gmframe = Frame(frame1)

    RenderGMTextYScrollbar = Scrollbar(gmframe)
    RenderGMTextYScrollbar.pack(side = RIGHT, fill = Y)

    TempFont = font.Font(gmframe, size=10, family='Consolas')
    RenderGMText = Listbox(gmframe, width=32, height=21, borderwidth=4, selectmode="extended", relief='ridge', yscrollcommand=RenderGMTextYScrollbar.set)
    RenderGMText.pack(side = LEFT)

    RenderGMTextYScrollbar['command'] = RenderGMText.yview
    RenderGMTextYScrollbar.pack(side=RIGHT, fill=BOTH)


    gmframe.pack()
    gmframe.place(x = 7, y = 250)

# 사진 보기 버튼
def InitShowImageButton():
    TempFont = font.Font(frame1, size=12, weight='bold', family='Consolas')
    selectbtn = Button(frame1, width = 11, height=2, font=TempFont, text="사진보기", command = ImageButtonAction)
    selectbtn.pack()
    selectbtn.place(x=265, y=260)

# 장바구니 버튼
def InitSbskButton():
    TempFont = font.Font(frame1, size=12, weight='bold', family='Consolas')
    selectbtn = Button(frame1, width = 11, height=2, font=TempFont, text="판매점선택", command = SelectButtonAction)
    selectbtn.pack()
    selectbtn.place(x=380, y=260)

    TempFont = font.Font(frame1, size=12, weight='bold', family='Consolas')
    sbskbtn = Button(frame1, width=11, height=3, font = TempFont, text="장바구니담기!", command = BskButtonAction)
    sbskbtn.pack()
    sbskbtn.place(x=265, y=320)

    # 지도 버튼 생성
def InitMapButton():
    mapImg = PhotoImage(file="image/지도.png").subsample(5, 8)
    Mapbtn = Button(frame1, image=mapImg, command = MapButtonAction)
    Mapbtn.image = mapImg
    Mapbtn.pack()
    Mapbtn.place(x=380, y= 320)

# 판매점 선택 버튼 누르면 실행되는 함수 - 해당 판매점에서 판매하는 상품 조회
def SelectButtonAction():
    global RenderGMText, RenderText, gmReq, entpname, martSelectedData
    global parsing

    selected = RenderText.curselection()
    s = selected[0]
    entpid = martSelectedData[2][s]
    entpname = martSelectedData[0][s]
    print(entpid, entpname)

    RenderGMText.delete(0, END)
    # temp = InputMartEntry.get()
    # entpid = parsing.martNameId.get(entpid)
    # print(entpid)
    gmServerUrl = "http://openapi.price.go.kr/openApiImpl/ProductPriceInfoService/getProductPriceInfoSvc.do?serviceKey="
    gmServerValue = "&goodInspectDay=" + "20210514" + "&entpId=" + parsing.urlencode(entpid)
    gmAreaData = parsing.openAPItoXML(gmServerUrl, parsing.serverKey, gmServerValue)
    gmReq = (parsing.getParsingGMData(gmAreaData, "iros.openapi.service.vo.goodPriceVO"))
    #print(gmReq)
    if gmReq == []:
        tkinter.messagebox.showinfo("sorry,,", "해당 판매점의 상품 판매 정보가 없어요!\n다른 판매점을 선택해주세요!\n")
    for i in range(len(gmReq)):
        RenderGMText.insert(END, gmReq[i])

BskArr=[]
BskArrnum = 0
BskPriceArr=[]

# 장바구니 버튼 누르면 실행되는 함수
def BskButtonAction():
    global gmReq, RenderGMText, parsing
    global inNum
    global BskArr,BskArrnum,BskPriceArr, selectedGoodsName, selectedGoodsPrice

    selected = RenderGMText.curselection()
    s = selected[0]
    selectedGoods = gmReq[s]
    selectedGoodsName = parsing.gmContentData[0][s]
    selectedGoodsPrice = int(parsing.gmContentData[1][s])
    
    BskArr.append(selectedGoodsName)
    BskPriceArr.append(selectedGoodsPrice)
    print(selectedGoods)
    print(selectedGoodsName)
    print(selectedGoodsPrice)
    inNum+=1
    BskArrnum+=1
    RenderBskText.insert(END, selectedGoods)
    HistogramGui()


#-------------------------------------------------------------------------------------
#                           frame2
#-------------------------------------------------------------------------------------

def InitBskText():
    TempFont = font.Font(frame2, size=13, weight='bold', family='Consolas')
    MainText = Label(frame2, font=TempFont, text="<장바구니 리스트>", bg = BG_COLOR)
    MainText.pack()
    MainText.place(x=170, y=20)

def RenderBskText():
    global RenderBskText
    bskframe = Frame(frame2)

    RenderBskTextYScrollbar = Scrollbar(bskframe)
    RenderBskTextYScrollbar.pack(side = RIGHT, fill = Y)

    TempFont = font.Font(bskframe, size=10, family='Consolas')
    RenderBskText = Listbox(bskframe, width=65, height=12, borderwidth=4, relief='ridge', yscrollcommand=RenderBskTextYScrollbar.set)
    RenderBskText.pack(side = TOP)

    RenderBskTextYScrollbar['command'] = RenderBskText.yview
    RenderBskTextYScrollbar.pack(side=RIGHT, fill=BOTH)

    bskframe.pack()
    bskframe.place(x = 6, y = 45)

c_width=450
c_height=230

counts=[]
        
def HistogramGui():
    canvas = Canvas(frame2, width = c_width, height = c_height, bg = BG_COLOR)
    canvas.pack()
    canvas.place(x = 22.5, y = 350)

    TempFont = font.Font(frame2, size=12, weight='bold', family='Consolas')
    HgramText = Label(frame2, font=TempFont, text="[장바구니 내 상품 가격]", bg = BG_COLOR)
    HgramText.pack()
    HgramText.place(x=160, y=335)

    y_stretch = 4
    y_gap = 10
    x_stretch = 10
    x_width = 30
    x_gap = 20

    print(BskPriceArr)

    for x, y in enumerate(BskPriceArr):
        # calculate reactangle coordinates
        x0 = x * x_stretch + x * x_width + x_gap
        y0 = c_height - (y / 300 * y_stretch + y_gap)
        x1 = x * x_stretch + x * x_width + x_width + x_gap
        y1 = c_height - y_gap
        # Here we draw the bar
        canvas.create_rectangle(x0, y0, x1, y1, fill="RoyalBlue1")
        canvas.create_text(x0+2, y0, anchor=SW, text=str(y))
        canvas.create_text(x0+2, y1+15, anchor=SW, text=str(x+1))
           
# 장바구니 내 품목 선택 삭제
def InitBskDelButton():
    TempFont = font.Font(frame2, size=12, weight='bold', family='Consolas')
    SearchButton = Button(frame2, font=TempFont, width = 12, height = 3, text="해당 품목 삭제",command=deleteBskGoods)
    SearchButton.pack()
    SearchButton.place(x=30, y=260)
    

def deleteBskGoods():
    global RenderBskText
    global inNum
    global BskArr, BskPriceArr, BskArrnum, selectedGoodsName, selectedGoodsPrice

    selected = RenderBskText.curselection()
    s = selected[0]
    delgoods = RenderBskText.index(selected[0])

    inNum-=1
    BskArrnum-=1
    del BskArr[s]
    del BskPriceArr[s]

    RenderBskText.delete(delgoods)

    HistogramGui()

def InitMailgramButton():
    mailImg = PhotoImage(file="image/gmail.png").subsample(5,8)
    Mailbtn = Button(frame2, image=mailImg,command=SendEmailTK)
    Mailbtn.image = mailImg
    Mailbtn.pack()
    Mailbtn.place(x=190, y=260)

    telegramImg = PhotoImage(file="image/텔레그램.png").subsample(3, 2)
    Telegrambtn = Button(frame2, image=telegramImg)
    Telegrambtn.image = telegramImg
    Telegrambtn.pack()
    Telegrambtn.place(x=330, y=260)           

#-------------------------------------------------------------------------------------
#                          부가기능
#-------------------------------------------------------------------------------------

# 사진 보기 버튼 누르면 실행되는 함수
def ImageButtonAction():
    global RenderText, RenderGMText, parsing, goodsSelectedData
    rts = RenderText.curselection()
    gms = RenderGMText.curselection()
    tofind = ""
    if len(gms) != 0:   # 마트 내 상품 선택 시
        tofind = parsing.gmContentData[0][gms[0]]
    if len(rts) != 0:   # 상품 검색시
        tofind = goodsSelectedData[rts[0]]

    print(tofind)

    #renderImage.MakeImage(tofind)

    search_name = tofind
    search_path = "Your Path"
    search_selenium(search_name, search_path)
    
    img = PhotoImage(file="./img/0.png").zoom(2)
    ImageLabel = Label(frame1, width = 130, height = 130, image = img, bg = BG_COLOR)
    ImageLabel.image = img
    ImageLabel.pack()
    ImageLabel.place(x=300, y=400)

def search_selenium(search_name, search_path):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument('disable-gpu')
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")


    search_url = "https://www.google.com/search?q=" + str(search_name) + "&hl=ko&tbm=isch"

    browser = webdriver.Chrome('chromedriver.exe', options=options)
    browser.get(search_url)

    image_count = len(browser.find_elements_by_tag_name("img"))

    browser.implicitly_wait(2)

    image = browser.find_elements_by_tag_name("img")[0]
    image.screenshot("./img/0.png")

    browser.close()
    

#이메일창 띄우는 함수
def SendEmailTK():
    nw = Tk()
    nw.title("Send Email")

    nw.geometry('300x150+400+300')

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
    global BskArr,BskArrnum,BskPriceArr, entpname
    GetEmailLabel=EmailLabel.get()

    # global value
    host = "smtp.gmail.com"  # Gmail STMP 서버 주소.
    port = "587"
    #htmlFileName = "totalGoodsInfo.xml"

    senderAddr = "dltnals5809@gmail.com" # 보내는 사람 email 주소.
    recipientAddr =GetEmailLabel  # 받는 사람 email 주소.

    Gmailtext=""

    Gmailtext += str("<" + entpname + ">에서 담은 장바구니 내역입니다.\n\n")
    for i in range(len(BskArr)):
        Gmailtext += str("[{0}] {1} : {2}원\n".format(i+1, BskArr[i], BskPriceArr[i]))

    #msg = MIMEBase("multipart", "alternative")
    msg = MIMEText(Gmailtext)
    msg['Subject'] = "장바구니 내용"
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    print(msg)

    # 메일을 발송한다.
    s = mysmtplib.MySMTP(host, port)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("dltnals5809@gmail.com", pickle.load(open("userpw.plk", "rb")))

    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()

# 지도 관련 함수들

def MapButtonAction():
    global martSelectedData, mapFrame

    mapWindow = Toplevel()
    mapFrame = Frame(mapWindow, width=800, height = 600)
    mapFrame.pack()


    selected = RenderText.curselection()
    s = selected[0]
    martname = martSelectedData[0][s]
    latitude = martSelectedData[4][s]
    longtitude = martSelectedData[5][s]

    if latitude == "위도 정보 없음" and longtitude == "경도 정보 없음":
        tkinter.messagebox.showinfo("sorry,,","위도 경도 정보가 없어요!\n다른 판매점을 선택해주세요!\n")
        mapWindow.destroy()
    else:
        Pressed(martname, latitude, longtitude)

    mapWindow.mainloop()

# cef모듈로 브라우저 실행
def showMap(frame):
    sys.excepthook = cef.ExceptHook
    window_info = cef.WindowInfo(frame.winfo_id())
    window_info.SetAsChild(frame.winfo_id(), [0,0,800,600])
    cef.Initialize()
    browser = cef.CreateBrowserSync(window_info, url='file:///map.html')
    cef.MessageLoop()


def Pressed(martname, latitude, longtitude):
    # 지도 저장
    # 위도 경도 지정
    global martSelectedData, mapFrame

    m = folium.Map(location=[latitude, longtitude], zoom_start=13)
    # 마커 지정
    folium.Marker([latitude, longtitude], popup=martname).add_to(m)
    # html 파일로 저장
    m.save('map.html')

    # 브라우저를 위한 쓰레드 생성
    thread = threading.Thread(target=showMap, args=(mapFrame,))
    thread.daemon = True
    thread.start()

InitTopText()
parsing.getParsingAllData()
MartSearchCheckBox()
InitInputEntry()
InitSearchButton()
#RenderGoodsImage()
InitMapButton()
RenderSearchResultText()
InitRenderGMText()
InitShowImageButton()
InitSbskButton()

InitBskText()
RenderBskText()
InitBskDelButton()
InitMailgramButton()


g_Tk.mainloop()
