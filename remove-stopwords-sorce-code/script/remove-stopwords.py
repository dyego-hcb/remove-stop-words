import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words_pt = set(stopwords.words('portuguese'))

def remove_stop_words(text):
    words = text.split()
    filtered_text = ' '.join(word for word in words if word.lower() not in stop_words_pt)
    return filtered_text

def process_file(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as f_in, open(output_file_path, 'w', encoding='utf-8') as f_out:
        for line in f_in:
            f_out.write(remove_stop_words(line) + '\n')

input_file_path = './input/in.txt'
output_file_path = './output/out.txt.txt'
process_file(input_file_path, output_file_path)
