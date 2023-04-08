from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Definir las credenciales de inicio de sesión
usuario = "entique-6520@hotmail.com"
contrasena = "m8QLX2uww+r.f%y"

# Inicializar el controlador de Chrome
driver = webdriver.Chrome()

# Navegar a la página de inicio de Habbo
driver.get("https://www.habbo.es/")

# Esperar a que se cargue la página
time.sleep(3)

# Verificar si el botón de "Rechazarlas todas" está presente en la página
try:
    btn_rechazar = driver.find_element(By.XPATH, "//button[contains(.,'Rechazarlas todas')]")
    btn_rechazar.click()
    print("Cookies rechazadas.")
except:
    print("No se encontró el botón de rechazo de cookies.")


# Escribir el nombre de usuario en el campo correspondiente
campo_usuario = driver.find_element(By.XPATH, "//input[contains(@name,'email')]")
campo_usuario.send_keys(usuario)

# Escribir la contraseña en el campo correspondiente
campo_contrasena = driver.find_element(By.XPATH, "//input[contains(@name,'password')]")
campo_contrasena.send_keys(contrasena)

# Hacer clic en el botón de "Iniciar sesión"
btn_ingresar = driver.find_element(By.XPATH, "//button[@ng-disabled='LoginController.loginInProgress'][contains(.,'Conectar')]")
btn_ingresar.click()

# esperar 5 segundos antes de buscar el botón de omitir
time.sleep(5)

# Esperar hasta que el botón de "Omitir" del captcha esté visible y hacer clic en él
try:
    omitir_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[3]/div[3]")))
    omitir_btn.click()
    print("Se ha hecho clic en el botón Omitir del captcha.")
except:
    print("No se pudo hacer clic en el botón Omitir del captcha.")


# Esperar a que se inicie sesión
time.sleep(5)

# Verificar que se haya iniciado sesión correctamente
if "Bienvenido" in driver.page_source:
    print("Inicio de sesión exitoso!")
else:
    print("Inicio de sesión fallido.")

# Cerrar la ventana del navegador
driver.quit()
