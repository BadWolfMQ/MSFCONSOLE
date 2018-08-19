import os
import time
from tkinter import *


os.system(' mode con: cols=40 lines=8')
print (40 * '=')
print ("      M E N U - P R I N C I P A L ")
print (40 * '=')
print (" 1. Download")
print (" 2. Documentos")
print (" 3. Aplicativos")
print('')
MenuPrincipal = input('Escolha: ')
MenuPrincipal = int(MenuPrincipal)


if MenuPrincipal == 1:
        #MENU DE DOWNLOADS

        os.system(' mode con: cols=98 lines=20')
        print('                                            [Download]')
        print('')
        print('[1-Sony vegas][            ][            ][            ][            ][            ][            ]')
        print('[2-Photoshop ][            ][            ][            ][            ][            ][            ]')
        print('[            ][            ][            ][            ][            ][            ][            ]')
        print('[            ][            ][            ][            ][            ][            ][            ]')
        print('[            ][            ][            ][            ][            ][            ][            ]')
        print('[            ][            ][            ][            ][            ][            ][            ]')
        print('[            ][            ][            ][            ][            ][            ][            ]')
        print('[            ][            ][            ][            ][            ][            ][            ]')
        print('[            ][            ][            ][            ][            ][            ][            ]')
        print('[            ][            ][            ][            ][            ][            ][            ]')
        print('[            ][            ][            ][            ][            ][            ][            ]')
        print('[            ][            ][            ][            ][            ][            ][            ]')
        print('[            ][            ][            ][            ][            ][            ][            ]')
        print('[            ][            ][            ][            ][            ][            ][            ]')
        print('[            ][            ][            ][            ][            ][            ][            ]')
        print('[            ][            ][            ][            ][            ][            ][            ]')
        print('')
        MenuDownloads = input('                                                 ')
        MenuDownloads = int(MenuDownloads)

        if MenuDownloads == 1:
                import wget
                os.system(' mode con: cols=100 lines=4')
                url = 'http://download1595.mediafire.com/k8c1pxgslhpg/kq097qng4zcig9s/SonyVegas.rar'
                wolf = wget.download (url)
                print("100% [............................................... .] 3841532/3841532>")
                wolf
                'app'
        elif MenuDownloads == 2:
                import wget
                os.system(' mode con: cols=100 lines=4')
                url = 'http://download1181.mediafire.com/m9p94nb61nyg/4gic085v4482773/Photoshop+CS6+PT-BR+2017+%28C4N4L+JC%29.rar'
                wolf = wget.download (url)
                print("100% [............................................... .] 3841532/3841532>")
                wolf
                'app'





elif MenuPrincipal == 2:
        os.startfile('notepad')
elif MenuPrincipal == 3:
        janela = Tk()
        janela.geometry('200x200')
        janela.title('Janela 1')
        janela.mainloop()
else:
        os.system('clear')
        print ("Opção invalida. Tente novamente...")