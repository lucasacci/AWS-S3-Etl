import boto3
import os
from dotenv import load_dotenv

load_dotenv()

# Credenciales s3
s3_key = os.getenv('S3_KEY')
s3_secret = os.getenv('S3_SECRET')

def download_csv(bucket_name, s3_key, local_file_path, aws_access_key_id, aws_secret_access_key):
    # Crear un cliente de S3 con credenciales
    s3_client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    try:
        # Descargar el archivo desde S3
        s3_client.download_file(bucket_name, s3_key, local_file_path)
        print(f"Archivo descargado con éxito en: {local_file_path}")
    except Exception as e:
        print(f"Error al descargar el archivo: {e}")

# Información del bucket y archivos
bucket_name = 'desafio-rkd'
file_1_s3_key = 'disney_plus_titles.csv'
file_2_s3_key = 'netflix_titles.csv'

# Ruta local donde se guardarán los archivos
local_file_1 = os.path.join(os.getcwd(), 'files', 'disney_plus_titles.csv')
local_file_2 = os.path.join(os.getcwd(), 'files','netflix_titles.csv')

# Descargar los archivos
download_csv(bucket_name, file_1_s3_key, local_file_1, s3_key, s3_secret)
download_csv(bucket_name, file_2_s3_key, local_file_2, s3_key, s3_secret)
