from tkinter import *
import math


def actualizar(exp, val, visualizar):
    op = ['+','-','x','/','%']
    if(val in op):
        if(exp.snd == False):
            exp.valor += val
            exp.snd = True            
    elif(val == 'AC'):
        exp.valor = ""
        exp.snd = False
    elif(val == 'CE'):
        if(exp.valor[len(exp.valor)-1] in op):
            exp.snd = False
        exp.valor = exp.valor[:-1]
    #elif (val == 'ans'):
    #    exp.valor = exp.anterior
    #    #print('entre')
    else:
        exp.valor += val
    visualizar.delete(0,END)
    visualizar.insert(0,exp.valor)
    #print(exp.valor)

def calcular(exp,visualizar):
    if(exp.snd == True):
        if('+' in exp.valor):
            exp.anterior = str(int(exp.valor.split('+')[0]) + int(exp.valor.split('+')[1]))
        elif('-' in exp.valor):
            exp.anterior = str(int(exp.valor.split('-')[0]) - int(exp.valor.split('-')[1]))
        elif('x' in exp.valor):
            exp.anterior = str(int(exp.valor.split('x')[0]) * int(exp.valor.split('x')[1]))
        elif('/' in exp.valor):
            exp.anterior = str(int(exp.valor.split('/')[0]) / int(exp.valor.split('/')[1]))
        elif('%' in exp.valor):
            exp.anterior = str(int(exp.valor.split('%')[0]) % int(exp.valor.split('%')[1]))
        
        visualizar.delete(0,END)
        visualizar.insert(0,exp.anterior)
        
        exp.valor = ""
        exp.snd = False



class Expresion():
    def __init__(self):
        self.snd = False
        self.valor = ""
        self.anterior = ""


class Ventana():
    
    def __init__(self, master):
        self.exp = Expresion()
        

        self.ancho  = master.winfo_screenwidth() 
        self.alto = master.winfo_screenheight() 
        #master.geometry(f'{int(self.ancho/4)}x{int(self.alto/2)}')
        master.title("Calculadora")

        self.cajaInput = Entry(master)
        self.cajaInput.grid(row=0, column=0,columnspan=4)
        
        ac = Button(master, text="AC",command=lambda: actualizar(self.exp,'AC',self.cajaInput), bg='#6bbedf')
        ac.grid(row=1, column=0, sticky='nesw')

        ce = Button(master, text="CE",command=lambda: actualizar(self.exp,'CE',self.cajaInput),bg='#6bbedf')
        ce.grid(row=1, column=1, sticky='nesw')

        porcentaje = Button(master, text="%",command=lambda: actualizar(self.exp,'%',self.cajaInput),bg='#6bbedf')
        porcentaje.grid(row=1, column=2, sticky='nesw')

        div = Button(master, text="/",command=lambda: actualizar(self.exp,'/',self.cajaInput),bg='#6bbedf')
        div.grid(row=1, column=3, sticky='nesw')

        siete = Button(master, text="7",command=lambda: actualizar(self.exp,'7',self.cajaInput), bg='#7ad9ff')
        siete.grid(row=2, column=0, sticky='nesw')

        ocho = Button(master, text="8",command=lambda: actualizar(self.exp,'8',self.cajaInput), bg='#7ad9ff')
        ocho.grid(row=2, column=1, sticky='nesw')

        nueve = Button(master, text="9",command=lambda: actualizar(self.exp,'9',self.cajaInput), bg='#7ad9ff')
        nueve.grid(row=2, column=2, sticky='nesw')

        mult = Button(master, text="x",command=lambda: actualizar(self.exp,'x',self.cajaInput),bg='#6bbedf')
        mult.grid(row=2, column=3, sticky='nesw')

        cuatro = Button(master, text="4",command=lambda: actualizar(self.exp,'4',self.cajaInput), bg='#7ad9ff')
        cuatro.grid(row=3, column=0, sticky='nesw')

        cinco = Button(master, text="5",command=lambda: actualizar(self.exp,'5',self.cajaInput), bg='#7ad9ff')
        cinco.grid(row=3, column=1, sticky='nesw')

        seis = Button(master, text="6",command=lambda: actualizar(self.exp,'6',self.cajaInput), bg='#7ad9ff')
        seis.grid(row=3, column=2, sticky='nesw')  

        menos = Button(master, text="-",command=lambda: actualizar(self.exp,'-',self.cajaInput),bg='#6bbedf')
        menos.grid(row=3, column=3, sticky='nesw')

        uno = Button(master, text="1",command=lambda: actualizar(self.exp,'1',self.cajaInput), bg='#7ad9ff')
        uno.grid(row=4, column=0, sticky='nesw')

        dos = Button(master, text="2",command=lambda: actualizar(self.exp,'2',self.cajaInput), bg='#7ad9ff')
        dos.grid(row=4, column=1, sticky='nesw')

        tres = Button(master, text="3",command=lambda: actualizar(self.exp,'3',self.cajaInput), bg='#7ad9ff')
        tres.grid(row=4, column=2, sticky='nesw')

        suma = Button(master, text="+",command=lambda: actualizar(self.exp,'+',self.cajaInput),bg='#6bbedf')
        suma.grid(row=4, column=3, sticky='nesw')

        cero = Button(master, text="0",command=lambda: actualizar(self.exp,'0',self.cajaInput), bg='#7ad9ff')
        cero.grid(row=5, column=0, sticky='nesw')

        ans = Button(master, text="ans", bg='#7ad9ff')#,command=lambda: actualizar(self.exp,'ans',self.cajaInput))
        ans.grid(row=5, column=1, sticky='nesw')

        igual = Button(master, text="=",command=lambda: calcular(self.exp,self.cajaInput), bg='#FFA07A')
        igual.grid(row=5, column=2, columnspan=2, sticky='nesw')

root = Tk()
obj = Ventana(root)


root.mainloop()