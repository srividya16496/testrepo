pip3 install --upgrade "ibm-watson>=4.2.1"
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Set some variables
api_key = '[API KEY]'
api_url = '[API URL]'
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

## English to French
def english_to_french(text1):
    frenchtranslation = language_translate.translate(
        text = text1,
        model_id = 'en-fr'
    ).get_result()
return frenchtranslation.get("translations")[0].get("translation")


##  French to English
def french_to_english(text1):
    frenchtranslation = language_translate.translate(
        text = text1,
        model_id = 'fr-en'
    ).get_result()
return frenchtranslation.get("translations")[0].get("translation")



# Print results
print(json.dumps(translation, indent=2, ensure_ascii=False))
