import tkinter 
from GeradorDeCNPJ import cnpjGenerator
from GeradorDeCPF import cpfGenerator
from GeradorDePIs import pisGenerator

class Application:
    def __init__(self, master=None):
        self.tela1 = tkinter.Frame()
        self.tela1.pack()
        
        self.mensagem(self)
        self.botao_sair(self)
        self.botao_reload(self)
        self.campos(self)

    #Elementos de tela

    def mensagem(self, widget1):
        self.msg = tkinter.Label(self.tela1, text="Teste Fácil Br")
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg["pady"] = 10
        self.msg.pack()
    
    def botao_sair(self, widget1):
        self.sair = tkinter.Button(self.tela1)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Verdana", "10", "bold")
        self.sair["fg"] = "red"
        self.sair["width"] = 5
        self.sair["command"] = self.mudar_Texto
        self.sair.pack(side=tkinter.RIGHT)

    def botao_reload(self, widget1):
        self.reload = tkinter.Button(self.tela1)
        self.reload["text"] = "Mudar"
        self.reload["font"] = ("Verdana", "10", "bold")
        self.reload["fg"] = "green"
        self.reload["width"] = 5
        self.reload["command"] = self.novo_valor
        self.reload.pack(side=tkinter.RIGHT)

    def botao_sim(self, widget1):
        self.sim = tkinter.Button(self.tela1)
        self.sim["text"] = "Sim"
        self.sim["font"] = ("Verdana", "10", "bold")
        self.sim["width"] = 5
        self.sim["command"] = self.tela1.quit
        self.sim.pack(side=tkinter.RIGHT)

    def botao_nao(self, widget1):
        self.nao = tkinter.Button(self.tela1)
        self.nao["text"] = "Não"
        self.nao["font"] = ("Verdana", "10", "bold")
        self.nao["width"] = 5
        self.nao["command"] = self.opcoes_nao
        self.nao.pack(side=tkinter.RIGHT)

    def campos(self, widget1):
        self.primeiro_conteiner = tkinter.Frame()
        self.primeiro_conteiner["pady"] = 10
        self.primeiro_conteiner =  tkinter.Label(text = ("CPF: ", cpfGenerator()))
        self.primeiro_conteiner.pack(side=tkinter.BOTTOM)
        
        self.segundo_conteiner = tkinter.Frame()
        self.segundo_conteiner["pady"] = 10
        self.segundo_conteiner = tkinter.Label(text = ("CNPJ: ", cnpjGenerator()))
        self.segundo_conteiner.pack(side=tkinter.BOTTOM)

        self.terceiro_conteiner = tkinter.Frame()
        self.terceiro_conteiner["pady"] = 10
        self.terceiro_conteiner = tkinter.Label(text = ("PIS: ", pisGenerator()))
        self.terceiro_conteiner.pack(side = tkinter.BOTTOM) 
 
    #Condição do botão sair

    def mudar_Texto(self):
        if self.msg["text"] == "Teste Fácil Br":
            self.msg["text"] = "Tem certeza?"
            self.sair["command"] = self.sair.forget()
            self.reload["command"] = self.reload.forget()
            self.botao_nao(self.tela1)
            self.botao_sim(self.tela1)
        else:
            self.msg["text"] = "Teste Fácil Br"
        
    #Condição para o botão não

    def opcoes_nao(self):
        if self.nao["text"] == "Não":
            self.msg["text"] = "Teste Fácil Br"
            self.sim["command"] = self.sim.forget()
            self.nao["command"] = self.nao.forget()
        self.botao_sair(self)
        self.botao_reload(self)

    #Novos valores da aplicação

    def novo_valor(self):
        if self.reload["text"] == "Mudar":
            self.primeiro_conteiner["command"] = self.primeiro_conteiner.forget()
            self.segundo_conteiner["command"] = self.segundo_conteiner.forget()
            self.terceiro_conteiner["command"] = self.terceiro_conteiner.forget()
        self.campos(self)

            

        
        

# Criação de tela e epecificações

janela = tkinter.Tk()
Application(janela)
janela.title("Teste Fácil Br")
janela.maxsize(200,500)
janela.mainloop()
