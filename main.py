
from tkinter import *
from tkinter import font
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk
import parsing
import renderImage
from random import*

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

    RenderText.delete(0, END)

    sText = InputEntry.get()
    s = []

   # 마트 검색 체크
    if var1.get() == 1 and var2.get() == 0:
        for item in parsing.martReq:
            if sText in item:
                print(item)
                RenderText.insert(END, item) 


    # 상품 검색 체크
    if var2.get() == 1 and var1.get() == 0:
        for item in parsing.goodsReq:
            if sText in item:
                print(item)
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

# 상품 이미지 관련 함수
def RenderGoodsImage():
    global goodsLabel
    goodsImg = PhotoImage(file="defaultGoodsImage.png").subsample(3)
    goodsLabel = Label(frame1, image=goodsImg)
    goodsLabel.image = goodsImg
    goodsLabel.pack()
    goodsLabel.place(x=15, y=125)

# 지도, 메일, 텔레그램 이미지 넣은 버튼 만드는 함수
def InitButton():
    mapImg = PhotoImage(file="map.png")
    Mapbtn = Button(frame1, image=mapImg)
    Mapbtn.image = mapImg
    Mapbtn.pack()
    Mapbtn.place(x=240, y=525)

    mailImg = PhotoImage(file="gmail.png").subsample(9, 9)
    Mailbtn = Button(frame1, image=mailImg,command=SendEmailTK)
    Mailbtn.image = mailImg
    Mailbtn.pack()
    Mailbtn.place(x=320, y=525)

    telegramImg = PhotoImage(file="telegram.png").subsample(4, 4)
    Telegrambtn = Button(frame1, image=telegramImg)
    Telegrambtn.image = telegramImg
    Telegrambtn.pack()
    Telegrambtn.place(x=387, y=525)

# 마트 선택 후 해당 마트에서 파는 상품 보여주는 곳
def InitRenderGMText():
    global RenderGMText

    gmframe = Frame(frame1)

    RenderGMTextYScrollbar = Scrollbar(gmframe)
    RenderGMTextYScrollbar.pack(side = RIGHT, fill = Y)

    TempFont = font.Font(gmframe, size=10, family='Consolas')
    RenderGMText = Listbox(gmframe, width=29, height=21, borderwidth=4, selectmode="extended", relief='ridge', yscrollcommand=RenderGMTextYScrollbar.set)
    RenderGMText.pack(side = LEFT)

    RenderGMTextYScrollbar['command'] = RenderGMText.yview
    RenderGMTextYScrollbar.pack(side=RIGHT, fill=BOTH)


    gmframe.pack()
    gmframe.place(x = 7, y = 250)

# 장바구니를 들고갈 마트 입력 Entry, 안내문 label
def InitInputMartEntry():
    global InputMartEntry

    TempFont = font.Font(frame1, size=12, weight='bold', family='Consolas')
    MainText = Label(frame1, font=TempFont, bg = BG_COLOR, text="판매점 이름을 입력하세요")
    MainText.pack()
    MainText.place(x=245, y=248)

    TempFont = font.Font(frame1, size=10, weight='bold', family='Consolas')
    InputMartEntry = Entry(frame1, font=TempFont, width=31, borderwidth=6, relief='ridge')
    InputMartEntry.pack()
    InputMartEntry.place(x=245, y=273)

# 장바구니 버튼
def InitSbskButton():
    TempFont = font.Font(frame1, size=10, weight='bold', family='Consolas')
    selectbtn = Button(frame1, width = 10, height=3, font=TempFont, text="판매점\n선택", command = SelectButtonAction)
    selectbtn.pack()
    selectbtn.place(x=330, y=305)

    sbskImg = PhotoImage(file="장바구니.png").subsample(2)
    sbskbtn = Button(frame1, image=sbskImg, command = BskButtonAction)
    sbskbtn.image = sbskImg
    sbskbtn.pack()
    sbskbtn.place(x=410, y=305)

# 사진 보기 버튼
def InitShowImageButton():
    TempFont = font.Font(frame1, size=10, weight='bold', family='Consolas')
    selectbtn = Button(frame1, width = 10, height=3, font=TempFont, text="사진\n보기", command = ImageButtonAction)
    selectbtn.pack()
    selectbtn.place(x=250, y=305)

# 판매점 선택 버튼 누르면 실행되는 함수 - 해당 판매점에서 판매하는 상품 조회
def SelectButtonAction():
    global RenderGMText
    global parsing
    global gmReq

    RenderGMText.delete(0, END)
#    temp = InputMartEntry.get()
    entpid = parsing.martNameId.get(InputMartEntry.get())
    print(entpid)
    gmServerUrl = "http://openapi.price.go.kr/openApiImpl/ProductPriceInfoService/getProductPriceInfoSvc.do?serviceKey="
    gmServerValue = "&goodInspectDay=" + "20210514" + "&entpId=" + parsing.urlencode(entpid)
    gmAreaData = parsing.openAPItoXML(gmServerUrl, parsing.serverKey, gmServerValue)
    gmReq = (parsing.getParsingGMData(gmAreaData, "iros.openapi.service.vo.goodPriceVO"))
    print(gmReq)
    if gmReq == []:
        RenderGMText.insert(END, "해당 판매점은 검색할 수 없습니다.")
        RenderGMText.insert(END, "다른 판매점을 선택해주세요!\n")
    for i in range(len(gmReq)):
        RenderGMText.insert(END, gmReq[i])

BskArr=[0]*10
BskArrnum=0
BskPriceArr=[0]*10
# 장바구니 버튼 누르면 실행되는 함수
def BskButtonAction():
    global gmReq, RenderGMText, parsing
    global inNum
    global BskArr,BskArrnum,BskPriceArr
    selected = RenderGMText.curselection()
    s = selected[0]
    selectedGoods = gmReq[s]
    selectedGoodsName = parsing.gmContentData[0][s]
    selectedGoodsPrice = int(parsing.gmContentData[1][s])
    
   
    
    BskArr.insert(BskArrnum,selectedGoodsName)
    BskPriceArr.insert(BskArrnum,selectedGoodsPrice)
    print(selectedGoods)
    print(selectedGoodsName)
    print(selectedGoodsPrice)
    inNum+=1
    BskArrnum+=1
    RenderBskText.insert(END, selectedGoods)
    MainGUI()


#-------------------------------------------------------------------------------------
#                           frame2
#-------------------------------------------------------------------------------------

def InitBskText():
    TempFont = font.Font(frame2, size=14, weight='bold', family='Consolas')
    MainText = Label(frame2, font=TempFont, text="[장바구니 리스트]", bg = BG_COLOR)
    MainText.pack()
    MainText.place(x=160, y=20)

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
    bskframe.place(x = 6, y = 60)

# 장바구니 내 품목 선택 삭제
def InitBskDelButton():
    TempFont = font.Font(frame2, size=12, weight='bold', family='Consolas')
    SearchButton = Button(frame2, font=TempFont,  text="해당 품목 삭제",command=deleteBskGoods)
    SearchButton.pack()
    SearchButton.place(x=200, y=250)
    

def deleteBskGoods():
    global RenderBskText
    global inNum
    global BskArr,BskArrnum

    selected = RenderBskText.curselection()
    delgoods = RenderBskText.index(selected[0])
    RenderBskText.delete(delgoods)
    inNum-=1
    #선택한거 배열에서  지우기
    BskArrnum-=1
    

width=450
height=200

counts=[0]*10
#10말고 장바구니안 상품개수만큼
class MainGUI:
    def displayhistogram(self):
        global gmReq, RenderGMText
        global RenderBskText
        global inNum
        global BskArr,BskArrnum,BskPriceArr
        self.canvas.delete('histogram')
        
        
        
        
        ch=inNum
        #counts[ch]=판매가격 가져오기
        counts[ch]=BskPriceArr[ch]
        barwidth=(width-20)/10
        maxcount=int(max(counts))
        for i in range(10):
            self.canvas.create_rectangle(10+i*barwidth, height-(height-10)*counts[i]/maxcount, 10+(i+1)*barwidth, height-10, tags='histogram')
            #text=상품이름
            self.canvas.create_text(20+i*barwidth+10,height-5,text=i+1,tags='histogram')
            #text=str(counts[i]) 말고 판매가격 
            self.canvas.create_text(20+i*barwidth+10,height-(height-10)*counts[i]/maxcount-5,text=BskPriceArr[i],tags='histogram')
            
    def __init__(self):
        
        self.canvas=Canvas(frame2,width=width,height=height,bg='white')
        self.canvas.pack()
        self.canvas.place(x=22.5,y=350)
        self.displayhistogram()
        
           



    


#-------------------------------------------------------------------------------------
#                          부가기능
#-------------------------------------------------------------------------------------

# 사진 보기 버튼 누르면 실행되는 함수
def ImageButtonAction():
    tofind = "오리온 초코파이"
    renderImage.MakeImage(tofind)
   
    imagew = Tk()
    imagew.title("Show Image")

    imagew.geometry('600x400')

    TempFont = font.Font(imagew, size=20, weight='bold', family='Consolas')
    MainText = Label(imagew, font=TempFont,text="{0}의 이미지".format(tofind))
    MainText.pack(side=TOP)
    #MainText.place(x=5)

    #newImageLabel = Label(imagew, width = 500, height = 350)
    # goodsImage = ImageTk.PhotoImage(Image.open("map.png"))
    # newImageLabel.configure(image=goodsImage)
    # newImageLabel.image = goodsImage

    # newImage.pack(side=LEFT)

    img = ImageTk.PhotoImage(Image.open("{0}.gif".format(tofind)))
    newImageLabel = Label(imagew, width = 500, height = 350, image = img)
    newImage.pack(side=LEFT)
    # newImageLabel.configure(image=img)
    # newImageLabel.image = img

    # goodsImage = ImageTk.PhotoImage(Image.open(file_name))
    # goodsLabel.configure(image=goodsImage)
    # goodsLabel.image = goodsImage

    imagew.mainloop()

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

    senderAddr = "dltnals5809@gmail.com" # 보내는 사람 email 주소.
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
    s.login("dltnals5809@gmail.com","비밀번호")
    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()


InitTopText()
parsing.getParsingAllData()
MartSearchCheckBox()
InitInputEntry()
InitSearchButton()
#RenderGoodsImage()
InitButton()
RenderSearchResultText()
InitRenderGMText()
InitInputMartEntry()
InitShowImageButton()
InitSbskButton()

InitBskText()
RenderBskText()
InitBskDelButton()



g_Tk.mainloop()
