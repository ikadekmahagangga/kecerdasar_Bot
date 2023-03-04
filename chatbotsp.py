import random

# membuat kumpulan pertanyaan dan jawaban
questions = {
    "hai": ["Halo!", "Hai!", "Hai, apa kabar?"],
    "apa kabar": ["Baik-baik saja, terima kasih!", "Baik, terima kasih! Kamu sendiri?", "Lumayan, terima kasih!"],
    "siapa nama kamu": ["Nama saya Chatbot!", "Saya disebut Chatbot!"],
    "bye": ["Sampai jumpa!", "Dadah!", "Bye!"]
}

# fungsi untuk merespon input pengguna
def respond(input_text):
    # membuat input pengguna menjadi lowercase
    input_text = input_text.lower()

    # mencari pertanyaan yang cocok
    for question in questions:
        if question in input_text:
            return random.choice(questions[question])

    # jika tidak ada pertanyaan yang cocok, merespon dengan kalimat default
    return "Maaf, saya tidak mengerti apa yang kamu maksud."

# program utama
while True:
    user_input = input("Pesan Anda: ")
    bot_response = respond(user_input)
    print("Chatbot:", bot_response)
