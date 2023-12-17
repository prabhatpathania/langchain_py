from langchain.document_loaders import AssemblyAIAudioTranscriptLoader
from langchain.document_loaders.assemblyai import TranscriptFormat


audio_file = "https://storage.googleapis.com/aai-docs-samples/nbc.mp3"
# or a local file path: audio_file = "./nbc.mp3"

loader = AssemblyAIAudioTranscriptLoader(file_path=audio_file,transcript_format=TranscriptFormat.SENTENCES)

docs = loader.load()

news_content=docs[0].page_content
content_info= docs[0].metadata

print(news_content)