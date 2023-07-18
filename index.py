import pyaudio

import assemblyai as aai

# aai.settings.api_key = "1dbc60da72694918aec13a3a6140dbd2"
aai.settings.api_key = "1dbc60da72694918aec13a3a6140dbd2"

transcriber = aai.Transcriber()

transcript = transcriber.transcribe("./my-local-audio-file.wav")

print(transcript.text)