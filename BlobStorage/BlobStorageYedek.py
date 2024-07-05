from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os

# Azure storage baglanti ayalari

connection_string = "DefaultEndpointsProtocol=https;AccountName=rgacademy1str;AccountKey=s2KWwRXJh6zX3fdzwRE7TpJc1/0cWmapMCquelvVzOxPhAVUs86N4Tqpo4Kb6u7SNaaOnYcGHZy3+AStbKlYRw==;EndPointSuffix=core.windows.net"
container_name = "azureml"
blob_name = "yatirimDeneme"
#file_path = "DummyData/yatirim_2706.pdf"

script_directory= os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(script_directory, "DataFiles")


blob_service_client = BlobServiceClient.from_connection_string(connection_string)

container_client = blob_service_client.get_container_client(container_name)

for file_name in os.listdir(data_file):
    local_file_path = os.path.join(data_file,file_name)
    blob_name = file_name

    blob_client = container_client.get_blob_client(file_name)


    with open(local_file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)

    print(f"{blob_name} isimli blob basariyla yuklendi")
print("Butun Dosyalar Basariyla Yuklendi")