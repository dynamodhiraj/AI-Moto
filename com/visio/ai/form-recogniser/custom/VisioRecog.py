import os
from azure.ai.formrecognizer import FormRecognizerClient
from azure.ai.formrecognizer import FormTrainingClient
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import ResourceNotFoundError

# Run pip3 install azure-ai-formrecognizer
#Azure key and Endpoint
endpoint="https://visiorecog.cognitiveservices.azure.com/"
key ="186908db5d6d42d798b1594fa7e224d8"  


#Recognizing form fields and content using custom models trained to analyze your custom forms.
form_recognizer_client = FormRecognizerClient(endpoint, AzureKeyCredential(key))
#Training custom models to analyze all fields .
form_training_client = FormTrainingClient(endpoint, AzureKeyCredential(key))


formUrl = "https://raw.githubusercontent.com/Azure/azure-sdk-for-python/master/sdk/formrecognizer/azure-ai-formrecognizer/tests/sample_forms/forms/Form_1.jpg"

#Analyse Content of a file at a given url
poller = form_recognizer_client.begin_recognize_content_from_url(formUrl)

# Analyse Content of a file from a local disk
#poller = form_recognizer_client.begin_recognize_content()

page = poller.result()

table = page[0].tables[0] # page 1, table 1

print("Table found on page {}:".format(table.page_number))

for cell in table.cells:
    print("Cell text: {}".format(cell.text))
    print("Location: {}".format(cell.bounding_box))
    print("Confidence score: {}\n".format(cell.confidence))

