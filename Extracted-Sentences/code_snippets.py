# Restrict the ground truths to only ML2xx
for key, value in raw_data.items():
  new_ground_truths = []
  for gt in value['ground_truths']:
    if gt.startswith("ML2"):
      new_ground_truths.append(gt)
  raw_data[key]['ground_truths'] = new_ground_truths
  
  # My clean function. You totally don't have to use this
  def clean(sentence):
    sentence = re.sub(r'[=~,:%;\[\]\(\)]', '', sentence)
    sentence = re.sub(r'--', ' ', sentence)
    sentence = re.sub(r'[^\-a-zA-Z][0-9]+', '', sentence) # numbers
    sentence = re.sub(r'^[0-9]+ ', '', sentence) # numbers at beginning
    sentence = re.sub(r'^([a-z] ){2,}', '', sentence)  # n a s a a u t h o ...

    sentence = re.sub(r' {2,}', ' ', sentence)  # extra spaces

    stop_words = set(stopwords.words('english'))
    stop_words.remove('t') 
    word_tokens = word_tokenize(sentence)  # look at tokenization of things like 'sage ii' vs 'sage-ii'  
    filtered_sentence = [w for w in word_tokens if not w in stop_words]

    sentence = ' '.join(filtered_sentence)
    sentence = re.sub(r' \.', '.', sentence)
    return sentence
