import os
import tkinter as tk
from tkinter import PhotoImage,messagebox,Toplevel,filedialog
from tkinter import ttk
import json
from tkinter.constants import BOTTOM, RIGHT

file=""
FONT=("Times bold", 14)
#creazione e configurazione della finestra madre
root = tk.Tk()
root.geometry("600x600")
root.title("FantAsta")
logo=PhotoImage(file="logo_small.png")
root.iconphoto(False,logo)
main_color="#292828"
second_color="#4A8DFF"
text_color="#919191"
root.config(bg=main_color)

#banner 
banner=PhotoImage(file="banner_small.png")
bannerLB=tk.Label(root,image=banner)
bannerLB.pack(pady=15)




def nuovaAsta():
    root.destroy()
    import main
nuova=tk.Button(root,text="Crea Asta",command=nuovaAsta,width=20,height=2,bg=second_color,relief="raised",fg=main_color,borderwidth=0)
nuova.pack(pady=15)

def importaAsta():
    filetypes = (
        ('json files', '*.json'),
        ('All files', '*.*')
    )
    flag=False
    
    f= filedialog.askopenfilename(filetypes=filetypes)
    if f == '':
        flag=True
    if flag==False:
        with open("datiAsta.json","r") as filejson:
            dictjson= json.load(filejson)
        dictjson["file"]=f
        with open("datiAsta.json","w") as filejson2:
            json.dump(dictjson,filejson2)
        root.destroy()
        import astaCaricata

        
    
nuova=tk.Button(root,text="Importa Asta",command=importaAsta,width=20,height=2,bg=second_color,relief="raised",fg=main_color,borderwidth=0)
nuova.pack(pady=15)

def seleziona_Asta(x,finestra):
    with open("datiAsta.json","r") as filejson:
        f= json.load(filejson)
    f["file"]=x
    with open("datiAsta.json","w") as filejson2:
        json.dump(f,filejson2)
    finestra.destroy()
    root.destroy()
    import astaCaricata

def caricaaAsta():
    lista_aste=[]
    lista_file=os.listdir()
    #print(lista_file)
    for file in lista_file:
        if ".json" in file and file != "datiAsta.json":
            lista_aste.append(file)
    
    new_window=Toplevel(root)
    new_window.geometry("300x300")
    logo=PhotoImage(file="logo_small.png")
    new_window.iconphoto(False,logo)
    new_window.config(bg=main_color)
    select_asta= tk.Label(new_window,text="Seleziona asta da caricare: ",font=("Times bold", 14),bg=main_color,fg=text_color)
    select_asta.pack()
    combo_select=ttk.Combobox(new_window,values=lista_aste)
    combo_select.pack(pady=15)
    butt_select=tk.Button(new_window,text="Seleziona",width=20,height=2,bg=second_color,relief="raised",fg=main_color,borderwidth=0)
    #associo alla premuta del bottone la chiamata di seleziona asta con il passaggio del file json
    butt_select.bind('<Button-1>',lambda i: seleziona_Asta(combo_select.get(),new_window))
    butt_select.pack(pady=10)



    
nuova=tk.Button(root,text="Carica Asta",command=caricaaAsta,width=20,height=2,bg=second_color,relief="raised",fg=main_color,borderwidth=0)
nuova.pack(pady=15)

credits=tk.Label(root,text="Powered by LOLLOS (2021)",font=("Times bold", 10),bg=main_color,fg=text_color)
credits.pack(side=BOTTOM)


if __name__=="__main__":
    root.mainloop()