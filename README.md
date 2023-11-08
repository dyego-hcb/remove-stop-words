# Stop Words Removal Script

This Python script swiftly removes Portuguese stop words from textual data, aiding in data cleaning for text analysis and Natural Language Processing (NLP) applications.

### Folder Structure

- The **[Remove Stop-Words Source Code](./remove-stopwords-sorce-code/)** folder contains the inputs and outputs used in the created project, as well as the source code itself.
- In the **[Script](./remove-stopwords-sorce-code/script/)** folder, you will find the source code for the project.

## Features

- Removes stop words from the text within a file using NLTK's Portuguese stop words list.
- Efficient file reading and writing to handle large text files.

## Quick Start

1. Clone the repository.
2. Install NLTK: `pip install nltk`.
3. Download the stop words list: `python -c "import nltk; nltk.download('stopwords')"`
4. Run the script: `python remove_stop_words.py input.txt output.txt`.

## Script

The `remove_stop_words.py` script is the core component. It processes `input.txt` to strip out stop words and saves the cleaned text to `output.txt`.

## License

This code is released under the MIT License. See the `LICENSE` file for details.

## Author

- [Your Name](https://github.com/your-username)
