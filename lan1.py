from googletrans import Translator

# Initialize the Translator
translator = Translator()

# Function to translate text
def translate_text(text, src_language='auto', dest_language='en'):
    try:
        translated = translator.translate(text, src=src_language, dest=dest_language)
        return translated.text
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage
text_to_translate = "Hola, ¿cómo estás?"
translated_text = translate_text(text_to_translate, src_language='es', dest_language='en')
print(f"Translated Text: {translated_text}")
 