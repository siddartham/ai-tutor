from .utils import get_llm


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
