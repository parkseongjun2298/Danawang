from tkinter import *
from tkinter import font
import tkinter.messagebox

g_Tk = Tk()
g_Tk.geometry("500x640+750+200")
DataList = []
var1 = IntVar()
var2 = IntVar()


def InitTopText():
    TempFont = font.Font(g_Tk, size=24, weight='bold', family='Consolas')
    MainText = Label(g_Tk, font=TempFont, text="[Danawang~]")
    MainText.pack()
    MainText.place(x=140)


def InitInputLabel():
    global InputLabel
    TempFont = font.Font(g_Tk, size=11, weight='bold', family='Consolas')
    InputLabel = Entry(g_Tk, font=TempFont, width=38, borderwidth=6, relief='ridge')
    InputLabel.pack()
    InputLabel.place(x=120, y=60)


def InitSearchButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family='Consolas')
    SearchButton = Button(g_Tk, font=TempFont, text="검색", command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=440, y=60)


def MartSearchCheckBox():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family='Consolas')
    chkbox = Checkbutton(g_Tk, font=TempFont, text='마트 검색', variable=var1, command=SearchMart)
    chkbox2 = Checkbutton(g_Tk, font=TempFont, text='상품 검색', variable=var2)
    chkbox.pack()
    chkbox2.pack()
    chkbox.place(x=26, y=60)
    chkbox2.place(x=26, y=90)


def SearchButtonAction():
    global SearchListBox

    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    iSearchIndex = SearchListBox.curselection()[0]
    if iSearchIndex == 0:
        SearchMart()
    elif iSearchIndex == 1:
        pass
    elif iSearchIndex == 2:
        pass
    elif iSearchIndex == 3:
        pass

    RenderText.configure(state='disabled')


def SearchMart():
    if var1.get() == True:
        import urllib
        import http.client
        conn = http.client.HTTPConnection("openapi.price.go.kr")
        conn.request("GET",
                     "/openApiImpl/ProductPriceInfoService/getProductPriceInfoSvc.do?serviceKey=%2BD2FzMpML7KBFXB2law50GJANbBLxxEO8U2hX1YsjNwaLBqoqG%2FsbsR6QiGzg5sk2nIa3kRWpljvOZVryafkcQ%3D%3D&goodInspectDay=20200508&entpId=100")
        req = conn.getresponse()
        global DataList
        DataList.clear()
        if req.status == 200:
            BooksDoc = req.read().decode('utf-8')
            if BooksDoc == None:
                print("에러")
            else:
                pass


def RenderGoodsImage():
    goodsImg = PhotoImage(file="defaultGoodsImage.png").subsample(3)
    goodsLabel = Label(g_Tk, image=goodsImg)
    goodsLabel.image = goodsImg
    goodsLabel.pack()
    goodsLabel.place(x=17, y=125)


def InitButton():
    mapImg = PhotoImage(file="map.png")
    Mapbtn = Button(g_Tk, image=mapImg)
    Mapbtn.image = mapImg
    Mapbtn.pack()
    Mapbtn.place(x=240, y=525)

    mailImg = PhotoImage(file="gmail.png").subsample(9, 9)
    Mailbtn = Button(g_Tk, image=mailImg)
    Mailbtn.image = mailImg
    Mailbtn.pack()
    Mailbtn.place(x=320, y=525)

    telegramImg = PhotoImage(file="telegram.png").subsample(4, 4)
    Telegrambtn = Button(g_Tk, image=telegramImg)
    Telegrambtn.image = telegramImg
    Telegrambtn.pack()
    Telegrambtn.place(x=387, y=525)


def SearchResultRenderText():
    global RenderText

    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText = Text(g_Tk, width=50, height=11, borderwidth=6, relief='ridge')
    RenderText.pack()
    RenderText.place(x=121, y=95)

    RenderText.configure(state='disabled')


def InitRenderText():
    global RenderText

    RenderTextScrollbar = Scrollbar(g_Tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=375, y=200)

    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText = Text(g_Tk, width=30, height=28, borderwidth=6, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=10, y=252)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

    RenderText.configure(state='disabled')


def InitInputMartLabel():
    global InputMartLabel

    TempFont = font.Font(g_Tk, size=12, weight='bold', family='Consolas')
    MainText = Label(g_Tk, font=TempFont, text="판매점 이름을 입력하세요")
    MainText.pack()
    MainText.place(x=245, y=252)

    TempFont = font.Font(g_Tk, size=10, weight='bold', family='Consolas')
    InputMartLabel = Entry(g_Tk, font=TempFont, width=31, borderwidth=6, relief='ridge')
    InputMartLabel.pack()
    InputMartLabel.place(x=245, y=273)


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


InitTopText()
MartSearchCheckBox()
SearchMart()
InitInputLabel()
InitSearchButton()
RenderGoodsImage()
InitButton()
SearchResultRenderText()
InitRenderText()
InitInputMartLabel()
InitSbskButton()

g_Tk.mainloop()
