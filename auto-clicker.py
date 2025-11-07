import pyautogui
import time
import keyboard
import threading

class AutoClicker:
    def __init__(self):
        self.clicking = False
        self.click_thread = None
        self.click_interval = 0.5  # Intervalo más seguro para empezar
        self.total_clicks = 0
        
    def start_clicking(self):
        if self.clicking:
            return
            
        self.clicking = True
        self.total_clicks = 0
        print("🟢 Auto clicker INICIADO")
        print(f"📊 Intervalo: {self.click_interval}s")
        print("⏹️  Presiona 'Q' para detener")
        
        def click_loop():
            while self.clicking:
                pyautogui.click()
                self.total_clicks += 1
                time.sleep(self.click_interval)
        
        self.click_thread = threading.Thread(target=click_loop)
        self.click_thread.daemon = True
        self.click_thread.start()
    
    def stop_clicking(self):
        if not self.clicking:
            return
            
        self.clicking = False
        print("🔴 Auto clicker DETENIDO")
        print(f"📈 Clicks realizados: {self.total_clicks}")
    
    def set_interval(self):
        try:
            nuevo_intervalo = float(input("🕒 Nuevo intervalo (segundos): "))
            if nuevo_intervalo > 0:
                self.click_interval = nuevo_intervalo
                print(f"✅ Intervalo establecido: {nuevo_intervalo}s")
            else:
                print("❌ El intervalo debe ser mayor a 0")
        except ValueError:
            print("❌ Ingresa un número válido")

# Configuración inicial
pyautogui.FAILSAFE = True  # Mover mouse a esquina superior izquierda para emergencia
clicker = AutoClicker()

print("🎮 AUTO CLICKER - CONTROLES:")
print("=================================")
print("🟢 S - Iniciar auto clicker")
print("🔴 Q - Detener auto clicker")  
print("⚙️  I - Cambiar intervalo")
print("❌ ESC - Salir del programa")
print("=================================")
print("💡 Mueve el mouse a la esquina superior")
print("   izquierda para PARADA DE EMERGENCIA")
print("=================================")

try:
    while True:
        if keyboard.is_pressed('s') and not clicker.clicking:
            clicker.start_clicking()
            time.sleep(0.3)  # Prevenir múltiples activaciones
        
        elif keyboard.is_pressed('q') and clicker.clicking:
            clicker.stop_clicking()
            time.sleep(0.3)
        
        elif keyboard.is_pressed('i'):
            clicker.set_interval()
            time.sleep(0.3)
        
        elif keyboard.is_pressed('esc'):
            clicker.stop_clicking()
            print("👋 Saliendo del programa...")
            break
        
        time.sleep(0.01)
        
except KeyboardInterrupt:
    clicker.stop_clicking()
    print("👋 Programa interrumpido por el usuario")