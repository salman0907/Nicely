import json
from os.path import join, dirname
from watson_developer_cloud import AlchemyLanguageV1

alchemy_language = AlchemyLanguageV1(api_key='df8f270a6f64bc6cab503b9018b9f4940d12eb76')

myString = 'I hate you, go die'

def analyzeString(textString):
	combined_operations = ['doc-emotion', 'doc-sentiment']
	#print(json.dumps(alchemy_language.combined(text=textString, extract=combined_operations), indent=2))
	data = alchemy_language.combined(text=textString, extract=combined_operations)
	#return data["docEmotions"]
	#return {data["docSentiment"], data["docEmotions"]}
	return data

info = analyzeString(myString);
#print info['docSentiment']
anger = info['docEmotions']['anger']				#anger score
joy = info['docEmotions']['joy']					#joy score
fear = info['docEmotions']['fear']					#fear score
sadness = info['docEmotions']['sadness']			#sadness score
disgust = info['docEmotions']['disgust']			#disgust score
overallSentiment = info['docSentiment']['type']		#will be a string, either "positive" or "negative"
overallScore = info['docSentiment']['score']		#will be a positive or negative number. The more negative value, the more negative sentiment
