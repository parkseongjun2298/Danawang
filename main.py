from tkinter import *
from tkinter import font
import tkinter.messagebox
import xml.etree.ElementTree as ET

BG_COLOR = 'light blue'

g_Tk = Tk()
g_Tk.geometry("505x640+750+200")
g_Tk.title("DANAWANG")
g_Tk['bg'] = BG_COLOR

var1 = IntVar()
var2 = IntVar()
searchText = StringVar()

goodsTree = ET.parse('totalGoodsInfo.xml')
goodsRoot = goodsTree.getroot()
martTree = ET.parse('totalMartInfo.xml')
martRoot = martTree.getroot()

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
    # 마트 검색 체크
    if var1.get() == 1:
        for child in martRoot:
            if sText in child[1].text:
                s = searchText.get()
                s += child[1].text
                print(child[1].text)
        searchText.set(s)

    # 상품 검색 체크
    if var2.get() == 1:
        for child in goodsRoot:
            if sText in child[1].text:
                RenderText.insert(INSERT, child[1].text)
                print(child[1].text)

        # for i in s:
        #     RenderText.insert(END, i)

    SearchResultRenderText()
                
        #         s = searchText.get()
        #         s += child[1].text
        #         print(child[1].text)
        # searchText.set(s)
            # for i in range(8):
            #     print(child[i].text, end=' ')
            # print('\n')

    # global SearchListBox

    # RenderText.configure(state='normal')
    # RenderText.delete(0.0, END)
    # iSearchIndex = SearchListBox.curselection()[0]
    # if iSearchIndex == 0:
    #     SearchMart()
    # elif iSearchIndex == 1:
    #     pass
    # elif iSearchIndex == 2:
    #     pass
    # elif iSearchIndex == 3:
    #     pass

    # RenderText.configure(state='disabled')

# 마트/상품 검색한 것 보여주는 함수
def SearchResultRenderText():
    global RenderText

    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText = Text(g_Tk, width=50, height=9, borderwidth=6, relief='ridge')
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
    Mailbtn = Button(g_Tk, image=mailImg)
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
def InitInputMartLabel():
    global InputMartLabel

    TempFont = font.Font(g_Tk, size=12, weight='bold', family='Consolas')
    MainText = Label(g_Tk, font=TempFont, bg = BG_COLOR, text="판매점 이름을 입력하세요")
    MainText.pack()
    MainText.place(x=245, y=252)

    TempFont = font.Font(g_Tk, size=10, weight='bold', family='Consolas')
    InputMartLabel = Entry(g_Tk, font=TempFont, width=31, borderwidth=6, relief='ridge')
    InputMartLabel.pack()
    InputMartLabel.place(x=245, y=273)

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


InitTopText()
MartSearchCheckBox()
InitInputEntry()
InitSearchButton()
RenderGoodsImage()
InitButton()
SearchResultRenderText()
InitRenderMartText()
InitInputMartLabel()
InitSbskButton()

g_Tk.mainloop()
