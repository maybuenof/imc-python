from tkinter import * 

class Imc:
    def __init__(self, master):
        self.master = master
        master.title("Cálculo do IMC - Índice de Massa Corporal")

        self.patient_name = Label(master, text="Nome do paciente:")
        self.patient_name.grid(row=0, column=0, pady = 5, padx = 10)

        self.full_adress = Label(master, text="Endereço Completo:")
        self.full_adress.grid(row=1, column=0, pady = 2, padx = 10)

        self.label_height = Label(master, text="Altura (m):")
        self.label_height.grid(row=2, column=0, pady = 2, ipadx = 30)

        self.label_weight = Label(master, text="Peso (kg):")
        self.label_weight.grid(row=3, column=0, pady = 2, ipadx = 30)

        self.label_result = Label(master, text="Resultado:")
        self.label_result.grid(row=2, column=2)

        self.entry_patient_name = Entry(master)
        self.entry_patient_name.grid(row=0, column=1, ipadx= 50)

        self.entry_full_adress = Entry(master)
        self.entry_full_adress.grid(row=1, column=1, ipadx= 50)

        self.entry_height = Entry(master)
        self.entry_height.grid(row=2, column=1, ipadx= 20)

        self.entry_weight = Entry(master)
        self.entry_weight.grid(row=3, column=1, ipadx= 20)

        self.entry_result = Entry(master)
        self.entry_result.grid(row=2, column=3, padx = 20, ipady = 20)

        self.button_calculate = Button(master, text="Calcular", command=self.calculate)
        self.button_calculate.grid(row=6, column=1, pady = 20, padx = 20)

        self.restart_button = Button(master, text="Reiniciar", command=self.restart)
        self.restart_button.grid(row=6, column=0, pady = 20, padx = 20)

        self.close_button = Button(master, text="Fechar", command=self.quit)
        self.close_button.grid(row=6, column=2, pady = 20, padx = 20)

    def quit(self):
        self.master.quit()

    def restart(self):
        self.entry_patient_name.delete(0, END)
        self.entry_full_adress.delete(0, END)
        self.entry_height.delete(0, END)
        self.entry_weight.delete(0, END)
        self.entry_result.delete(0, END)

    def calculate(self):
        height = float(self.entry_height.get())
        weight = float(self.entry_weight.get())
        result = weight / (height * height)
        self.entry_result.delete(0, END)
        if result < 17:
            self.entry_result.insert(0, "Muito abaixo do peso")
        elif result >= 17 and result < 18.5:
            self.entry_result.insert(0, "Abaixo do peso")
        elif result >= 18.5 and result < 25:
            self.entry_result.insert(0, "Peso normal")
        elif result >= 25 and result < 30:
            self.entry_result.insert(0, "Acima do peso")
        elif result >= 30 and result < 35:
            self.entry_result.insert(0, "Obesidade I")
        elif result >= 35 and result < 40:
            self.entry_result.insert(0, "Obesidade II (severa)")
        elif result >= 40:
            self.entry_result.insert(0, "Obesidade III (mórbida)")


root = Tk()
Imc(root)
root.mainloop()