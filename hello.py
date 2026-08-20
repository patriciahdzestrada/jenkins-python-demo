import os

token = os.getenv("DEMO_TOKEN")

print("¿Token disponible?:", token is not None)

def mensaje():
    return "Hola desde Jenkins - Pipeline automatizado"


print(mensaje())
print("Pipeline ejecutado automáticamente")