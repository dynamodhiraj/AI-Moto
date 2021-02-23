import os
from azure.ai.formrecognizer import FormRecognizerClient
from azure.ai.formrecognizer import FormTrainingClient
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import ResourceNotFoundError

# Run pip3 install azure-ai-formrecognizer
#Azure key and Endpoint
endpoint="https://visiorecog.cognitiveservices.azure.com/"
key ="186908db5d6d42d798b1594fa7e224d8"  

# To train a model you need an Azure Storage account.
# Use the SAS URL to access your training files.
form_training_client = FormTrainingClient(endpoint, AzureKeyCredential(key))
trainingDataUrl = "https://azuremarketvisio.blob.core.windows.net/formrecogblobs?sp=racwl&st=2021-02-19T21:02:18Z&se=2021-02-20T21:02:18Z&sv=2020-02-10&sr=c&sig=ZypQ1QolILXiSYKat9grHEpVoUHAe6sJW9UOLpwyG4U%3D"

poller = form_training_client.begin_training(trainingDataUrl, use_training_labels=False)
model = poller.result()

print("Model ID: {}".format(model.model_id))
print("Status: {}".format(model.status))
print("Training started on: {}".format(model.training_started_on))
print("Training completed on: {}".format(model.training_completed_on))

print("\nRecognized fields:")
for submodel in model.submodels:
    print(
        "The submodel with form type '{}' has recognized the following fields: {}".format(
            submodel.form_type,
            ", ".join(
                [
                    field.label if field.label else name
                    for name, field in submodel.fields.items()
                ]
            ),
        )
    )

# Training result information
for doc in model.training_documents:
    print("Document name: {}".format(doc.name))
    print("Document status: {}".format(doc.status))
    print("Document page count: {}".format(doc.page_count))
    print("Document errors: {}".format(doc.errors))