import csv
from sys import path
from tkinter import PhotoImage, Toplevel, ttk,filedialog
from tkinter import messagebox
from tkinter.constants import ANCHOR
import sqlite3
import tkinter as tk
import json

db=sqlite3.connect("serieA.db")
cursore=db.cursor()
with open("datiAsta.json","r") as filejson:
    f= json.load(filejson)
filename=f["file"]

with open(filename,"r") as jsonOBJ:
    dictJSON=json.load(jsonOBJ)

CREDITI=dictJSON["crediti"]
PRESIDENTE=dictJSON["presidente"]
LEGA=dictJSON["lega"]
NOMI_PARTECIPANTI=dictJSON["partecipanti"]
taken=dictJSON["taken"]

class Partecipante():
    def __init__(self,nome) -> None:
        self.crediti=CREDITI
        self.slot_difensori=8
        self.slot_centrocampisti=8
        self.slot_attaccanti=6
        self.slot_portieri=3
        self.difensori=[]
        self.centrocampisti=[]
        self.attaccanti=[]
        self.portieri=[]
        self.nome=nome

    def __repr__(self) -> str:
        #giocatori_totali=self.portieri+self.difensori+self.centrocampisti+self.attaccanti
        stringa_difensori=""
        stringa_portieri=""
        stringa_attaccanti=""
        stringa_centrocampisti=""
        for i in self.difensori:
            stringa_difensori+=str(i)+"\n  "
        for i in self.portieri:
            stringa_portieri+=str(i)+"\n  "
        for i in self.centrocampisti:
            stringa_centrocampisti+=str(i)+"\n  "
        for i in self.attaccanti:
            stringa_attaccanti+=str(i)+"\n  "
        slot_rimasti=self.slot_portieri+self.slot_attaccanti+self.slot_centrocampisti+self.slot_difensori
        p=f"Stato Di {self.nome}: \nCrediti disponibili: {self.crediti} \nPortieri: {stringa_portieri} \nDifensori: {stringa_difensori} \nCentrocampisti: {stringa_centrocampisti} \nAttaccanti: {stringa_attaccanti} \nSlot rimanenti:{slot_rimasti} \nLegenda:[Ruolo,Giocatore,Club,Quotazione,Crediti Spesi]"
        return p
    def addPlayer(self,info_gioc,prezzo):
        info_gioc=list(info_gioc)
        info_gioc.append(prezzo)
        slot_liberi=self.slot_attaccanti+self.slot_centrocampisti+self.slot_difensori+self.slot_portieri
        if self.crediti>int(prezzo)+slot_liberi-1:
            if info_gioc[0] == "P":
                if self.slot_portieri >0:
                    self.slot_portieri-=1
                    self.crediti-=int(prezzo)
                    self.portieri.append(info_gioc)
                    taken.append(info_gioc)
                    messagebox.showinfo("Completato",f"{info_gioc[1]} aggiunto correttamente a {self.nome}")
                else:
                    messagebox.showerror("Errore","Slot portieri terminati")
            if info_gioc[0] == "D":
                if self.slot_difensori >0:
                    self.slot_difensori-=1
                    self.crediti-=int(prezzo)
                    self.difensori.append(info_gioc)
                    taken.append(info_gioc)
                    messagebox.showinfo("Completato",f"{info_gioc[1]} aggiunto correttamente a {self.nome}")
                else:
                    messagebox.showerror("Errore","Slot difensori terminati")
            if info_gioc[0] == "C":
                if self.slot_centrocampisti >0:
                    self.slot_centrocampisti-=1
                    self.crediti-=int(prezzo)
                    self.centrocampisti.append(info_gioc)
                    taken.append(info_gioc)
                    messagebox.showinfo("Completato",f"{info_gioc[1]} aggiunto correttamente a {self.nome}")
                else:
                    messagebox.showerror("Errore","Slot centrocampisti terminati")
            if info_gioc[0] == "A":
                if self.slot_attaccanti >0:
                    self.slot_attaccanti-=1
                    self.crediti-=int(prezzo)
                    self.attaccanti.append(info_gioc)
                    taken.append(info_gioc)
                    messagebox.showinfo("Completato",f"{info_gioc[1]} aggiunto correttamente a {self.nome}")
                else:
                    messagebox.showerror("Errore","Slot attaccanti terminati")
            combo_partecipanti.delete(0,len(combo_partecipanti.get()))
            campo_ricerca.delete(0,len(campo_ricerca.get()))
            box_crediti.delete(0,len(box_crediti.get()))

            lista_ricerca.delete(0,lista_ricerca.size()-1)


            pass
        else:
            messagebox.showerror("Errore","Crediti insufficenti per completare l'asta")
partecipanti=[]
for nome in NOMI_PARTECIPANTI:
    p=Partecipante(nome)
    partecipanti.append(p)

for partecipante in partecipanti:
    partecipante.portieri=list(dictJSON[partecipante.nome][0])
    partecipante.difensori=list(dictJSON[partecipante.nome][1])
    partecipante.centrocampisti=list(dictJSON[partecipante.nome][2])
    partecipante.attaccanti=list(dictJSON[partecipante.nome][3])
    partecipante.crediti=dictJSON[partecipante.nome][4]
    partecipante.slot_portieri=dictJSON[partecipante.nome][5]
    partecipante.slot_difensori=dictJSON[partecipante.nome][6]
    partecipante.slot_centrocampisti=dictJSON[partecipante.nome][7]
    partecipante.slot_attaccanti=dictJSON[partecipante.nome][8]


root = tk.Tk()
root.geometry("600x600")
root.title("FantAsta")
main_color="#292828"
second_color="#4A8DFF"
text_color="#919191"
root.config(bg=main_color)
logo=PhotoImage(file="logo_small.png")
root.iconphoto(False,logo)

def on_closing():
    if messagebox.askokcancel("Esci","Sicuro di uscire da questa pagina?\n (i dati non salvati andranno persi)"):
        root.destroy()
root.protocol("WM_DELETE_WINDOW",on_closing)


#label partecipante
label_partecipanti= tk.Label(root,text="Seleziona Un Partecipante:",font=("Times bold", 14),bg=main_color,fg=text_color)
label_partecipanti.grid(column=0,row=0,sticky="W")

#combo partecipante
combo_partecipanti=ttk.Combobox(root,values=NOMI_PARTECIPANTI)
combo_partecipanti.grid(column=0,row=1,padx=10,sticky="W")

#label
ricerca= tk.Label(root,text="Cerca Un Giocatore:",font=("Times bold", 14),bg=main_color,fg=text_color)
ricerca.grid(column=0,row=2,sticky="W",pady=10)

#entry box
campo_ricerca=tk.Entry(root,font=(18),width=20,bg=text_color)
campo_ricerca.grid(column=0,row=3,padx=10)

#listbox
lista_ricerca=tk.Listbox(root,width=50,height=8,bg=text_color)
lista_ricerca.grid(column=0,row=4,padx=10,pady=10)


def search():
    pass
    lista_ricerca.delete(0,lista_ricerca.size()-1)
    giocatore=campo_ricerca.get().upper()
    cursore.execute(f"SELECT Ruolo,Cognome,Squadra,Quotazione FROM calciatori WHERE cognome= '{giocatore}' COLLATE NOCASE")
    c=0
    for i in cursore:
        lista_ricerca.insert(c,i)

#bottone
bottone_ricerca=tk.Button(root,text="Ricerca",command=search,bg=second_color,relief="raised",fg=main_color,borderwidth=0)
bottone_ricerca.grid(column=1,row=3,sticky="W")

#label crediti
label_crediti=tk.Label(root,text="Inserisci Il Costo:",font=("Times bold", 14),bg=main_color,fg=text_color)
label_crediti.grid(column=1,row=4,sticky="S")

#box crediti
box_crediti=tk.Entry(root,font=("Helvetica", 12),width=10,bg=text_color)
box_crediti.grid(column=2,row=4,sticky="S")

def seleziona():
    if combo_partecipanti.get() == "":
        print("seleziona un partecipante")
        messagebox.showerror("Errore","Seleziona un partecipante")
    elif lista_ricerca.get(ANCHOR) == "":
        messagebox.showerror("Errore","Seleziona un giocatore")
    
    elif box_crediti.get() == "":
         messagebox.showerror("Errore","Inserisci costo del giocatore")
    else:
        #print(lista_ricerca.get(ANCHOR))
        #print(combo_partecipanti.get())
        #print(box_crediti.get())
        if lista_ricerca.get(ANCHOR) in taken:
            messagebox.showerror("Errore","Giocatore già acquistato")
            combo_partecipanti.delete(0,len(combo_partecipanti.get()))
            campo_ricerca.delete(0,len(campo_ricerca.get()))
            box_crediti.delete(0,len(box_crediti.get()))

            lista_ricerca.delete(0,lista_ricerca.size()-1)
        else:
            for partecipante in partecipanti:
                if combo_partecipanti.get() == partecipante.nome:
                    partecipante.addPlayer(lista_ricerca.get(ANCHOR),box_crediti.get())
    

#bottone selezione
bottone_selezione=tk.Button(root,text="Aggiungi",bd=3,command=seleziona,bg=second_color,relief="raised",fg=main_color,borderwidth=0)
bottone_selezione.grid(column=0,row=5)

#label stato partecipante
label_stato= tk.Label(root,text="Visualizza Stato Partecipante: ",font=("Times bold", 14),bg=main_color,fg=text_color)
label_stato.grid(column=0,row=6,pady=10,padx=10)

#combo stato
combo_stato=ttk.Combobox(root,values=NOMI_PARTECIPANTI)
combo_stato.grid(column=0,row=7,padx=10,sticky="N",pady=0)

def stato():
    for partecipante in partecipanti:
        if combo_stato.get() == partecipante.nome:
            #print(partecipante)
            new_window=Toplevel(root)
            new_window.geometry("600x600")
            new_window.title(f"Stato di {partecipante.nome}")
            label_nuova=tk.Label(new_window,text=partecipante,font=("Courier",15))
            label_nuova.grid(pady=30,padx=20)


#bottone stato
bottone_stato=tk.Button(root,text="Seleziona",bd=3,command=stato,width=20,bg=second_color,relief="raised",fg=main_color,borderwidth=0)
bottone_stato.grid(column=1,row=7,sticky="W")

#creazione file json di salvataggio
def salva():

    salvataggio={}
    for partecipante in partecipanti:
        salvataggio[partecipante.nome]=[partecipante.portieri,partecipante.difensori,partecipante.centrocampisti,partecipante.attaccanti,partecipante.crediti,partecipante.slot_portieri,partecipante.slot_difensori,partecipante.slot_centrocampisti,partecipante.slot_attaccanti]
    salvataggio["crediti"]=CREDITI
    salvataggio["presidente"]=PRESIDENTE
    salvataggio["lega"]=LEGA
    salvataggio["taken"]=taken
    salvataggio["partecipanti"]=[]
    for p in partecipanti:
        salvataggio["partecipanti"].append(p.nome)
    jsonOBJ=json.dumps(salvataggio)
    with open(f"{LEGA}.json","w") as file:
        file.write(jsonOBJ)
    messagebox.showinfo("Info","Asta Salvata Correttamente \n(Lega.json)")
    #print(salvataggio)
    

#bottone stampa
bottone_stampa=tk.Button(root,text="Salva Asta",bd=3,width=20,bg=second_color,relief="raised",fg=main_color,borderwidth=0,height=2,command=salva)
bottone_stampa.grid(column=0,row=8,padx=20,pady=40)

def stampa():
    header=["Partecipante","Ruolo","Giocatore","Club","Quotazione","Prezzo"]
    finale=["Partecipante","Crediti","Slot Portieri","Slot Difensori","Slot Centrocampisti","Slot Attaccanti"]
    files = [('Csv Files', '*.csv'),
        ('All Files', '*.*')]
    
    salvataggio= filedialog.asksaveasfile(filetypes=files,defaultextension=('Csv Files', '*.csv'),mode='a')
    with open(salvataggio.name, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for partecipante in partecipanti:
            nome=[partecipante.nome]
            for info in partecipante.portieri:
                scrivi=nome+info
                writer.writerow(scrivi)
            for info in partecipante.difensori:
                scrivi=nome+info
                writer.writerow(scrivi)
            for info in partecipante.centrocampisti:
                scrivi=nome+info
                writer.writerow(scrivi)
            for info in partecipante.attaccanti:
                scrivi=nome+info
                writer.writerow(scrivi)
        writer.writerow(finale)
        for partecipante in partecipanti:
            scrivi=[partecipante.nome,partecipante.crediti,partecipante.slot_portieri,partecipante.slot_difensori,partecipante.slot_centrocampisti,partecipante.slot_attaccanti]
            writer.writerow(scrivi)



    
#bottone stampa 
bottone_stampa=tk.Button(root,text="Stampa Excel",bd=3,width=20,bg=second_color,relief="raised",fg=main_color,borderwidth=0,height=2,command=stampa)
bottone_stampa.grid(column=1,row=8,padx=10,pady=50)

def riordina(selezione,lista):
    lista.delete(0,lista.size()-1)
    if selezione == "Cognome":
        cursore.execute("select * from calciatori order by cognome desc")
        c=0
        for i in cursore:
            lista.insert(c,i)

    if selezione == "Ruolo":
        cursore.execute("select * from calciatori order by Ruolo desc")
        c=0
        for i in cursore:
            lista.insert(c,i)

    if selezione == "Club":
        cursore.execute("select * from calciatori order by Squadra desc")
        c=0
        for i in cursore:
            lista.insert(c,i)


def ricercaListone(selezione,ricerca,lista):
    print("ok")
    lista.delete(0,lista.size()-1)
    if selezione == "Cognome":
        cursore.execute(f"select Ruolo,Cognome,Squadra,Quotazione from calciatori where Cognome = '{ricerca.upper()}' COLLATE NOCASE")
        c=0
        for i in cursore:
            lista.insert(c,i)

    if selezione == "Ruolo":
        if ricerca.upper()=="ATTACCANTE":
            ricerca="A"
        if ricerca.upper()=="DIFENSORE":
            ricerca="D"
        if ricerca.upper()=="PORTIERE":
            ricerca="P"
        if ricerca.upper()=="CENTROCAMPISTA":
            ricerca="C"
        cursore.execute(f"select Ruolo,Cognome,Squadra,Quotazione from calciatori where Ruolo = '{ricerca.upper()}'")
        c=0
        for i in cursore:
            lista.insert(c,i)

    if selezione == "Club":
        cursore.execute(f"select Ruolo,Cognome,Squadra,Quotazione from calciatori where Squadra = '{ricerca}' COLLATE NOCASE")
        c=0
        for i in cursore:
            lista.insert(c,i)

def listone():
    new_window=Toplevel(root)
    new_window.geometry("600x600")
    new_window.config(bg=main_color)
    new_window.iconphoto(False,logo)
    
    #label filtri
    label_filtri= tk.Label(new_window,text="Cerca per:",font=("Times bold", 14),bg=main_color,fg=text_color)
    label_filtri.grid(column=0,row=0,padx=15,sticky="W")
    #compbo filtri
    combo_filtri=ttk.Combobox(new_window,values=["Cognome","Ruolo","Club"])
    combo_filtri.bind('<<ComboboxSelected>>', lambda i:riordina(combo_filtri.get(),lista_listone))
    combo_filtri.grid(column=1,row=0,pady=5)

    #entry ricerca
    box_cerca=tk.Entry(new_window,font=("Helvetica", 18),width=20,bg=text_color)
    box_cerca.grid(column=0,row=1,pady=15,padx=15) 

    #bottone
    bottone_cerca=tk.Button(new_window,text="Ricerca",bg=second_color,relief="raised",fg=main_color,borderwidth=0)
    bottone_cerca.bind('<Button-1>',lambda i:ricercaListone(combo_filtri.get(),box_cerca.get(),lista_listone))
    bottone_cerca.grid(column=1,row=1,sticky="W")

    #listone
    lista_listone=tk.Listbox(new_window,width=76,height=30,bg=text_color)
    lista_listone.grid(column=0,row=2,padx=10,pady=10,columnspan=2)
    

#bottone listone
bottone_listone=tk.Button(root,text="Lista Giocatori",bd=3,width=20,bg=second_color,relief="raised",fg=main_color,borderwidth=0,height=2,command=listone)
bottone_listone.grid(column=1,row=4)


if __name__=="__main__":
    root.mainloop()


