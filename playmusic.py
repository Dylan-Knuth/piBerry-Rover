from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_mp3("car_start.mp3")

play(song)
