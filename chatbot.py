from chatterbot import ChatBot
import spacy

spacy.cli.download("en_core_web_sm")
spacy.cli.download("en")

nlp = spacy.load('en_core_web_sm')

chatbot = ChatBot(
    'PersonalBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

# Training With Own Questions 
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(chatbot)

training_data_quesans = open('training_data/ques_ans.txt').read().splitlines()
training_data_about = open('training_data/About.txt').read().splitlines()
training_data_gk = open('training_data/Gk.txt').read().splitlines()
training_data_greetings = open('training_data/Greetings.txt').read().splitlines()
training_data_joke = open('training_data/Joke.txt').read().splitlines()
training_data_movie = open('training_data/Movie.txt').read().splitlines()

training_data = training_data_quesans + training_data_about + training_data_gk + training_data_greetings + training_data_joke + training_data_movie 

trainer.train(training_data)

# Training With Corpus
# from chatterbot.trainers import ChatterBotCorpusTrainer

# trainer_corpus = ChatterBotCorpusTrainer(chatbot)

# trainer_corpus.train(
#     'chatterbot.corpus.english'
# )
