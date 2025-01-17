import re
import json
import deepl

def load_api_key(config_file):
    """Load the API key from a configuration file."""
    try:
        with open(config_file, 'r', encoding='utf-8') as file:
            config = json.load(file)
        return config["deepl_api_key"]
    except (FileNotFoundError, KeyError):
        raise ValueError("API key not found in the configuration file.")

def pair_text_files_with_deepl(file1, config_file):
    # Load API key from the configuration file
    api_key = load_api_key(config_file)

    # Initialize DeepL Translator
    translator = deepl.Translator(api_key)

    # Read the content of the file
    with open(file1, 'r', encoding='utf-8') as file_a:
        content_a = file_a.read()

    # Split the content into sentences while preserving dots inside quotes and at the end of sentences
    sentences_a = [sentence.strip() + '.' for sentence in re.split(r'(?<!\")\.(?!\")(?=\s|$)|(?<=\n)', content_a.strip().replace('\".', '".')) if sentence.strip()]

    # Output sentences_a for user verification
    print("Sentences from file1 (sentences_a):")
    for sentence in sentences_a:
        print(sentence)

    # Translate sentences_a using DeepL API
    sentences_b = []
    for sentence in sentences_a:
        try:
            result = translator.translate_text(sentence, target_lang="KO")  # Change "KO" to the desired target language
            sentences_b.append(result.text.strip())
        except deepl.DeepLException as e:
            print(f"Translation error for sentence: {sentence}")
            sentences_b.append("[Translation Error]")

    # Ensure the number of sentences matches
    if len(sentences_a) != len(sentences_b):
        raise ValueError("The number of translated sentences does not match the original sentences.")

    # Create output by pairing sentences_a and sentences_b
    output = []
    for sentence_a, sentence_b in zip(sentences_a, sentences_b):
        output.append(f"{sentence_a}\n{sentence_b}\n\n")

    # Print the paired output
    print("\nPaired output:")
    print(''.join(output))

    return ''.join(output)

# Example usage
file1 = 'file1.txt'
config_file = 'config.json'

try:
    output = pair_text_files_with_deepl(file1, config_file)

    # Optionally save the output to a file
    with open('paired_output.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(output)
except ValueError as e:
    print(f"Error: {e}")

