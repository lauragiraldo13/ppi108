from ayudas import *

VIDA = './archivos/vida.txt'

def leer_vida():
    if not os.path.exists(VIDA):
        return 100 # Valor inicial si no existe el archivo
    
    with open (VIDA, "r") as f:
        contenido = f.read().strip()
        return int(contenido) if contenido else 100
    
def guardar_vida(nueva_vida):
    with open (VIDA, "w") as f:
        f.write(str(nueva_vida))

def recibir_danio(cantidad):
    vida_actual = leer_vida()
    vida_restante = max(0, vida_actual - cantidad)

    print(f"Vida anterior: {vida_actual}")
    print(f"Recibiendo: {cantidad} de daño...")
    print(f"Vida restante: {vida_restante}")

    guardar_vida(vida_restante)
    return vida_restante
