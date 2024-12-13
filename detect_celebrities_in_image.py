import boto3

# Crie um cliente do Rekognition
rekognition_client = boto3.client('rekognition')

def detect_celebrities(image_path):
    with open(image_path, 'rb') as image:
        response = rekognition_client.recognize_celebrities(Image={'Bytes': image.read()})
        
    if 'CelebrityFaces' in response:
        for celebrity in response['CelebrityFaces']:
            print(f"Nome: {celebrity['Name']}")
            print(f"Confiança: {celebrity['MatchConfidence']}")
            print(f"URL do perfil: {celebrity['Urls'][0] if celebrity['Urls'] else 'N/A'}")
            print("\n")
    else:
        print("Nenhuma celebridade detectada.")

# Exemplo de uso
detect_celebrities('caminho/para/sua/imagem.jpg')
