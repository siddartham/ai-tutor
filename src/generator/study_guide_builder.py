from .utils import get_llm
from ..qa.query_rag import query


def format_qa(chunks, question):
    return f"Question: {question}\n Info: {chunks} \n\n"


async def get_answers(qa, index, chunks):
    questions = qa.splitlines()
    qa_format = ""
    for question in questions:
        qa_format += format_qa(query(chunks, index, question), question)

    answer_prompt = (
        f"You are helping a student answer the questions.\n\n"
        f"You are provided each questions and text relevant to that questions below the"
        f"question.\n\n"
        f"You have to answer from the text provided for each question: \n\n"
        f" {qa_format}\n\n"
        f"Please provide answers to the respective questions"
    )
    llm = get_llm()
    return llm.invoke(answer_prompt).content


async def get_flashcards(qa, text):
    flashcard_prompt = (
        f"You are helping a student learn the concepts thoroughly.\n\n"
        f"You are provided with lecture text and the list of questions a student is interested to learn: \n\n"
        f"Lecture: {text}\n\n"
        f"Questions: {qa}\n\n"
        f"Please provide 10 flashcards that could cover the topics mentioned by the student"
    )
    llm = get_llm()
    return llm.invoke(flashcard_prompt).content

async def followup_quiz(qa, text):
    pass
