# Script de Remoção de Stop Words

Este script em Python remove rapidamente stop words em português de dados textuais, auxiliando na limpeza de dados para análise de texto e aplicações de Processamento de Linguagem Natural (PLN).

### Estrutura do Diretório

- A pasta **[Código Fonte de Remoção de Stop Words](./remove-stopwords-sorce-code/)** contém os inputs e outputs utilizados no projeto, assim como o próprio código-fonte.
- Na pasta **[Script](./remove-stopwords-sorce-code/script/)**, você encontrará o código-fonte do projeto.

## Recursos

- Remove stop words do texto dentro de um arquivo usando a lista de stop words em português do NLTK.
- Leitura e escrita eficientes de arquivos para lidar com grandes volumes de texto.

## Início Rápido

1. Clone o repositório.
2. Instale o NLTK: `pip install nltk`.
3. Baixe a lista de stop words: `python -c "import nltk; nltk.download('stopwords')"`
4. Execute o script: `python remove_stop_words.py input.txt output.txt`.

## Script

O script `remove_stop_words.py` é o componente central. Ele processa `input.txt` para remover as stop words e salva o texto limpo em `output.txt`.

***

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