;ControlFocus()方法用于识别Window窗口ControlFocus("文件上传", "","Edit1")
; WinWait()设置10秒钟用于等待窗口的显示
WinWait("[CLASS:#32770]","",3)
; ControlSetText()用于向“文件名”输入框内输入本地文件的路径，如果是在桌面第三个参数直接写文件名
ControlSetText("文件上传", "", "Edit1", "C:\Users\admin\Desktop\cat.jpg")
Sleep(1000)
; ControlClick()用于点击上传窗口中的“打开”按钮
ControlClick("文件上传", "","Button1");
