from tkinter import *
from tkinter import font

import tkinter.messagebox
g_Tk = Tk()
g_Tk.geometry("400x600+750+200")
DataList = []
var1 = IntVar()
var2 = IntVar()

def InitTopText():
    TempFont = font.Font(g_Tk, size=20, weight='bold', family = 'Consolas')
    MainText = Label(g_Tk, font = TempFont, text="[Danawang~]")
    MainText.pack()
    MainText.place(x=120)




def InitInputLabel():
    global InputLabel
    TempFont = font.Font(g_Tk, size=10, weight='bold', family = 'Consolas')
    InputLabel = Entry(g_Tk, font = TempFont, width = 28, borderwidth = 6, relief = 'ridge')
    InputLabel.pack()
    InputLabel.place(x=120, y=60)

def InitSearchButton():
    TempFont = font.Font(g_Tk, size=10, weight='bold', family = 'Consolas')
    SearchButton = Button(g_Tk, font = TempFont, text="검색",  command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=334, y=60)
def MartSearchCheckBox():

    chkbox=Checkbutton(g_Tk, text='마트 검색', variable=var1,command=SearchMart)
    chkbox2 = Checkbutton(g_Tk, text='상품 검색', variable=var2)
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
    if var1.get()==True:
        import urllib
        import http.client
        conn = http.client.HTTPConnection("openapi.price.go.kr")
        conn.request("GET","/openApiImpl/ProductPriceInfoService/getProductPriceInfoSvc.do?serviceKey=%2BD2FzMpML7KBFXB2law50GJANbBLxxEO8U2hX1YsjNwaLBqoqG%2FsbsR6QiGzg5sk2nIa3kRWpljvOZVryafkcQ%3D%3D&goodInspectDay=20200508&entpId=100")
        req = conn.getresponse()
        global DataList
        DataList.clear()
        if req.status == 200:
            BooksDoc = req.read().decode('utf-8')
            if BooksDoc == None:
                print("에러")
            else:
                pass





def SearchResultRenderText():
    global RenderText



    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText = Text(g_Tk, width=34, height=8, borderwidth=6, relief='ridge')
    RenderText.pack()
    RenderText.place(x=120, y=90)


    RenderText.configure(state='disabled')

def InitRenderText():
    global RenderText

    RenderTextScrollbar = Scrollbar(g_Tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=375, y=200)

    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText = Text(g_Tk, width=25, height=28, borderwidth=6, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=10, y=215)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

    RenderText.configure(state='disabled')


InitTopText()
MartSearchCheckBox()
SearchMart()
InitInputLabel()
InitSearchButton()
SearchResultRenderText()
InitRenderText()


g_Tk.mainloop()