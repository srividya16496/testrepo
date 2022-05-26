pip3 install --upgrade "ibm-watson>=4.2.1"
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Set some variables
api_key = 'nG0iX-KPotlqCO9vVJyoGJ4JINKCf7UejygK19IVxaQ7'
api_url = 'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/ab732265-4699-4c56-9ee5-c7e37c110fd3'
model_id = 'en-it'
text_to_translate = 'Your content you want translate here'

# Prepare the Authenticator
authenticator = IAMAuthenticator(api_key)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(api_url )

# Translate
translation = language_translator.translate(
    text=text_to_translate,
    model_id=model_id).get_result()

# Print results
print(json.dumps(translation, indent=2, ensure_ascii=False))
