import os

token = os.getenv("DEMO_TOKEN")
env = os.getenv("APP_ENV")

print("¿Token disponible?:", token is not None)
print("Ambiente:", env)

def mensaje():
    return "Hola desde Jenkins - Pipeline automatizado"


print(mensaje())
print("Pipeline ejecutado automáticamente")