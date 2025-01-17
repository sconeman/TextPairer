def pair_text_files(file1, file2):
    # Read the content of both files
    with open(file1, 'r', encoding='utf-8') as file_a:
        content_a = file_a.read()

    with open(file2, 'r', encoding='utf-8') as file_b:
        content_b = file_b.read()

    # Split the content into paragraphs using double newlines
    paragraphs_a = content_a.strip().split('\n\n')
    paragraphs_b = content_b.strip().split('\n\n')

    # Ensure both files have the same number of paragraphs
    if len(paragraphs_a) != len(paragraphs_b):
        raise ValueError(f"The number of paragraphs in the first file ({len(paragraphs_a)}) and the second file ({len(paragraphs_b)}) do not match.\n\nFile 1 paragraphs:\n{paragraphs_a}\n\nFile 2 paragraphs:\n{paragraphs_b}")

    output = []

    # Iterate through each paragraph and pair sentences
    for i, (para_a, para_b) in enumerate(zip(paragraphs_a, paragraphs_b), start=1):
        sentences_a = para_a.strip().split('\n')
        sentences_b = para_b.strip().split('\n')

        # Ensure both paragraphs have the same number of sentences
        if len(sentences_a) != len(sentences_b):
            raise ValueError(f"Paragraph {i}: The number of sentences in the first file ({len(sentences_a)}) and the second file ({len(sentences_b)}) do not match.\n\nFile 1 sentences:\n{sentences_a}\n\nFile 2 sentences:\n{sentences_b}")

        # Pair sentences
        for sentence_a, sentence_b in zip(sentences_a, sentences_b):
            output.append(f"{sentence_a}\n{sentence_b}\n\n")

        # Add a blank line between paragraphs
        output.append("\n")

    return ''.join(output)

# Example usage
file1 = 'file1.txt'
file2 = 'file2.txt'

try:
    output = pair_text_files(file1, file2)
    print(output)

    # Optionally save the output to a file
    with open('paired_output.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(output)
except ValueError as e:
    print(f"Error: {e}")

