# coding: utf-8

from Tkinter import *
import ImageTk, random


class Meny(Frame):
    global app2
    
    def __init__(self, master):
        Frame.__init__(self, master)
        
        self.visa_meny()
        
    #Skapar innehållet till och visar en meny
    def visa_meny(self):
        self.starta_spel = Button(self, text = "Starta spelet", command = self.starta)
        self.starta_spel.grid(row = 1, sticky = W+E)
        self.info = Label(self, text = "Välkommen till metal-quiz, frågesportsspelet om tung musik! Reglerna är enkla, du får 50 poäng för varje rätt svar och om du svarar fel har du förlorat. Nu kör vi!",
                          height=7, wraplength = 300)
        self.info.grid(row = 0)
        self.pack(fill=BOTH, expand=1)
    
    #Startar spelet    
    def starta(self):
        self.pack_forget()
        app2.starta()

class Spel(Frame):
    global app
  
    #Skapar variabler och grafiska komponenter till spelet
    def __init__(self, master):
        Frame.__init__(self, master)   
         
        self.master = master
        
        self.poang = 0
        
        self.svar = StringVar()
        self.svar.set(None)
        
        self.svar_a = StringVar()
        self.svar_b = StringVar()
        self.svar_c = StringVar()
        self.svar_d = StringVar()
        
        self.master.title("Metal-quiz")
        
        self.bild = Label(self, width = 295)
        
        self.visa_poang = Label(self)
        
        self.fraga = Label(self)
        
        self.svara = Button(self, text="Svara", command = self.svarat)
        
        self.starta_omknapp = Button(self, text="Starta om", padx=0, command = self.starta_om)
        
        self.sluttext = Label(self, height = 16, width = 36)
        
        self.menyknapp = Button(self, text="Meny", command = self.meny)
        self.menyknapp.grid(row = 7, column = 1, sticky = W+E)
        
        self.avsluta = Button(self, text="Avsluta", command = self.quit)
        self.avsluta.grid(row = 7, column = 2, sticky = W+E)
        
        Radiobutton(self,
                    textvariable = self.svar_a,
                    variable = self.svar,
                    value = "A",
                    ).grid(row = 3, column = 1, sticky = W)
        
        Radiobutton(self,
                    textvariable = self.svar_b,
                    variable = self.svar,
                    value = "B",
                    ).grid(row = 4, column = 1, sticky = W)
                    
        Radiobutton(self,
                    textvariable = self.svar_c,
                    variable = self.svar,
                    value = "C",
                    ).grid(row = 5, column = 1, sticky = W)
                    
        Radiobutton(self,
                    textvariable = self.svar_d,
                    variable = self.svar,
                    value = "D",
                    ).grid(row = 6, column = 1, sticky = W)
    
    #Startar spelet    
    def starta(self):
        self.poang = 0
        self.index = random.randint(0,3)
        
        #Hämtar in en slumpvis vald fråga
        fraga = open("fråga" + str(self.index) + ".txt", "r")
        self.aktuell_fraga = fraga.read()
        fraga.close()
        
        #Hämtar in alternativ och svar till frågan
        alternativ = open("alternativ" + str(self.index) + ".txt", "r")
        self.alternativ_svar = alternativ.readlines()
        alternativ.close()
        
        #Sätter värdet för rätt svar
        self.ratt_svar = self.alternativ_svar[4]
        
        #Hämtar in bild kopplad till frågan
        self.tkbild = ImageTk.PhotoImage(file = "image" + str(self.index) + ".jpg")
        
        #Ser till att rätt alternativ visas
        self.svar_a.set(self.alternativ_svar[0])
        self.svar_b.set(self.alternativ_svar[1])
        self.svar_c.set(self.alternativ_svar[2])
        self.svar_d.set(self.alternativ_svar[3])
        
        self.visa_poang.configure(text = "Poäng: " + str(self.poang))
        self.bild.configure(image = self.tkbild)
        self.fraga.configure(text = self.aktuell_fraga)
        
        self.bild.grid(row = 1, columnspan = 3, sticky = W+E)
        self.visa_poang.grid(row = 0, columnspan = 3, sticky = W)
        self.fraga.grid(row = 2, column = 0, columnspan = 3, sticky = W)
        self.svara.grid(row = 7, column = 0, sticky = W+E)
        
        self.pack(fill=BOTH, expand=1)
        
    
    def svarat(self):
        #Om svaret är rätt ökas poängen med 50 och ny fråga hämtas
        if str(self.svar.get()) == self.ratt_svar:
            self.poang += 50
            self.index = random.randint(0,3)
        
            fraga = open("fråga" + str(self.index) + ".txt", "r")
            self.aktuell_fraga = fraga.read()
            fraga.close()
        
            alternativ = open("alternativ" + str(self.index) + ".txt", "r")
            self.alternativ_svar = alternativ.readlines()
            alternativ.close()
        
            self.ratt_svar = self.alternativ_svar[4]
        
            self.tkbild = ImageTk.PhotoImage(file = "image" + str(self.index) + ".jpg")
            
            self.svar_a.set(self.alternativ_svar[0])
            self.svar_b.set(self.alternativ_svar[1])
            self.svar_c.set(self.alternativ_svar[2])
            self.svar_d.set(self.alternativ_svar[3])
            
            self.bild.configure(image = self.tkbild)
            
            self.fraga.configure(text = self.aktuell_fraga)
            
            self.visa_poang.configure(text = "Poäng: " + str(self.poang))
        else:
            self.fel_svar() 
            
    #Avslutar spelet och återvänder till menyn
    def meny(self):
        self.sluttext.grid_forget()
        self.starta_omknapp.grid_forget()
        self.pack_forget()
        app.visa_meny()
        
    #Visar slutgiltig poäng och en knapp för att starta om spelet
    def fel_svar(self):
        self.svara.grid_forget()
        self.bild.grid_forget()
        self.visa_poang.grid_forget()
        self.fraga.grid_forget()
        self.sluttext.configure(text = "Fel svar! Du fick " + str(self.poang) + " poäng")
        self.sluttext.grid(row = 0, columnspan = 3)
        self.starta_omknapp.grid(row = 7, column = 0, sticky = W+E)
        
    #Startar om spelet
    def starta_om(self):
        self.starta_omknapp.grid_forget()
        self.svara.grid(row = 7, column = 0, sticky = W+E)
        self.sluttext.grid_forget()
        self.starta()
          

def main():
    
    global app
    global app2
  
    root = Tk()
    root.geometry("295x425")
    app = Meny(root)
    app2 = Spel(root)
    root.mainloop()  


main()