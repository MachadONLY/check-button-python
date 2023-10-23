from tkinter import *

def muda_imagem():
    selecoes = [shoutmon.get(), ballistamon.get(), dorulumon.get()]
    fusoes = {
        (True, True, True): "./digimons/shoutmonX5.png",
        (True, True, False): "./digimons/shoutmonX2.png",
        (True, False, True): "./digimons/shoutmonX3.png",
        (False, True, True): "./digimons/shoutmonX4.png",
        (True, False, False): "./digimons/shoutmon.png",
        (False, True, False): "./digimons/ballistamon.png",
        (False, False, True): "./digimons/dorulumon.png",
        (False, False, False): "./digimons/desconhecido.png"
    }
    
    nova_imagem = fusoes[tuple(selecoes)]
    imagem["file"] = nova_imagem
    atualiza_rotulos(selecoes)

def atualiza_rotulos(selecoes):
    rotulo_selecionados["text"] = "Digimons selecionados: " + ", ".join([nome for nome, selecionado in zip(["Shoutmon", "Ballistamon", "Dorulumon"], selecoes) if selecionado])

window = Tk()
window.title("O Programa da Fusão")
window.geometry("700x500")

ballistamon = BooleanVar()
dorulumon = BooleanVar()
shoutmon = BooleanVar()

container1 = Frame(window)
container2 = Frame(window)
container1.pack(side=LEFT, padx=50)
container2.pack(pady=100)

check_ballistamon = Checkbutton(container1, text="Ballistamon", variable=ballistamon, command=muda_imagem)
check_dorulumon = Checkbutton(container1, text="Dorulumon", variable=dorulumon, command=muda_imagem)
check_shoutmon = Checkbutton(container1, text="Shoutmon", variable=shoutmon, command=muda_imagem)

check_ballistamon.grid(row=0, column=0)
check_dorulumon.grid(row=1, column=0)
check_shoutmon.grid(row=2, column=0)

rotulo_selecionados = Label(container1, text="Digimons selecionados:")
rotulo_selecionados.grid(row=3, column=0)

imagem = PhotoImage(file="./digimons/desconhecido.png")
imagemDesconhecido = Label(container2)
imagemDesconhecido["image"] = imagem
imagemDesconhecido.pack()

window.mainloop()
