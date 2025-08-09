# import gradio as gr
from src.ingestion.audio_transcriber import transcribe_audio
from src.ingestion.pdf_parser import extract_pdf
from src.ingestion.youtube_downloader import download_audio
from src.qa.embed_store import chunk_text, embed_text
from src.generator.summarizer import get_summary
from src.generator.study_guide_builder import get_answers, followup_quiz
from src.generator.flash_card_maker import get_flashcards
import asyncio


info_dict = {
    "youtube_link": "https://www.youtube.com/watch?v=joewRl1CTL8",
    "lecture_notes": "../data/Continuous-Functions.pdf",
    "qa": "../data/qa.txt"
}


def get_qa(path):
    with open(path, 'r') as file:
        content = file.read()
        return content


async def generate():
    download_audio(info_dict["youtube_link"])
    audio_text = transcribe_audio("./audio.m4a")
    pdf_text = extract_pdf(info_dict["lecture_notes"])

    text = "\n".join((audio_text, pdf_text))
    chunks = chunk_text(text)
    index = embed_text(chunks)

    qa = get_qa(info_dict["qa"])

    summary = await get_summary(text)
    answers = await get_answers(qa, index, chunks)
    flash_cards = await get_flashcards(qa, text)
    quiz = await followup_quiz(qa, text)

    text = "\n\n ## Summary \n\n" + summary + "\n\n ## Q&A \n\n" + answers + "\n\n ## Flash Cards \n\n" + flash_cards + "\n\n ## Quiz \n\n" + quiz
    print(text)


if __name__ == "__main__":
    asyncio.run(generate())
