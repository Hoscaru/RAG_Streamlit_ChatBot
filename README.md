Crea el entorno virtual:python -m venv "Nombre del entorno"
Activa el entorno virtual
Instala las dependencias del requirements.txt: pip install -r requirements.txt
crea tu archivo .env y dentro de el agregas tu Api Key. Ejm:
GROQ_API_KEY="Tu Api key"
Yo utilice groq como proveedor esta vez, pero se puede usar cohere tambien o cualquier otra, solo que debes cambiar
las importaciones e instalar las dependencias de langchain-cohere, etc
