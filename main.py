from tkinter import *
import tkinter

# cores
cor1 = "#0a0a0a"  # black / preta
cor2 = "#fafcff"  # white / branca
cor3 = "#21c25c"  # green / verde
cor4 = "#eb463b"  # red / vermelha
cor5 = "#dedcdc"  # gray / Cizenta
cor6 = "#3080f0"  # blue / azul

# Configurando a janela
janela = Tk()
janela.title("")
janela.geometry("300x180")
janela.configure(bg=cor1)
janela.resizable(width=FALSE, height=FALSE)

# Definindo variaveis globais
global tempo
global rodar
global contador
global limitador

limitador = 59

tempo = "00:00:00"
rodar = False
contador = -5

# Funcao iniciar


def iniciar():
    global tempo
    global contador
    global limitador
    if rodar:
        # antes do cronometro começar
        if contador <= -1:
            inicio = 'Comecando em ' + str(contador)
            label_tempo['text'] = inicio
            label_tempo['font'] = 'Arial 10'

        # rodando o cronometro
        else:
            label_tempo['font'] = 'Times 50 bold'

            temporaria = str(tempo)
            h, m, s = map(int, temporaria.split(":"))
            h = int(h)
            m = int(m)
            s = int(contador)

            if (s >= limitador):
                contador = 0
                m += 1
            s = str(0)+str(s)
            m = str(0)+str(m)
            h = str(0)+str(h)

            # Atualizando os valores atuais
            temporaria = str(h[-2:]) + ":" + str(m[-2:]) + ":" + str(s[-2:])
            label_tempo['text'] = temporaria
            tempo = temporaria

        label_tempo.after(1000, iniciar)
        contador += 1
# Funcao para dar inicio


def start():
    global rodar
    rodar = True
    iniciar()

# Funcao pausar


def pausar():
    global rodar
    rodar = False

# Funcao reiniciar


def reiniciar():
    global contador
    global tempo

    # Reiniciando o contador
    contador = 0

    # Reiniciando o tempo
    tempo = "00:00:00"
    label_tempo['text'] = tempo


# Criando label
label_app = Label(janela, text='Cronometro',
                  font=("Arial 10"), bg=cor1, fg=cor2)
label_app.place(x=20, y=5)

label_tempo = Label(janela, text=tempo,
                    font=("Times 50 bold"), bg=cor1, fg=cor4)
label_tempo.place(x=20, y=30)

# Criando botões
botao_iniciar = Button(janela, command=start, text='Iniciar', width=10,
                       height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief='raised', overrelief=RIDGE)
botao_iniciar.place(x=20, y=130)

botao_pausar = Button(janela, command=pausar, text='Pausar', width=10,
                      height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief='raised', overrelief=RIDGE)
botao_pausar.place(x=105, y=130)

botao_reiniciar = Button(janela, command=reiniciar, text='Reiniciar', width=10,
                         height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief='raised', overrelief=RIDGE)
botao_reiniciar.place(x=190, y=130)

janela.mainloop()
