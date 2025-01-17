# Pair Text Files with DeepL API Translation

This script pairs sentences from a text file (`file1.txt`) with their translated versions using the DeepL API. The translation process uses an external API key stored in a configuration file for enhanced security.

## Features
- Splits text into sentences while preserving dots inside quotes and at the end of sentences.
- Uses the DeepL API to translate sentences from the source language to the target language.
- Pairs original and translated sentences for easy review and saving.

## Requirements
- Python 3.8 or higher
- DeepL Python SDK

## Installation
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install the required dependencies:
   ```bash
   pip install deepl
   ```

## Configuration
1. Create a `config.json` file in the project root directory with the following content:
   ```json
   {
       "deepl_api_key": "your_deepl_api_key_here"
   }
   ```
   Replace `your_deepl_api_key_here` with your actual DeepL API key.

2. Add `config.json` to your `.gitignore` file to prevent it from being tracked by Git:
   ```
   config.json
   ```

## Usage
1. Place the source text file (`file1.txt`) in the project directory.
2. Run the script:
   ```bash
   python <script-name>.py
   ```
3. Review the extracted sentences and their translations.
4. The paired output will be saved to `paired_output.txt`.

## Example
### Input: `file1.txt`
```
1. Nietzsche and Dostoevsky had deep insights into human nature.
"Art is the lie that enables us to realize the truth," said Picasso.
```

### Output: `paired_output.txt`
```
1. Nietzsche and Dostoevsky had deep insights into human nature.
니체와 도스토옙스키는 인간 본성에 대한 깊은 통찰을 가지고 있었습니다.

"Art is the lie that enables us to realize the truth," said Picasso.
"예술은 진실을 깨닫게 해주는 거짓말입니다,"라고 피카소는 말했습니다.

```

## Error Handling
- If the API key is missing or invalid, a `ValueError` is raised.
- Sentences that fail to translate will display `[Translation Error]`.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

