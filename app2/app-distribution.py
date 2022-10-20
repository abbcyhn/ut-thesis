import requests

FOG_API_ENDPOINT = "http://localhost:81/api/sync"
CLOUD_API_ENDPOINT = "http://http://172.17.90.194:81/api/sync"

def sendto(audio, subtitle, api_endpoint):
	response = requests.post(url = api_endpoint, files={'audio': audio, 'subtitle': subtitle})
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

def main():
	index = 0
	audio = readfile('input/p001.mp3')
	subtitle = readfile('input/p001.xhtml')

	while(True):
		
		response = "EMPTY RESPONSE"

		# send to fog
		if (index % 2 == 0):
			print("SENDING TO FOG")
			response = sendto(audio, subtitle, FOG_API_ENDPOINT)
			print("RETRIEVING FROM FOG")
		# send to cloud
		else:
			print("SENDING TO CLOUD")
			response = sendto(audio, subtitle, CLOUD_API_ENDPOINT)
			print("RETRIEVING FROM CLOUD")

		index += 1

		print(response)

if __name__ == '__main__':
	main()