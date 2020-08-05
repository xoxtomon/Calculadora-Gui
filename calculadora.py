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
        master.geometry(f'{int(self.ancho/4)}x{int(self.alto/2)}')
        master.title("Calculadora")

        self.cajaInput = Entry(master)
        self.cajaInput.grid(row=0, column=0,columnspan=4)
        
        ac = Button(master, text="AC",command=lambda: actualizar(self.exp,'AC',self.cajaInput))
        ac.grid(row=1, column=0)

        ce = Button(master, text="CE",command=lambda: actualizar(self.exp,'CE',self.cajaInput))
        ce.grid(row=1, column=1)

        porcentaje = Button(master, text="%",command=lambda: actualizar(self.exp,'%',self.cajaInput))
        porcentaje.grid(row=1, column=2)

        div = Button(master, text="/",command=lambda: actualizar(self.exp,'/',self.cajaInput))
        div.grid(row=1, column=3)

        siete = Button(master, text="7",command=lambda: actualizar(self.exp,'7',self.cajaInput))
        siete.grid(row=2, column=0)

        ocho = Button(master, text="8",command=lambda: actualizar(self.exp,'8',self.cajaInput))
        ocho.grid(row=2, column=1)

        nueve = Button(master, text="9",command=lambda: actualizar(self.exp,'9',self.cajaInput))
        nueve.grid(row=2, column=2)

        mult = Button(master, text="x",command=lambda: actualizar(self.exp,'x',self.cajaInput))
        mult.grid(row=2, column=3)

        cuatro = Button(master, text="4",command=lambda: actualizar(self.exp,'4',self.cajaInput))
        cuatro.grid(row=3, column=0)

        cinco = Button(master, text="5",command=lambda: actualizar(self.exp,'5',self.cajaInput))
        cinco.grid(row=3, column=1)

        seis = Button(master, text="6",command=lambda: actualizar(self.exp,'6',self.cajaInput))
        seis.grid(row=3, column=2)  

        menos = Button(master, text="-",command=lambda: actualizar(self.exp,'-',self.cajaInput))
        menos.grid(row=3, column=3)

        uno = Button(master, text="1",command=lambda: actualizar(self.exp,'1',self.cajaInput))
        uno.grid(row=4, column=0)

        dos = Button(master, text="2",command=lambda: actualizar(self.exp,'2',self.cajaInput))
        dos.grid(row=4, column=1)

        tres = Button(master, text="3",command=lambda: actualizar(self.exp,'3',self.cajaInput))
        tres.grid(row=4, column=2)

        suma = Button(master, text="+",command=lambda: actualizar(self.exp,'+',self.cajaInput))
        suma.grid(row=4, column=3)

        cero = Button(master, text="0",command=lambda: actualizar(self.exp,'0',self.cajaInput))
        cero.grid(row=5, column=0)

        ans = Button(master, text="ans")#,command=lambda: actualizar(self.exp,'ans',self.cajaInput))
        ans.grid(row=5, column=1)

        igual = Button(master, text="=",command=lambda: calcular(self.exp,self.cajaInput))
        igual.grid(row=5, column=2, columnspan=2)

root = Tk()
obj = Ventana(root)


root.mainloop()