# TextPairer

**TextPairer** is a utility designed to pair corresponding paragraphs and sentences from two text files. It ensures that the paired content is aligned correctly, making it suitable for scenarios such as bilingual text alignment, subtitle synchronization, or other comparative text analysis tasks.

## Features
- Reads two text files and aligns their content.
- Supports pairing paragraphs and sentences with validation.
- Provides detailed error messages when alignment issues are detected.
- Saves the paired output to a new file for easy reference.

## Prerequisites
- Python 3.7 or higher

## Installation
Clone the repository and navigate to the project directory:
```bash
$ git clone <repository_url>
$ cd TextPairer
```

## Usage
Prepare two text files for pairing, ensuring the content in each file corresponds logically:
- `file1.txt` (e.g., a source language or reference text)
- `file2.txt` (e.g., a target language or comparative text)

### Example
```python
from text_pairer import pair_texts

file1 = 'file1.txt'
file2 = 'file2.txt'

try:
    paired_output = pair_texts(file1, file2)
    print(paired_output)

    # Save to file
    with open('paired_output.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(paired_output)
except ValueError as e:
    print(f"Error: {e}")
```

### Command-line Example
```bash
$ python text_pairer.py file1.txt file2.txt
```
This will process the two input files and generate `paired_output.txt` in the current directory.

## Functionality
### `pair_texts(file1, file2)`
- **Input:** Two text files containing paragraphs separated by double newlines (`\n\n`) and sentences separated by single newlines (`\n`).
- **Output:** A string where each paragraph and its corresponding sentences are paired.

### Error Handling
- Ensures the number of paragraphs in both files match.
- Validates the number of sentences within each paired paragraph.
- Provides detailed error messages if mismatches occur.

## Output Format
The output file will contain aligned text in the following format:
```
Sentence from file1
Sentence from file2

[Blank line separating paragraphs]
```

## Contributing
Contributions are welcome! Please fork the repository, make changes, and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

For additional questions or issues, feel free to open an issue in the repository.

