import os
import time
import json
import requests
from pydub import AudioSegment



###################################################################### CONSTANTS
INPUT_PATH = "input"
AUDIO_INPUT_PATH = f"{INPUT_PATH}/pulp_fiction_audio.mp3"
SUBTITLE_INPUT_PATH = f"{INPUT_PATH}/pulp_fiction_subtitle_input.txt"

OUTPUT_PATH = "output"
SUBTITLE_OUTPUT_PATH = f"{OUTPUT_PATH}/pulp_fiction_subtitle_output.srt"

FOG_API_ENDPOINT = "http://localhost:81/api/sync"
CLOUD_API_ENDPOINT = "http://172.17.90.194:81/api/sync"


###################################################################### AUDIO SLICING
def get_audio_slices():
	audio = AudioSegment.from_mp3(AUDIO_INPUT_PATH)
	audio_slices = audio[::10000]
	return audio_slices

def get_count_of_audio_slices():
	audio_slices = get_audio_slices()
	length = len(list(audio_slices))
	length = length - 3 # remove music for pulp fiction
	return length

def split_audios():
	audio_slices = get_audio_slices()

	slice_counter = 0
	for index, chunk in enumerate(audio_slices):
		# remove music for pulp fiction
		if index == 0 or index == 1 or index == 2:
			continue

		# write audio slice
		audio_slice_path = f"{INPUT_PATH}/pulp_fiction_audio_{slice_counter}.mp3"	
		with open(audio_slice_path, "wb") as f:
			chunk.export(f, format="mp3")
		
		slice_counter += 1
	
	# return slice_counter


###################################################################### SUBTITLE SLICING
def readsubtitles(filepath):
	with open(filepath, 'r') as f:
		lines = f.readlines()
	return lines

def split_subtitles(slice_counter):
	subtitle_slices = split_subtitles_helper(readsubtitles(SUBTITLE_INPUT_PATH), slice_counter)

	for index in range(slice_counter):
		# write subtitle slice
		subtitle_slice_path = f"{INPUT_PATH}/pulp_fiction_subtitle_{index}.txt"
		with open(subtitle_slice_path, "w") as f:
			for subtitle in list(subtitle_slices[index]):
				f.write(subtitle)

def split_subtitles_helper(a, n):
    k, m = divmod(len(a), n)
    return [a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n)]


###################################################################### SYNC PART
def sendto(audio_path, subtitle_path, api_endpoint):
	files = {
		'audio': open(audio_path, 'rb'),
		'subtitle': open(subtitle_path, 'rb'),
	}
	response = requests.post(url = api_endpoint, files=files)
	return response.content


###################################################################### OUTPUT MERGING
def get_as_list(jsonfile):
	jsonfile = jsonfile.decode('utf8')
	myjson = json.loads(jsonfile)
	return myjson['fragments']

def change_format(sec, offset):
	sec = sec.split('.')
	s = int(sec[0]) + offset
	ms = sec[1]
	st = f"{time.strftime('%H:%M:%S', time.gmtime(s))},{ms}"
	return st

def convert_to_subtitles(line_counter, jsonfile, offset, filepath):
	l = get_as_list(jsonfile)

	for i in l:
		line_counter += 1
		begin = change_format(i['begin'], offset)
		end = change_format(i['end'], offset)
		lines = i['lines']

		subtitle = f"{line_counter}\n"
		subtitle += f"{begin} --> {end}"
		for line in lines:
			subtitle += f"\n{line}"
		subtitle += "\n\n"
		with open(filepath, 'a') as f: f.write(subtitle)
	
	return line_counter


def main():
	print("CALCULATING count of audio slices")
	slice_counter = get_count_of_audio_slices()

	print("SPLITTING audios")
	split_audios()

	print("SPLITTING subtitles")
	split_subtitles(slice_counter)

	print("SENDING api is started")
	line_counter = 0
	for index in range(slice_counter):
		response = "EMPTY RESPONSE"

		# audio slice
		audio_slice_path = f"{INPUT_PATH}/pulp_fiction_audio_{index}.mp3"

		# subtitle slice
		subtitle_slice_path = f"{INPUT_PATH}/pulp_fiction_subtitle_{index}.txt"

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

		# merging
		offset = index * 10
		line_counter = convert_to_subtitles(line_counter, response, offset, SUBTITLE_OUTPUT_PATH)

		# remove slices
		os.remove(audio_slice_path)
		os.remove(subtitle_slice_path)


if __name__ == '__main__':
	main()