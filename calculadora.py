import tkinter as tk

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("402x580")
        self.root.resizable(False, False)
        self.root.configure(bg='#f3f3f3')
        self.root.iconbitmap("assets/Calculator.ico")# adicionei icone (:

        self.expression = ""
        self.resultado = tk.StringVar()

        self.criar_interface()

    def criar_interface(self):
        # Visor ampliado
        tela = tk.Entry(self.root, textvariable=self.resultado, font=('Segoe UI', 32), justify='right', bd=0, bg='#f3f3f3', relief='flat')
        tela.place(x=10, y=20, width=382, height=214)

        botoes = [
            ('C', '⌫', '%', '/'),
            ('7', '8', '9', '*'),
            ('4', '5', '6', '-'),
            ('1', '2', '3', '+'),
            ('±', '0', '.', '=')
        ]

        cores = {
            'numerico': '#fcfcfc',
            'operador': '#f6f6f6',
            '=': '#1975c5'
        }

        for i, linha in enumerate(botoes):
            for j, simbolo in enumerate(linha):
                if simbolo.isdigit() or simbolo == '.':
                    cor = cores['numerico']
                elif simbolo == '=':
                    cor = cores['=']
                else:
                    cor = cores['operador']

                botao = tk.Button(self.root, text=simbolo,
                                  command=lambda s=simbolo: self.clique(s),
                                  font=('Segoe UI', 14), bd=0,
                                  bg=cor, fg='black',
                                  activebackground='#dcdcdc')
                x = 10 + j * 96
                y = 254 + i * 66
                botao.place(x=x, y=y, width=94, height=56)

    def clique(self, simbolo):
        if simbolo == 'C':
            self.expression = ""
            self.resultado.set("")
        elif simbolo == '⌫':
            self.expression = self.expression[:-1]
            self.resultado.set(self.expression)
        elif simbolo == '=':
            try:
                resultado_final = eval(self.expression.replace('%', '/100'))
                self.resultado.set(str(resultado_final))
                self.expression = str(resultado_final)
            except:
                self.resultado.set("Erro")
                self.expression = ""
        elif simbolo == '±':
            if self.expression and self.expression[0] == '-':
                self.expression = self.expression[1:]
            else:
                self.expression = '-' + self.expression
            self.resultado.set(self.expression)
        else:
            self.expression += simbolo
            self.resultado.set(self.expression)

if __name__ == "__main__":
    import ctypes
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()
