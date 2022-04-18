from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import os
from shutil import rmtree
from PIL import ImageTk, Image

PATH = os.getcwd() + "\\"


def open_file():
    file_types = (('Text files', '*.txt'),
                  ('All files', '*.*'))

    filename = fd.askopenfilename(
        title='Выберите файл с AppID',
        initialdir=os.getcwd(),
        filetypes=file_types)
    if filename != '':
        file_name = filename.split('/')
        output = f'Файл "{file_name[-1]}" успешно загружен и Applist сгенерирован'
        showinfo(
            title='Файл успешно загружен',
            message=output
        )
        file = open(f'{filename}')
        app_list = file.read().split('\n')
        try:
            os.mkdir(f'Applist')
        except FileExistsError:
            rmtree(f'{PATH}Applist')
            os.mkdir(f'Applist')
        for i in range(0, len(app_list)):
            with open(f'Applist\\{i}.txt', 'w') as f:
                f.write(f'{app_list[i]}')


root = Tk()
root.title('AppList generator')
root.iconbitmap(PATH+'gui\\generator.ico')
root.resizable(width=False, height=False)

canvas = Canvas(root, width=300, height=200, bg='white')
canvas.pack(fill="both", expand=True)

image = Image.open(f"{PATH}gui\\bg_image.jpg").resize((850, 600))
background_image = ImageTk.PhotoImage(image)
canvas.create_image(-100, -100, image=background_image)

canvas.create_text(150, 50,
                   text="Выберите файл с AppID\n"
                        "программа сгенерирует Applist",
                   fill='white',
                   justify=CENTER,
                   font=('Arial', 12))

open_button = Button(root,
                     text='Сгенерировать папку Applist',
                     font=('Arial', 12),
                     activebackground='gray',
                     command=open_file)
open_button.place(relx=0.13, rely=0.65)

root.mainloop()
