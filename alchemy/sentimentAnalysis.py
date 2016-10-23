import json
from os.path import join, dirname
from watson_developer_cloud import AlchemyLanguageV1


myString = 'I hate you, go die'

def analyzeString(textString):
	alchemy_language = AlchemyLanguageV1(api_key='df8f270a6f64bc6cab503b9018b9f4940d12eb76')
	combined_operations = ['doc-emotion', 'doc-sentiment']
	data = alchemy_language.combined(text=textString, extract=combined_operations)
	anger = float(data['docEmotions']['anger'])				#anger score
	joy = float(data['docEmotions']['joy'])					#joy score
	fear = float(data['docEmotions']['fear'])					#fear score
	sadness = float(data['docEmotions']['sadness'])			#sadness score
	disgust = float(data['docEmotions']['disgust'])			#disgust score
	overallSentiment = data['docSentiment']['type']		#will be a string, either "positive" or "negative"
	overallScore = float(data['docSentiment']['score'])		#will be a positive or negative number. The more negative value, the more negative sentiment
	sum = anger + joy + fear + sadness + disgust
	angerPercentage = anger / sum
	joyPercentage = joy / sum
	fearPercentage = fear / sum
	sadnessPercentage = sadness / sum
	disgustPercentage = disgust / sum
	percentages = [angerPercentage, joyPercentage, fearPercentage, sadnessPercentage, disgustPercentage];
	return percentages

#info = analyzeString(myString);
#print info['docSentiment']
# anger = info['docEmotions']['anger']				#anger score
# joy = info['docEmotions']['joy']					#joy score
# fear = info['docEmotions']['fear']					#fear score
# sadness = info['docEmotions']['sadness']			#sadness score
# disgust = info['docEmotions']['disgust']			#disgust score
# overallSentiment = info['docSentiment']['type']		#will be a string, either "positive" or "negative"
# overallScore = info['docSentiment']['score']		#will be a positive or negative number. The more negative value, the more negative sentiment

info = analyzeString(myString)

print(info)