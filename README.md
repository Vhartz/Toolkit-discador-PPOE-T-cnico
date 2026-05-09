# PPPoE Toolkit Técnico

Sistema portátil para autenticação PPPoE e diagnóstico rápido de internet desenvolvido para técnicos de redes, provedores ISP e suporte FTTH/FTTx.

---

# Funcionalidades

✅ Autenticação PPPoE via interface gráfica
✅ Teste de navegação
✅ Teste DNS
✅ Desconexão PPPoE
✅ Logs em tempo real
✅ Interface simples e rápida
✅ Aplicação portátil para Windows
✅ Não requer instalação de Python no computador final

---

# Objetivo

O software foi criado para agilizar o dia a dia de técnicos de campo durante:

* instalação FTTH
* manutenção de clientes
* testes de autenticação
* validação de navegação
* testes de DNS
* diagnóstico rápido de conexão

---

# Interface

O sistema possui:

* Campo para nome da conexão PPPoE
* Campo de usuário PPPoE
* Campo de senha
* Botão conectar
* Botão desconectar
* Botão testar navegação
* Botão testar DNS
* Área de logs e retorno técnico

---

# Requisitos

## Para utilizar o executável

* Windows 10 ou superior
* Conexão PPPoE criada no Windows
* Permissões normais de usuário

Nenhuma dependência adicional é necessária.

---

# Como criar uma conexão PPPoE no Windows

1. Painel de Controle
2. Rede e Internet
3. Central de Rede e Compartilhamento
4. Configurar nova conexão
5. Conectar à Internet
6. Banda larga (PPPoE)

Crie uma conexão com o nome desejado.

Exemplo:

```text id="v3jlwm"
PPPOE_TESTE
```

Esse será o nome utilizado dentro do software.

---

# Como usar

1. Abra o programa
2. Digite:

   * nome da conexão PPPoE
   * usuário PPPoE
   * senha PPPoE
3. Clique em:

## Conectar PPPoE

O software irá:

* autenticar
* validar conexão
* mostrar retorno técnico

---

# Testes disponíveis

## Testar Navegação

Realiza teste de acesso externo validando conectividade com a internet.

## Testar DNS

Valida resolução DNS e acesso a domínios externos.

## Desconectar PPPoE

Encerra a sessão PPPoE ativa.

---

# Tecnologias utilizadas

* Python
* Tkinter
* Requests
* Rasdial (Windows)

---

# Compilação

Para gerar o executável:

```bash id="fjlwm9"
py -m PyInstaller --onefile --noconsole ppoetk.py
```

Executável gerado em:

```text id="jlwmc8"
dist/
```

---

# Instalação de dependências

```bash id="8cjlwm"
pip install requests
pip install pyinstaller
```

---

# Estrutura do projeto

```text id="0z9nux"
pppoetk.py
README.md
requirements.txt
```

---

# Melhorias futuras

* Tema dark
* Histórico de testes
* Exportação de logs
* Speedtest integrado
* Ping contínuo
* Identificação de gateway
* Consulta ONU
* Integração MikroTik
* Monitoramento FTTH
* Ferramentas de diagnóstico ISP

---

# Licença

Projeto livre para estudos, melhorias e uso técnico.

---

# Desenvolvido por

Vitor Barbosa
Técnico de Redes e Telecomunicações
Projeto voltado para suporte técnico ISP e FTTH.
