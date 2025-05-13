import tkinter as tk
from tkinter import messagebox
import serial
import serial.tools.list_ports

# ---------- CONFIGURAÇÕES ----------
PORTA = "COM5"  # Altere aqui para a COM certa
BAUD = 9600

# ---------- CONEXÃO SERIAL ----------
try:
    ser = serial.Serial(PORTA, BAUD)
except:
    ser = None
    print("⚠️ Erro ao conectar na porta. Verifique a COM.")
    messagebox.showwarning("Erro", "Não foi possível conectar na porta COM.")

# ---------- FUNÇÃO PARA ENVIAR COMANDOS ----------
def enviar_comando(cmd):
    if ser and ser.is_open:
        ser.write(cmd.encode())
        status_var.set(f"Enviado: {cmd}")
    else:
        status_var.set("⚠️ Porta serial não conectada")

# ---------- INTERFACE ----------
janela = tk.Tk()
janela.title("Controle Robô Bluetooth")
janela.geometry("350x350")
janela.configure(bg="#1e1e2f")

# ---------- ESTILOS ----------
estilo_botao = {
    "width": 10,
    "height": 2,
    "font": ("Arial", 12, "bold"),
    "bg": "#4CAF50",
    "fg": "white",
    "activebackground": "#45a049",
    "bd": 0
}

estilo_botao_parar = estilo_botao.copy()
estilo_botao_parar["bg"] = "#f44336"
estilo_botao_parar["activebackground"] = "#da190b"

# ---------- LABEL DE TÍTULO ----------
titulo = tk.Label(janela, text="Controle do Robô", font=("Arial", 16, "bold"), bg="#1e1e2f", fg="white")
titulo.pack(pady=10)

# ---------- FRAME DE BOTÕES ----------
frame_botoes = tk.Frame(janela, bg="#1e1e2f")
frame_botoes.pack(pady=10)

# Linha 1
tk.Label(frame_botoes, bg="#1e1e2f").grid(row=0, column=0)  # Espaço
btn_frente = tk.Button(frame_botoes, text="Frente", command=lambda: enviar_comando('F'), **estilo_botao)
btn_frente.grid(row=0, column=1, pady=5)
tk.Label(frame_botoes, bg="#1e1e2f").grid(row=0, column=2)

# Linha 2
btn_esq = tk.Button(frame_botoes, text="Esquerda", command=lambda: enviar_comando('L'), **estilo_botao)
btn_esq.grid(row=1, column=0, padx=5)

btn_parar = tk.Button(frame_botoes, text="Parar", command=lambda: enviar_comando('S'), **estilo_botao_parar)
btn_parar.grid(row=1, column=1, padx=5)

btn_dir = tk.Button(frame_botoes, text="Direita", command=lambda: enviar_comando('R'), **estilo_botao)
btn_dir.grid(row=1, column=2, padx=5)

# Linha 3
tk.Label(frame_botoes, bg="#1e1e2f").grid(row=2, column=0)
btn_tras = tk.Button(frame_botoes, text="Trás", command=lambda: enviar_comando('B'), **estilo_botao)
btn_tras.grid(row=2, column=1, pady=5)
tk.Label(frame_botoes, bg="#1e1e2f").grid(row=2, column=2)

# ---------- STATUS ----------
status_var = tk.StringVar()
status_var.set("Pronto para comandos")

status_label = tk.Label(janela, textvariable=status_var, font=("Arial", 10), bg="#1e1e2f", fg="#ccc")
status_label.pack(pady=10)

# ---------- FECHAR COM SERIAL ----------
def ao_fechar():
    if ser and ser.is_open:
        ser.close()
    janela.destroy()

janela.protocol("WM_DELETE_WINDOW", ao_fechar)

janela.mainloop()
