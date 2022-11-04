from transformers import pipeline
from flask import Flask, request, Response, jsonify

app = Flask(__name__)

@app.route('/api/analysis', methods=['POST'])
def main():
	review = request.form['review']
	review = review if len(review) <= 512 else review[0:512]
	result = sentiment_pipeline(review)
	label = result[0]
	return Response(response = label, status = 200, mimetype = "application/json")



if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
