import ollama
from ollama import Client

import glob
import pandas as pd
from PIL import Image

import os
from io import BytesIO


client = Client(host='http://host.docker.internal:11434')


# Load the DataFrame from a CSV file, or create a new one if the file doesn't exist
def load_or_create_dataframe(filename):
    if os.path.isfile(filename):
        df = pd.read_csv(filename)
    else:
        df = pd.DataFrame(columns=['image_file', 'description'])
    return df

df = load_or_create_dataframe('image_descriptions.csv')

def get_png_files(folder_path):
    return glob.glob(f"{folder_path}/*.png")

# get the list of image files in the folder yopu want to process
image_files = get_png_files("./images") 
image_files.sort()

print(image_files[:3])
print(df.head())


prompt = """
Consider this image then write a report using Markdown. Your report MUST contain the following sections and use the following format:
* Description: < a one sentence decription of what the picture depicts>
* Visible Objects: < a numbered list of all objects in the photo>
* Notable Details: < a numbered list of any notable features, including, landscape, architecture, weather>
* NSFW Content Detected: <yes or no>
"""
# processing the images 
def process_image(image_file):
    print(f"\nProcessing {image_file}\n")
    with Image.open(image_file) as img:
        with BytesIO() as buffer:
            img.save(buffer, format='PNG')
            image_bytes = buffer.getvalue()

    full_response = ''
    # Generate a description of the image
    for response in client.generate(model='llava',
                             prompt=prompt, 
                             images=[image_bytes], 
                             stream=True):
        # Print the response to the console and add it to the full response
        print(response['response'], end='', flush=True)
        full_response += response['response']

    # Add a new row to the DataFrame
    df.loc[len(df)] = [image_file, full_response]


for image_file in image_files:
    if image_file not in df['image_file'].values:
        process_image(image_file)

# Save the DataFrame to a CSV file
df.to_csv('image_descriptions.csv', index=False)

