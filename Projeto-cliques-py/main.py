import customtkinter as ctk

class App:
    def __init__(self, master: ctk.CTk):
        self.master = master
        self.master.geometry('400x400') 
        self.master.resizable(True,True) 
        self.master.wm_title('Contador de cliques by David Molizane')
        self.master.iconbitmap('files/py.ico')
        
        #Criar o contador como uma str
        self.counter: str = '0'
        
        #Create a label
        self.label = ctk.CTkLabel(self.master, text=self.counter, font=('Roboto Black', 35))
        self.label.place(relx=0.5, rely=0.4, anchor='center')
        
        #Create a button
        self.button = ctk.CTkButton(self.master, text='Clique aqui!',
                                    command=self.increment, corner_radius=10, font=('Roboto', 20))
        self.button.place(relx=0.5, rely=0.6, anchor='center')
        self.reset_button: ctk.CTkButton | None = None
        
    def increment(self):
        try:
            self.counter = str(int(self.counter) + 1)
            self.label.configure(text=self.counter)
            
            if int(self.counter) == 1:
                self.reset_button = ctk.CTkButton(self.master, text='Resetar', command=self.reset,corner_radius=10, fg_color='red', hover_color='darkred', font=('Roboto', 20))
                self.reset_button.place(relx=0.5, rely = 0.75, anchor='center')
        except Exception as e:
            print('Error:', e)
            
    def reset(self):  
        try:
            self.counter = '0'
            self.label.configure(text=self.counter)
            self.reset_button.destroy()
        except Exception as e:
            print('Error:', e)
        
if __name__ == '__main__':
    app = ctk.CTk()
    gui = App(master=app)
    app.mainloop()   


