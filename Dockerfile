# Imagen base de Python
FROM python:3.9

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos necesarios
COPY principal.py requirements.txt ./

# Instalar dependencias
RUN pip install -r requirements.txt

# Exponer puerto para Cloud Run
EXPOSE 8080

# Comando de inicio
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "principal:app"]
