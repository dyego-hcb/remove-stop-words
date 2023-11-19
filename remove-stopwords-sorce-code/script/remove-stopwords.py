import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words_pt = set(stopwords.words('portuguese'))

def remove_stop_words(text):
    words = text.split()
    filtered_text = ' '.join(word for word in words if word.lower() not in stop_words_pt)
    return filtered_text

def remove_stopwords_in_file(input_path, output_path):
    try:
        with open(input_path, 'r', encoding='utf-8') as input_file, open(output_path, 'w', encoding='utf-8') as output_file:
            for linha in input_file:
                texto_sem_stop_words = remove_stop_words(linha)
                if texto_sem_stop_words.strip():
                    output_file.write(texto_sem_stop_words + '\n')

        print(f"Stop words removidas e texto salvo em {output_path}")

    except FileNotFoundError:
        print(f"Arquivo {input_path} não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

input_path = './input/in.txt'
output_path = './output/out.txt'

remove_stopwords_in_file(input_path, output_path)
