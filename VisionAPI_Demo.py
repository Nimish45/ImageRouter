
import os

# Print the current working directory
#print("Current working directory:", os.getcwd())

# Print the list of files in the current directory
#print("Files in the current directory:", os.listdir())

import os, io
from google.cloud import vision_v1
from google.cloud.vision_v1 import types
import pandas as pd
import webbrowser

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.json'

client = vision_v1.ImageAnnotatorClient()

def detectText(img):


    with io.open(img, 'rb') as image_file:
        content = image_file.read()

    image = vision_v1.types.Image(content=content)

    response = client.text_detection(image=image)

    df = pd.DataFrame(columns = ['locale','description'])
    texts = response.text_annotations
    for text in texts:
        df = df._append(
            dict(locale = text.locale,
                description=text.description),
            ignore_index=True
        )
    filename='customer.xlsx'
    if 'ED5FVGXWS00' in df['description'].values:
        webbrowser.open('https://www.everydropwater.com/water-filter.refrigerator-water-and-ice-filter-3.edr3rxd1.html')

    df.to_excel(filename, index=False)
    return df

FILE_NAME = 'filter3.jpg'
FOLDER_PATH = r'C:\Users\nimis\OneDrive\Documents\Python Scripts'

print(detectText(os.path.join(FOLDER_PATH, FILE_NAME)))

#print(response)
#print(client)

