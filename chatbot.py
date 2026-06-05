from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

questions = [
    "hello",
    "how are you",
    "what is your name",
    "what courses are available",
    "how can i contact support"
]

answers = [
    "Hi! How can I help you?",
    "I am doing well.",
    "I am an AI chatbot.",
    "Python, Java and Data Science courses are available.",
    "Contact support at support@gmail.com"
]

def get_response(user_input):

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(
        questions + [user_input]
    )

    similarity = cosine_similarity(
        vectors[-1],
        vectors[:-1]
    )

    index = similarity.argmax()

    return answers[index]