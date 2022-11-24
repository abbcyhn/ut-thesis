import os
import time
import json
import requests
from pydub import AudioSegment

INPUT_PATH = "input"
AUDIO_INPUT_PATH = f"{INPUT_PATH}/audio.mp3"
SUBTITLE_INPUT_PATH = f"{INPUT_PATH}/subtitle.txt"

OUTPUT_PATH = "output"
SUBTITLE_OUTPUT_PATH = f"{OUTPUT_PATH}/subtitle.srt"

FOG_API_ENDPOINT = "http://localhost:5000/api/sync"
CLOUD_API_ENDPOINT = "http://localhost:5000/api/sync"

def sendto(audio_path, subtitle_path, api_endpoint):
	files = {
		'audio': open(audio_path, 'rb'),
		'subtitle': open(subtitle_path, 'rb'),
	}
	response = requests.post(url = api_endpoint, files=files)
	return response.content

def readfile(filepath):
	try:
		with open(filepath, "rb") as f:
			b = f.read(1)
			mybytearray = bytearray()
			while b:
				mybytearray += b
				b = f.read(1)
	except IOError:
		raise Exception('Error While Opening the file!')  

def readlines(filepath):
	with open(filepath, 'r') as f:
		lines = f.readlines()
	return lines



def change_format(sec, offset):
	sec = sec.split('.')
	s = int(sec[0]) + offset
	ms = sec[1]
	st = f"{time.strftime('%H:%M:%S', time.gmtime(s))},{ms}"
	return st


def get_as_list(jsonfile):
	jsonfile = jsonfile.decode('utf8').replace("'", '"')
	print(f"JSON TYPE IS {type(jsonfile)}")
	print(f"JSON IS {jsonfile}")
	myjson = json.load(jsonfile)
	return myjson['fragments']

def convert_to_subtitles(jsonfile, offset):
	subtitles = []
	l = get_as_list(jsonfile)

	index = 1
	for i in l:
		begin = change_format(i['begin'], offset)
		end = change_format(i['end'], offset)
		lines = i['lines']

		subtitle = f"{index}\n"
		subtitle += f"{begin} --> {end}"
		for line in lines:
			subtitle += f"\n{line}"
		subtitle += "\n\n"
		subtitles.append(subtitle)
		index += 1

	return subtitles

def append_subtitles(subtitles, filepath):
	for subtitle in subtitles:
		with open(filepath, 'a') as f:
			f.write(subtitle)

def main():
	audio = AudioSegment.from_mp3(AUDIO_INPUT_PATH)
	audio_slices = audio[::10000]
	subtitle_slices = readlines(SUBTITLE_INPUT_PATH)

	subtitle_index = -1
	for index, chunk in enumerate(audio_slices):
		response = "EMPTY RESPONSE"

		# read audio slice
		audio_slice_path = f"{INPUT_PATH}/audio_{index}.mp3"	
		with open(audio_slice_path, "wb") as f:
			chunk.export(f, format="mp3")

		# read subtitle slice
		subtitle_slice_path = f"{INPUT_PATH}/subtitle_{index}.txt"
		with open(subtitle_slice_path, "w") as f:
			subtitle_index += 1
			f.write(subtitle_slices[subtitle_index])
			subtitle_index += 1
			f.write(subtitle_slices[subtitle_index])

		# send to fog
		if (index % 2 == 0):
			print("SENDING TO FOG")
			response = sendto(audio_slice_path, subtitle_slice_path, FOG_API_ENDPOINT)
			print("RETRIEVING FROM FOG")
		# send to cloud
		else:
			print("SENDING TO CLOUD")
			response = sendto(audio_slice_path, subtitle_slice_path, CLOUD_API_ENDPOINT)
			print("RETRIEVING FROM CLOUD")

		print(response)

		offset = index * 10
		subtitles = convert_to_subtitles(response, offset)
		append_subtitles(subtitles, SUBTITLE_OUTPUT_PATH)

		# remove slices
		#os.remove(audio_slice_path)
		#os.remove(subtitle_slice_path)


if __name__ == '__main__':
	main()