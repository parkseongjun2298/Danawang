from tkinter import *
import threading
import sys
from tkinter import messagebox
# pip install folium
import folium
# pip install cefpython3==66.1

from tkinter import messagebox
import threading
import sys
import folium
from cefpython3 import cefpython as cef

# cef모듈로 브라우저 실행
def showMap(frame):
    sys.excepthook = cef.ExceptHook
    window_info = cef.WindowInfo(frame.winfo_id())
    window_info.SetAsChild(frame.winfo_id(), [0,0,800,600])
    cef.Initialize()
    browser = cef.CreateBrowserSync(window_info, url='file:///map.html')
    cef.MessageLoop()



def Pressed():
    # 지도 저장
    # 위도 경도 지정
    m = folium.Map(location=[37.3402849, 126.7313189], zoom_start=13)
    # 마커 지정
    folium.Marker([37.3402849, 126.7313189], popup='한국산업기술대').add_to(m)
    # html 파일로 저장
    m.save('map.html')

    # 브라우저를 위한 쓰레드 생성
    thread = threading.Thread(target=showMap, args=(frame,))
    thread.daemon = True
    thread.start()


window = Tk()
Button(window, text='folium 지도', command=Pressed).pack()
frame = Frame(window, width=800, height=600)
frame.pack()
window.mainloop()