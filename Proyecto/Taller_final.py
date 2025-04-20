import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC    
from selenium.webdriver.support.ui import WebDriverWait
import time

ruta_descargas = r"C:/Users/Santiago/Desktop/UCompensar/Pruebas de Software/Screenshots"

# Crear la carpeta si no existe
if not os.path.exists(ruta_descargas):
    os.makedirs(ruta_descargas)

def tomar_captura(driver, nombre_paso):
    ruta_captura = os.path.join(ruta_descargas, f"{nombre_paso}.png")
    driver.save_screenshot(ruta_captura)
    print(f"Captura Guardada en: {ruta_captura}")


options = webdriver.ChromeOptions()

# Modo headless (nuevo) + tamaño de ventana
options.add_argument("--headless")  

options.add_argument("--window-size=1370,768") 
driver = webdriver.Chrome(options=options)

try:
    # primer punto 
    driver.get("https://demoqa.com/automation-practice-form")
    driver.find_element(By.ID, "firstName").send_keys("Ana")
    driver.find_element(By.ID, "lastName").send_keys("Gómez")
    driver.find_element(By.ID, "userEmail").send_keys("ana.gomez@example.com")
    female = driver.find_element(By.XPATH, "//input[@id='gender-radio-2']")
    female.send_keys(Keys.SPACE)
    driver.find_element(By.ID, "userNumber").send_keys("3124567892")

    time.sleep(3)
    fecha_input = driver.find_element(By.ID, "dateOfBirthInput")
    fecha_input.send_keys(Keys.CONTROL + "a")
    fecha_input.send_keys("30 Jun 1998")
    fecha_input.send_keys(Keys.ENTER)

    wait = WebDriverWait(driver, 3)
    subjects_input = wait.until(EC.presence_of_element_located((By.ID, "subjectsInput")))
    subjects_input.send_keys("Maths")
    subjects_input.send_keys(Keys.ENTER)
    
    driver.find_element(By.XPATH, "//label[text()='Sports']").click()

    driver.find_element(By.ID, "uploadPicture").send_keys(os.path.abspath("C:/Users/Santiago/Desktop/UCompensar/Pruebas de Software/Imagen.jpeg"))
    driver.find_element(By.ID, "currentAddress").send_keys("cra 34 No 65 98")
    
    state_input = driver.find_element(By.ID, "react-select-3-input")
    state_input.send_keys("NCR")
    state_input.send_keys(Keys.ENTER)
    city_input = driver.find_element(By.ID, "react-select-4-input")
    city_input.send_keys("Delhi")
    city_input.send_keys(Keys.ENTER)

    boton = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView();", boton)
    boton.click()
    time.sleep(5)
    tomar_captura(driver, "Formulario" )
    time.sleep(5)

    print("Formulario enviado Correctamente")
    
    #segundo punto
    driver.get("https://demoqa.com/upload-download")
    driver.find_element(By.ID, "uploadFile").send_keys(os.path.abspath("C:/Users/Santiago/Desktop/UCompensar/Pruebas de Software/Imagen.jpeg"))
    descarga = driver.find_element(By.ID, "downloadButton")
    descarga.click()

    tomar_captura(driver, "Cargar archivo" )
    time.sleep(5)

    tomar_captura(driver, "Descargar archivo" )
    

    archivo = os.path.join(os.path.expanduser("~"), "Downloads","sampleFile.jpeg") 
    if os.path.exists(archivo):
        print(f"Archivo descargado correctamente en: {archivo}")
    else:
         print("El archivo no se encuentra en la carpeta de descargas.")

# tercer punto
    driver.get("https://demoqa.com/alerts")  

    confirm_button = driver.find_element(By.ID, "confirmButton")
    if(confirm_button):
        print("Se encontro el boton")
        confirm_button.click()
        WebDriverWait(driver,10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        time.sleep(5)
        alert.accept()

        tomar_captura(driver, "Aceptar boton" )
        
    else:
        print("No se encontro el boton")
    
    send = driver.find_element(By.ID, "promtButton") 
    if(send):
        print("se encontro el boton") 
        send.click()
        WebDriverWait(driver,10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        time.sleep(5)
        alert.send_keys("Hola Mundo!!!")
        time.sleep(5)
        alert.accept() 
        tomar_captura(driver, "Enviar Texto")
        
    else:
        print("no se encontro el boton") 


finally:
    input("presione enter para salir: ")
    driver.quit()