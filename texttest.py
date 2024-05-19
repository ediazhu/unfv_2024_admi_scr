
	
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import csv

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Abre la página web deseada
driver.get("https://web4.unfv.edu.pe/Resultado_Admision/2024/pregrado_general/")
codigo_ini= 90000 #
codigo_fin= 90200
for numero in range(codigo_ini, codigo_fin +1):
	#
	# Encuentra el elemento del campo de texto por su ID
	campo_texto = driver.find_element(By.ID, "Txt_Busqueda")

	# Introduce texto en el campo de texto
	
	codigostr = str(numero)

	campo_texto.send_keys(codigostr)

	# Encuentra el botón por su ID
	boton = driver.find_element(By.ID, "Btn_Buscar")
	ActionChains(driver)\
		.click(boton)\
		.perform()
	# Haz clic en el botón
	
	nom_pos = driver.find_element(By.ID, "Lbl_Nombre")
	esc_pos = driver.find_element(By.ID, "Lbl_Especialidad")
	pun_pos = driver.find_element(By.ID, "Lbl_Modalidad")
	con_pos = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/div/table/tbody/tr[5]/td/table/tbody/tr[5]/td/div/table/tbody/tr[2]/td")
	## Generacion de Resultados:
	# Datos de la nueva fila
	nueva_fila = [nom_pos.text, esc_pos.text, pun_pos.text, con_pos.text]

# Abre el archivo CSV en modo de apéndice
	with open("archivo.csv", "a", newline="") as archivo_csv:
			writer = csv.writer(archivo_csv)
			writer.writerow(nueva_fila)
	print(nom_pos.text, esc_pos.text, pun_pos.text, con_pos.text)
	#print(esc_pos.text)
	#print(pun_pos.text)
	#print(con_pos.text)
	
	driver.get(driver.current_url)
	driver.implicitly_wait(5)	#Tiempo cooldown 


	
driver.close()
