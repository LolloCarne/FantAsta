import tkinter as tk
from tkinter import PhotoImage,messagebox
import json

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


def creaAsta():
    if box1.get() != "" and box2.get() != "" and box3.get() != "" and box4.get() != "" and box5.get() != "":
        if len(box2.get().split(",")) == int(box1.get()):
            if box4.get() in box2.get().split(","):
                data={"num_partecipanti":int(box1.get()),"nomi_partecipanti":box2.get().split(","),"crediti":int(box3.get()),"presidente":box4.get(),"lega":box5.get()}
                jsonOBJ=json.dumps(data)
                with open("datiAsta.json","w") as file:
                    file.write(jsonOBJ)
                root.destroy()
                import asta
            else:
                messagebox.showerror("Errore","Il Presidente non è presente tra i nomi inseriti")

        else:
            messagebox.showerror("Errore","Numero dei partecipanti diverso dal numero di nomi inseriti")
    else:
         messagebox.showerror("Errore","è necessario compilare tutti i campi obbligatori")

num_partecipanti=tk.Label(root,font=("Times bold", 14),text="Numero Dei Partecipanti:",bg=main_color,fg=text_color)
num_partecipanti.grid(column=0,row=0,sticky="W",pady=10)
box1=tk.Entry(root,bd=3,width=20,bg=text_color)
box1.grid(column=0,row=1,sticky="W",padx=15)
nomi_partecipanti=tk.Label(root,font=("Times bold", 14),text="Nomi Dei Partecipanti(separati dalla virgola):",bg=main_color,fg=text_color)
nomi_partecipanti.grid(column=0,row=2,pady=10)
box2=tk.Entry(root,bd=3,width=20,bg=text_color)
box2.grid(column=0,row=3,sticky="W",padx=15)

crediti=tk.Label(root,font=("Times bold", 14),text="Crediti:",bg=main_color,fg=text_color)
crediti.grid(column=0,row=4,sticky="W",pady=10)
box3=tk.Entry(root,bd=3,width=20,bg=text_color)
box3.grid(column=0,row=5,sticky="W",padx=15)

presidente=tk.Label(root,font=("Times bold", 14),text="Presidente:",bg=main_color,fg=text_color)
presidente.grid(column=0,row=6,sticky="W",pady=10)
box4=tk.Entry(root,bd=3,width=20,bg=text_color)
box4.grid(column=0,row=7,sticky="W",padx=15)

lega=tk.Label(root,font=("Times bold", 14),text="Nome Lega:",bg=main_color,fg=text_color)
lega.grid(column=0,row=8,sticky="W",pady=10)
box5=tk.Entry(root,bd=3,width=20,bg=text_color)
box5.grid(column=0,row=9,sticky="W",padx=15)


invio=tk.Button(text="Crea Asta",command=creaAsta,width=15,bg=second_color,relief="raised",fg=main_color,borderwidth=0)
invio.grid(column=2,row=10)




if __name__=="__main__":
    root.mainloop()