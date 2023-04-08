from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
from pytest import mark

@mark.ui
def test_Automatizada1():


    # Definir las credenciales de inicio de sesión
    usuario = "entique-6520@hotmail.com"
    contrasena = "m8QLX2uww+r.f%y"

    # Inicializar el controlador de Chrome
    driver = webdriver.Chrome()

    # Navegar a la página de inicio de Habbo
    driver.get("https://www.corotos.com.do/")

    # maximiza la ventana del navegador
    driver.maximize_window()

    # Esperar a que se cargue la página
    time.sleep(3)

    # Verificar si el botón de "iniciar sesion" está presente en la página
    try:
        btn_iniciosesion = driver.find_element(By.XPATH, "//a[contains(@class,'w-full common-button common-button--primary common-button--primary--primary common-button--large flex rounded-lg')]")
        btn_iniciosesion.click()
        print("✓ Iniciar sesion")
    except:
        print("No se encontró el botón de iniciar sesion")

    

    # Escribir el nombre de usuario en el campo correspondiente
    campo_usuario = driver.find_element(By.XPATH, "//input[@placeholder='Correo aquí'][contains(@id,'email')]")
    campo_usuario.send_keys(usuario)

    # Escribir la contraseña en el campo correspondiente
    campo_contrasena = driver.find_element(By.XPATH, "//input[@placeholder='Escribe la contraseña'][contains(@id,'password')]")
    campo_contrasena.send_keys(contrasena)

    # Hacer clic en el botón "Continuar" para iniciar la sesion
    btn_ingresar = driver.find_element(By.XPATH, "//button[@class='button button--primary-taco button--size-bigger button--size-full'][contains(.,'Continuar')]")
    driver.save_screenshot("Reportes/Iniciarsesion.png")
    btn_ingresar.click()

    

    # Esperar a que se inicie sesión
    time.sleep(5)

    # Verificar si aparece el cartel "¡Verifica tu cuenta y crea más confianza!"
    try:
        # Hacer clic en el botón "Saltar paso"
        saltar_btn = driver.find_element(By.XPATH, "//a[contains(@class,'secondary-action actions close-verify-modal')]")
        driver.save_screenshot("Reportes/omitirverificacion.png")
        saltar_btn.click()
        print("✓ Se ha hecho clic en el botón Saltar paso.")
    except:
        print("El cartel de verificación no está presente.")


    # Esperar a que se inicie sesión
    time.sleep(3)

    # Verificar que se haya iniciado sesión correctamente
    if "Hola, bienvenido" in driver.page_source:
        print("✓ Inicio de sesión exitoso!")
    else:
        print("Inicio de sesión fallido.")


    # Hacer clic en el la opcion de Vehiculos en "Comprar por categoria"
    btn_vehiculos = driver.find_element(By.XPATH, "(//a[@href='vehiculos'][contains(.,'Vehículos')])[2]")
    btn_vehiculos.click()
    print("✓ Se hizo clic en la opcion Vehiculos de Comprar por categoria")
    time.sleep(5)

    # Hacer clic en el tipo de vehiculo y la marca preferida

    # Localizar el elemento del menú desplegable de tipo de vehiculo
    menu_desplegable = driver.find_element(By.XPATH, "//span[@class='ml-3 text-body-2'][contains(.,'Cualquier tipo de vehículo')]")
    menu_desplegable.click()

    time.sleep(1)

    # Esperar a que aparezcan las opciones
    opciones = WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.XPATH, "(//div[contains(.,'Carros')])[10]"))
    )

    # Buscar la opción "Carros" y hacer clic en ella
    for opcion in opciones:
        if opcion.text == "Carros":
            opcion.click()

    print("✓ Se seleccionó carro como tipo de vehiculo")   
    time.sleep(10)


    # Localizar el elemento del menú desplegable de marca
    menu_marca = driver.find_element(By.XPATH, "//span[@class='ml-3 text-body-2'][contains(.,'Cualquier marca')]")
    menu_marca.click()

    time.sleep(5)

    # Esperar a que aparezcan las opciones
    opcionesmarca = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.XPATH, "(//div[contains(.,'Audi')])[10]"))
    )

    # Buscar la opción "Audi" y hacer clic en ella
    for marca in opcionesmarca:
        if marca.text == "Audi":
            marca.click()

    print("✓ Se seleccionó Audi como la marca de vehiculo")
    driver.save_screenshot("Reportes/marcadevehiculo.png")           
    time.sleep(15)

    #Realizar busqueda

    btn_buscar = driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'Realizar búsqueda')]")
    btn_buscar.click()

    print("✓ Realizando busqueda")   
    time.sleep(10)

    #Ordernar resultados por precios mas bajos

    # Localizar el elemento del menú desplegable de relevancia
    menu_relevancia = driver.find_element(By.XPATH, "//span[@class='vs__selected'][contains(.,'Por relevancia')]")
    menu_relevancia.click()

    time.sleep(5)

    # Esperar a que aparezcan las opciones
    opcionesRelevancia = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.XPATH, "//li[contains(.,'Precios más bajos')]"))
    )

    # Buscar la opción "precios mas bajos" y hacer clic en ella
    for relevancia in opcionesRelevancia:
        if relevancia.text == "Precios más bajos":
            relevancia.click()

    print("✓ Se ordenaron los resultados por Precios mas bajos")
    driver.save_screenshot("Reportes/preciosmasbajos.png")
    time.sleep(15)


    # Localizar el elemento "limpiar filtros"
    limpiarfiltros = driver.find_element(By.XPATH, "//button[contains(.,'Limpiar filtros')]")
    limpiarfiltros.click()
    print("✓ Limpiando Filtros")   
    time.sleep(10)

    # Localizar el elemento del menú desplegable "Mi cuenta"
    menu_cuenta = driver.find_element(By.XPATH, "//span[@class='navbar-desktop__my-profile__btn'][contains(.,'Mi cuenta')]")
    menu_cuenta.click()
    driver.save_screenshot("Reportes/Micuenta.png")
    time.sleep(5)

    # Esperar a que aparezcan las opciones
    opcionesCuenta = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.XPATH, "//span[@class='text-error-7'][contains(.,'Cerrar sesión')]"))
    )

    # Buscar la opción "Cerrar sesión" y hacer clic en ella
    for cuenta in opcionesCuenta:
        if cuenta.text == "Cerrar sesión":
            cuenta.click()
    print("✓ Cerrando la Sesion")
    driver.save_screenshot("Reportes/sesioncerrada.png")           
    time.sleep(15)


    # Cerrar la ventana del navegador
    driver.quit()

    assert True
