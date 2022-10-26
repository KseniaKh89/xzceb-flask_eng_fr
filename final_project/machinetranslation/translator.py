import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('8iUhH-2loQmF1B0FYTFBe70MPNOD5oDnQcBZ0dKoYBgK')
language_translator = LanguageTranslatorV3(
    version = '2018-05-01',
    authenticator = authenticator
)
language_translator.set_service_url(
    'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/6a757b57-8414-4682-b0e3-650efb82696b')

def english_to_french(english_text):
    frenchtranslation = language_translator.translate(
        text = english_text, model_id = 'en-fr').get_result()
    french_text = frenchtranslation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    englishtranslation = language_translator.translate(
        text = french_text, model_id = 'fr-en').get_result()
    english_text = englishtranslation['translations'][0]['translation']
    return english_text
