from tkinter import *

from tkinter import filedialog
#from idlelib.tooltip import Hovertip
from docx import Document
from docx.shared import Pt
import os

from PIL import Image, ImageTk

import pytesseract

root = Tk()
root.geometry('1280x720')
root.title('DigiDocs')

#Test Image Path
test_img_path = "C:/Users/user/Documents/4TH YEAR - 2ND SEM/Neural Networks/DigiDocs/Test"
create_path = lambda f: os.path.join(test_img_path, f)

image_files = os.listdir(test_img_path)
image_path = image_files[2]

path = create_path(image_path)


#Download Converted Image
def download_image():
    document = Document()
    font = document.styles['Normal'].font
    font.name = 'Calibri'
    font.size = Pt(11)
    document.add_paragraph(text)
    document.save('C:/Users/user/Documents/4TH YEAR - 2ND SEM/Neural Networks/DigiDocs/Test.docx')


#Converts Image to Text
def ocr():
    global text
    custom_oem_psm_config = ''

    image = Image.open(path)
    text = pytesseract.image_to_string(image)

    try:
        x = text[0]
    except IndexError:
        print("Failed to recognize text")
        return 0
    else:
        print(text)


#Upload Page
def upload_page():

    global img, img1, frame_img, convert_img, save_img, clear_img, delete_img, canvas, frame, convert_btn, clear_btn, save_btn, delete_btn

    filename = filedialog.askopenfilename(filetypes=[('All Files', '*.*')], 
                                          initialdir='C:/Users/user/Documents/4TH YEAR - 2ND SEM/Neural Networks/DigiDocs/Test')

    img = Image.open(filename)
    img_resized = img.resize((200, 150))
    img1 = ImageTk.PhotoImage(img_resized)

    frame_img = PhotoImage(file="C:/Users/user/Documents/4TH YEAR - 2ND SEM/Neural Networks/DigiDocs/Image.png")
    frame = Label(root, image=frame_img, borderwidth=0, highlightthickness=0)
    frame.place(x=400.0, y=150.0)
    
    delete_img = PhotoImage(file="C:/Users/user/Documents/4TH YEAR - 2ND SEM/Neural Networks/DigiDocs/Delete.png")
    delete_btn = Button(root, image=delete_img, borderwidth=0, highlightthickness=0, relief="flat",
                        bg='#D9D9D9', command=lambda: [canvas.destroy(), frame.destroy(),
                                                       convert_btn.destroy(), clear_btn.destroy(),
                                                       save_btn.destroy(), delete_btn.destroy(),
                                                       create_page()])
    delete_btn.place(x=590, y=350)

    canvas = Label(root, image=img1,  borderwidth=0, highlightthickness=0)
    canvas.place(x=430.0, y=180.0, width=200, height=150)

    convert_img = PhotoImage(file="C:/Users/user/Documents/4TH YEAR - 2ND SEM/Neural Networks/DigiDocs/Convert.png")
    convert_btn = Button(root, image=convert_img, borderwidth=0, highlightthickness=0, relief="flat",
                         command=lambda:[converted_notif(), ocr()])
    convert_btn.place(x=820.0, y=620)

    save_img = PhotoImage(file="C:/Users/user/Documents/4TH YEAR - 2ND SEM/Neural Networks/DigiDocs/Save.png")
    save_btn = Button(root, image=save_img, borderwidth=0, highlightthickness=0, relief="flat",
                      command=lambda:[saved_notif(), saved_file()])
    save_btn.place(x=1000.0, y=620)

    clear_img = PhotoImage(file="C:/Users/user/Documents/4TH YEAR - 2ND SEM/Neural Networks/DigiDocs/Clear.png")
    clear_btn = Button(root, image=clear_img, borderwidth=0, highlightthickness=0, relief="flat",
                       bg='#F0F0F0', command=lambda:[canvas.destroy(), frame.destroy(),
                                                       convert_btn.destroy(), clear_btn.destroy(),
                                                       save_btn.destroy(), delete_btn.destroy(),
                                                       create_page()])
    clear_btn.place(x=1120.0, y=630)

    create_page()
    add_btn_1.destroy()


#Saved Page
def saved_page():
    global img1, frame_img, convert_img, save_img, clear_img, delete_img, canvas, frame, convert_btn, clear_btn, save_btn, delete_btn

    filename = filedialog.askopenfilename(filetypes=[('All Files', '*.*')], 
                                          initialdir='C:/Users/user/Documents/4TH YEAR - 2ND SEM/Neural Networks/DigiDocs/Drafts')

    img = Image.open(filename)
    img_resized = img.resize((200, 150))
    img1 = ImageTk.PhotoImage(img_resized)

    frame_img = PhotoImage(file="C:/Users/user/Documents/4TH YEAR - 2ND SEM/Neural Networks/DigiDocs/Image.png")
    frame = Label(root, image=frame_img, borderwidth=0, highlightthickness=0)
    frame.place(x=400.0, y=150.0)
    
    delete_img = PhotoImage(file="C:/Users/user/Documents/4TH YEAR - 2ND SEM/Neural Networks/DigiDocs/Delete.png")
    delete_btn = Button(root, image=delete_img, borderwidth=0, highlightthickness=0, relief="flat",
                        bg='#D9D9D9', command=lambda: [canvas.destroy(), frame.destroy(),
                                                       convert_btn.destroy(), clear_btn.destroy(),
                                                       save_btn.destroy(), delete_btn.destroy(),
                                                       create_page()])
    delete_btn.place(x=590, y=350)

    canvas = Label(root, image=img1,  borderwidth=0, highlightthickness=0)
    canvas.place(x=430.0, y=180.0, width=200, height=150)

    convert_img = PhotoImage(file="C:/Users/user/Documents/4TH YEAR - 2ND SEM/Neural Networks/DigiDocs/Convert.png")
    convert_btn = Button(root, image=convert_img, borderwidth=0, highlightthickness=0, relief="flat",
                         command=lambda:[converted_notif(), ocr()])
    convert_btn.place(x=820.0, y=620)

    save_img = PhotoImage(file="C:/Users/user/Documents/4TH YEAR - 2ND SEM/Neural Networks/DigiDocs/Save.png")
    save_btn = Button(root, image=save_img, borderwidth=0, highlightthickness=0, relief="flat",
                      command=lambda:[saved_notif(), saved_file()])
    save_btn.place(x=1000.0, y=620)

    clear_img = PhotoImage(file="C:/Users/user/Documents/4TH YEAR - 2ND SEM/Neural Networks/DigiDocs/Clear.png")
    clear_btn = Button(root, image=clear_img, borderwidth=0, highlightthickness=0, relief="flat",
                       bg='#F0F0F0', command=lambda:[canvas.destroy(), frame.destroy(),
                                                       convert_btn.destroy(), clear_btn.destroy(),
                                                       save_btn.destroy(), delete_btn.destroy(),
                                                       create_page()])
    clear_btn.place(x=1120.0, y=630)

    create_page()
    add_btn_1.destroy()


#Saves file to folder
def saved_file():
    filename = filedialog.asksaveasfilename(defaultextension='.jpg', filetypes=[('All Files', '*.*')],
                                            initialdir='C:/Users/user/Documents/4TH YEAR - 2ND SEM/Neural Networks/DigiDocs/Drafts')
    img.save(filename)


#Converted Notification
def converted_notif():

    global download_img, save_img1, exit_img

    notif_win = Toplevel(root)

    win_width = 600
    win_height = 100

    scrn_width = notif_win.winfo_screenwidth()
    scrn_height = notif_win.winfo_screenheight()

    center_x = int(scrn_width/2 - win_width/2)
    center_y = int(scrn_height/2 - win_height/2)

    notif_win.geometry(f'{win_width}x{win_height}+{center_x}+{center_y}')

    lb = Label(notif_win, text='Document Successfully Converted!', font="Arial 12 bold")
    lb.place(relx=0.5, y=20, anchor=CENTER)

    download_img = PhotoImage(file="C:/Users/user/Documents/4TH YEAR - 2ND SEM/Neural Networks/DigiDocs/Download.png")
    download_btn = Button(notif_win, image=download_img, borderwidth=0, highlightthickness=0, relief="flat",
                          command=lambda:[notif_win.destroy(), download_image()])
    download_btn.place(x=125, y=60)

    save_img1 = PhotoImage(file="C:/Users/user/Documents/4TH YEAR - 2ND SEM/Neural Networks/DigiDocs/Save.png")
    save_btn = Button(notif_win, image=save_img1, borderwidth=0, highlightthickness=0, relief="flat",
                      command=lambda: saved_notif())
    save_btn.place(x=300, y=60)

    exit_img = PhotoImage(file="C:/Users/user/Documents/4TH YEAR - 2ND SEM/Neural Networks/DigiDocs/Exit.png")
    exit_btn = Button(notif_win, image=exit_img, borderwidth=0, highlightthickness=0, relief="flat",
                      command=lambda:notif_win.destroy())
    exit_btn.place(x=425, y=70)

    icon1 = PhotoImage(file="C:/Users/user/Documents/4TH YEAR - 2ND SEM/Neural Networks/DigiDocs/BG.png")
    notif_win.iconphoto(False, icon1)

    notif_win.overrideredirect(True)


#Saved to Drafts Notification
def saved_notif():

    global ok_img

    notif_win = Toplevel(root)

    win_width = 600
    win_height = 100

    scrn_width = notif_win.winfo_screenwidth()
    scrn_height = notif_win.winfo_screenheight()

    center_x = int(scrn_width / 2 - win_width / 2)
    center_y = int(scrn_height / 2 - win_height / 2)

    notif_win.geometry(f'{win_width}x{win_height}+{center_x}+{center_y}')

    lb = Label(notif_win, text='Saved to Drafts!', font="Arial 12 bold")
    lb.place(relx=0.5, y=20, anchor=CENTER)

    ok_img = PhotoImage(file="C:/Users/user/Documents/4TH YEAR - 2ND SEM/Neural Networks/DigiDocs/OK.png")
    ok_btn = Button(notif_win, image=ok_img, borderwidth=0, highlightthickness=0, relief="flat",
                          command=lambda:notif_win.destroy())
    ok_btn.place(relx=0.5, y=60, anchor=CENTER)


    icon2 = PhotoImage(file="C:/Users/user/Documents/4TH YEAR - 2ND SEM/Neural Networks/DigiDocs/BG.png")
    notif_win.iconphoto(False, icon2)
    notif_win.overrideredirect(True)


#Create Page
def create_page():
    global add_btn_1, add_image_1

    create_frame = Frame(main_frame)
    lb = Label(create_frame, text='Welcome!', font="Arial 20 bold")
    lb.pack(ipadx=100, ipady=100, side=TOP, anchor="w")
    create_frame.pack()

    add_image_1 = PhotoImage(file="C:/Users/user/Documents/4TH YEAR - 2ND SEM/Neural Networks/DigiDocs/Create.png")
    add_btn_1 = Button(root, image=add_image_1, borderwidth=0, highlightthickness=0, relief="flat", 
                       command= lambda: upload_page())
    add_btn_1.place(x=400.0, y=150.0, width=250.0, height=150.0)


#Deletes Page
def delete_pages():
    for frame in main_frame.winfo_children():
        frame.pack_forget()

    
options_frame = Frame(root, bg='#151414')


#Create Button
create_btn = Button(options_frame, text='Create New Document', font='Arial 14 bold', fg='#FFFFFF', bd=0,
                    bg='#151414', activeforeground='#FFFFFF', activebackground='#151414', 
                    command=lambda: [create_page(), canvas.destroy(), frame.destroy(),
                                                       convert_btn.destroy(), clear_btn.destroy(),
                                                       save_btn.destroy(), delete_btn.destroy()])
create_btn.place(x=40, y=150, height=35)


#Draft Button
draft_btn = Button(options_frame, text='Drafts', font='Arial 14 bold', fg='#FFFFFF', bd=0,
                   bg='#151414', activeforeground='#FFFFFF', activebackground='#151414',
                   command=lambda: saved_page())
draft_btn.place(x=40, y=200, height=35)


#Options Frame
options_frame.pack(side=LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=300, height=720)


#Main Frame
main_frame = Frame(root)
main_frame.pack(ipady=20, side=TOP, anchor="w")
main_frame.configure(width=1280, height=720)


#DigiDocs Logo
logo_image = PhotoImage(file="C:/Users/user/Documents/4TH YEAR - 2ND SEM/Neural Networks/DigiDocs/Logo.png")

logo = Label(options_frame, image=logo_image, bg='#151414')
logo.place(x=1, y=20)


#Background Image
bg_image = PhotoImage(file="C:/Users/user/Documents/4TH YEAR - 2ND SEM/Neural Networks/DigiDocs/BG.png")
bg = Label(root, image=bg_image, bg='#F0F0F0')
bg.place(x=300, y=200)


#Icon
icon = PhotoImage(file="C:/Users/user/Documents/4TH YEAR - 2ND SEM/Neural Networks/DigiDocs/BG.png")
root.iconphoto(False, icon)

create_page()

root.mainloop()