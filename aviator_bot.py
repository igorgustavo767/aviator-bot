from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
import time 
import sqlite3
url = "https://aviator-next.spribegaming.com/?user=4000005242980&token=3034828b853c8b51fabd0f2a627ae7aef6952fa999cddfb77b070f57beafb4dd&lang=pt&currency=BRL&operator=SoftSwiss_blazecombr&return_url=https%3A%2F%2Fblaze.bet.br&ip=2804%3A631c%3A850d%3A3600%3Ae921%3A2d03%3Ab87b%3A57ed&nickname=FlorescenteAlegria&client_type=mobile"
options = Options() 
options.add_argument("--headless") 
options.add_argument("--disable-gpu") 
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=options)
driver.get(url)
# Conecta ou cria o banco de dados Aguarda o 
# carregamento da página
# Conecta ou cria o banco de dados
conn = sqlite3.connect("aviator.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS resultados (id INTEGER PRIMARY KEY AUTOINCREMENT, valor TEXT, horario DATETIME DEFAULT CURRENT_TIMESTAMP)")
conn.cursor()# Tenta capturar o valor da rodada 
cursor = conn.cursor()
# não existirtry: Cria a tabela se não 
# existircursor.execute("CREATE TABLE IF NOT 
# EXISTS resultados (id INTEGER PRIMARY KEY 
# AUTOINCREMENT, valor TEXT, horario DATETIME 
# DEFAULT CURRENT_TIMESTAMP)") valor = 
# driver.find_element(By.XPATH,
cursor.execute("CREATE TABLE IF NOT EXISTS resultados (id INTEGER PRIMARY KEY AUTOINCREMENT, valor TEXT, horario DATETIME DEFAULT CURRENT_TIMESTAMP)") 
try:
    valor = driver.find_element(By.XPATH, "//div[55555contains(text(),'x')]").text
    print("Valor capturado:", valor)
    cursor.execute("INSERT INTO resultados (valor) VALUES (?)", (valor,))
    conn.commit() 
except:
    print("Erro ao capturar valor")
