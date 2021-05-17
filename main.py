from tkinter import *
from tkinter import font
import tkinter.messagebox
from PIL import ImageTk, Image

g_Tk = Tk()
g_Tk.geometry("420x500+750+200")
DataList = []
var1 = IntVar()
var2 = IntVar()


def InitTopText():
    TempFont = font.Font(g_Tk, size=20, weight='bold', family='Consolas')
    MainText = Label(g_Tk, font=TempFont, text="[Danawang~]")
    MainText.pack()
    MainText.place(x=140)


def InitInputLabel():
    global InputLabel
    TempFont = font.Font(g_Tk, size=10, weight='bold', family='Consolas')
    InputLabel = Entry(g_Tk, font=TempFont, width=33, borderwidth=6, relief='ridge')
    InputLabel.pack()
    InputLabel.place(x=120, y=60)


def InitSearchButton():
    TempFont = font.Font(g_Tk, size=10, weight='bold', family='Consolas')
    SearchButton = Button(g_Tk, font=TempFont, text="검색", command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=370, y=60)


def MartSearchCheckBox():
    TempFont = font.Font(g_Tk, size=10, weight='bold', family='Consolas')
    chkbox = Checkbutton(g_Tk, font=TempFont, text='마트 검색', variable=var1, command=SearchMart)
    chkbox2 = Checkbutton(g_Tk, font=TempFont, text='상품 검색', variable=var2)
    chkbox.pack()
    chkbox2.pack()
    chkbox.place(x=20, y=50)
    chkbox2.place(x=20, y=70)


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
    goodsLabel.place(x=10, y=100)


def InitButton():
    mapImg = PhotoImage(file="map.png")
    Mapbtn = Button(g_Tk, image=mapImg)
    Mapbtn.image = mapImg
    Mapbtn.pack()
    Mapbtn.place(x=200, y=425)

    mailImg = PhotoImage(file="gmail.png").subsample(9, 9)
    Mailbtn = Button(g_Tk, image=mailImg)
    Mailbtn.image = mailImg
    Mailbtn.pack()
    Mailbtn.place(x=275, y=425)

    telegramImg = PhotoImage(file="telegram.png").subsample(4, 4)
    Telegrambtn = Button(g_Tk, image=telegramImg)
    Telegrambtn.image = telegramImg
    Telegrambtn.pack()
    Telegrambtn.place(x=340, y=425)


def SearchResultRenderText():
    global RenderText

    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText = Text(g_Tk, width=38, height=8, borderwidth=6, relief='ridge')
    RenderText.pack()
    RenderText.place(x=121, y=90)

    RenderText.configure(state='disabled')


def InitRenderText():
    global RenderText

    RenderTextScrollbar = Scrollbar(g_Tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=375, y=200)

    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText = Text(g_Tk, width=25, height=20, borderwidth=6, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=10, y=215)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

    RenderText.configure(state='disabled')


def InitInputMartLabel():
    global InputMartLabel

    TempFont = font.Font(g_Tk, size=10, weight='bold', family='Consolas')
    MainText = Label(g_Tk, font=TempFont, text="판매점 이름을 입력하세요")
    MainText.pack()
    MainText.place(x=200, y=215)

    TempFont = font.Font(g_Tk, size=10, weight='bold', family='Consolas')
    InputMartLabel = Entry(g_Tk, font=TempFont, width=27, borderwidth=6, relief='ridge')
    InputMartLabel.pack()
    InputMartLabel.place(x=200, y=240)


def InitSbskButton():
    TempFont = font.Font(g_Tk, size=15, weight='bold', family='Consolas')
    selectbtn = Button(g_Tk, font=TempFont, text="판매점 선택")
    selectbtn.pack()
    selectbtn.place(x=210, y=280)

    sbskImg = PhotoImage(file="장바구니.png").subsample(2)
    sbskbtn = Button(g_Tk, image=sbskImg)
    sbskbtn.image = sbskImg
    sbskbtn.pack()
    sbskbtn.place(x=340, y=270)


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
