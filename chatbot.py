# Mengimpor library yang diperlukan
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from chatterbot.comparisons import JaccardSimilarity
from chatterbot.response_selection import get_most_frequent_response
from chatterbot.conversation import Statement
import nltk

# Membuat instance chatbot
chatbot = ChatBot(
    'Bot', 
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'statement_comparison_function': JaccardSimilarity,
            'response_selection_method': get_most_frequent_response,
            'default_response': 'Maaf, saya tidak mengerti pertanyaan Anda',
            'maximum_similarity_threshold': 0.8
        }
    ]
)

# Mentraining chatbot menggunakan data yang disediakan
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# Menambahkan data training dari file lain
trainer_corpus = ListTrainer(chatbot)
with open("training_data.txt") as file:
    conversation_data = file.readlines()
conversation_data = [line.strip() for line in conversation_data]
trainer_corpus.train(conversation_data)

# Loop untuk meminta input dan menghasilkan output chatbot
while True:
    try:
        user_input = input("You: ")
        response = chatbot.get_response(user_input)
        print("Bot:", response)

    # Jika user memasukkan input yang tidak dapat diproses
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
