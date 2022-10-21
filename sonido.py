import sounddevice
import asyncio
from amazon_transcribe.client import TranscribeStreamingClient
from amazon_transcribe.handlers import TranscriptResultStreamHandler
from amazon_transcribe.model import TranscriptEvent
guardado=[]
ultimo=["0"]
estado=[False]

class MyEventHandler(TranscriptResultStreamHandler):
    async def handle_transcript_event(self, transcript_event: TranscriptEvent):
        results = transcript_event.transcript.results
        for result in results:
            if result.is_partial==False:
                ultimo[0]=result.alternatives[0].transcript
                guardado.append(result.alternatives[0].transcript)

async def Microfono():
    loop = asyncio.get_event_loop()
    input_queue = asyncio.Queue()
    def callback(indata, frame_count, time_info, status):
        loop.call_soon_threadsafe(input_queue.put_nowait, (bytes(indata), status))
    stream = sounddevice.RawInputStream(
        channels=1,
        samplerate=16000,
        callback=callback,
        blocksize=1024 * 2,
        dtype="int16",
    )
    with stream:
        while True:
            indata, status = await input_queue.get()
            yield indata, status

async def Escribir_fragmento(stream):
    async for chunk, status in Microfono():
        await stream.input_stream.send_audio_event(audio_chunk=chunk)
        if(estado[0]==False):
            break
    await stream.input_stream.end_stream()

async def Recibir_Enviar():
    client = TranscribeStreamingClient(region="us-east-1")
    stream = await client.start_stream_transcription(
        language_code="es-US",
        media_sample_rate_hz=16000,
        media_encoding="pcm"
    )
    handler = MyEventHandler(stream.output_stream)
    await asyncio.gather(Escribir_fragmento(stream), handler.handle_events())
loop=asyncio.get_event_loop()