import tkinter as tk
import subprocess
import requests
import threading
import time

# ==========================================
# FUNÇÃO CONECTAR PPPoE
# ==========================================

def conectar():

    conexao = entrada_conexao.get()
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    status_label.config(
        text="Discando PPPoE...",
        fg="orange"
    )

    comando = f'rasdial "{conexao}" {usuario} {senha}'

    resultado = subprocess.run(
        comando,
        shell=True,
        capture_output=True,
        text=True
    )

    saida = resultado.stdout + resultado.stderr

    texto_saida.insert(tk.END, saida + "\n")

    # ==========================================
    # VERIFICA SE CONECTOU
    # ==========================================

    if "Conectado" in saida or "Command completed successfully" in saida:

        status_label.config(
            text="PPPoE Conectado",
            fg="green"
        )

        texto_saida.insert(
            tk.END,
            "\nPPPoE autenticado com sucesso\n\n"
        )

    else:

        status_label.config(
            text="Falha ao conectar",
            fg="red"
        )

        texto_saida.insert(
            tk.END,
            "\nERRO AO DISCAR PPPoE\n\n"
        )

# ==========================================
# TESTE DE INTERNET
# ==========================================

def testar_navegacao():

    status_label.config(
        text="Testando navegação...",
        fg="blue"
    )

    try:

        requests.get(
            "https://google.com",
            timeout=5
        )

        texto_saida.insert(
            tk.END,
            "OK - Navegação funcionando\n"
        )

        status_label.config(
            text="Internet OK",
            fg="green"
        )

    except:

        texto_saida.insert(
            tk.END,
            "SEM INTERNET\n"
        )

        status_label.config(
            text="Sem internet",
            fg="red"
        )

# ==========================================
# TESTE DNS
# ==========================================

def testar_dns():

    status_label.config(
        text="Testando DNS...",
        fg="blue"
    )

    try:

        requests.get(
            "https://cloudflare.com",
            timeout=5
        )

        texto_saida.insert(
            tk.END,
            "DNS OK\n"
        )

        status_label.config(
            text="DNS funcionando",
            fg="green"
        )

    except:

        texto_saida.insert(
            tk.END,
            "FALHA DNS\n"
        )

        status_label.config(
            text="Falha DNS",
            fg="red"
        )

# ==========================================
# DESCONECTAR
# ==========================================

def desconectar():

    conexao = entrada_conexao.get()

    subprocess.run(
        f'rasdial "{conexao}" /disconnect',
        shell=True
    )

    status_label.config(
        text="PPPoE desconectado",
        fg="orange"
    )

    texto_saida.insert(
        tk.END,
        "PPPoE desconectado\n"
    )

# ==========================================
# THREADS
# ==========================================

def iniciar_conexao():
    threading.Thread(target=conectar).start()

def iniciar_teste():
    threading.Thread(target=testar_navegacao).start()

def iniciar_dns():
    threading.Thread(target=testar_dns).start()

# ==========================================
# JANELA
# ==========================================

janela = tk.Tk()

janela.title("Toolkit PPPoE Vitor Barbosa")

janela.geometry("600x500")

# ==========================================
# CAMPOS
# ==========================================

tk.Label(
    janela,
    text="Nome da conexão PPPoE"
).pack()

entrada_conexao = tk.Entry(
    janela,
    width=40
)

entrada_conexao.pack()

tk.Label(
    janela,
    text="Usuário PPPoE"
).pack()

entrada_usuario = tk.Entry(
    janela,
    width=40
)

entrada_usuario.pack()

tk.Label(
    janela,
    text="Senha PPPoE"
).pack()

entrada_senha = tk.Entry(
    janela,
    show="*",
    width=40
)

entrada_senha.pack()

# ==========================================
# BOTÕES
# ==========================================

btn_conectar = tk.Button(
    janela,
    text="Conectar PPPoE",
    width=25,
    command=iniciar_conexao
)

btn_conectar.pack(pady=5)

btn_testar = tk.Button(
    janela,
    text="Testar Navegação",
    width=25,
    command=iniciar_teste
)

btn_testar.pack(pady=5)

btn_dns = tk.Button(
    janela,
    text="Testar DNS",
    width=25,
    command=iniciar_dns
)

btn_dns.pack(pady=5)

btn_desconectar = tk.Button(
    janela,
    text="Desconectar PPPoE",
    width=25,
    command=desconectar
)

btn_desconectar.pack(pady=5)

# ==========================================
# STATUS
# ==========================================

status_label = tk.Label(
    janela,
    text="Aguardando...",
    fg="blue",
    font=("Arial", 12, "bold")
)

status_label.pack(pady=10)

# ==========================================
# LOGS
# ==========================================

texto_saida = tk.Text(
    janela,
    width=70,
    height=15
)

texto_saida.pack(pady=10)

# ==========================================
# LOOP
# ==========================================

janela.mainloop()