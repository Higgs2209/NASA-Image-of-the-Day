import apod_object_parser
import requests

api_key = "9h9Ua0s1QCTEbGx61gshIzuhy12BItEesg9pLywk"

# Set up API Key
response = apod_object_parser.get_data(api_key)

def get_description():
    # Get explanation text
    explanation_text = apod_object_parser.get_explaination(response)
    return explanation_text

# Get file extension
file_extension = apod_object_parser.get_media_type(response)



# Get image URL
image_url = apod_object_parser.get_hdurl(response)
image_response = requests.get(image_url)


def get_image():
    with open("image.jpg", "wb") as file:
        image = file.write(image_response.content)
        return image


print(image_url)



print(file_extension)

