import os
import fasttext

class Classification:
  def __init__(self):
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'model-en.ftz')
    
    self.model = fasttext.load_model(file_path)

  def map_result(self, result):
    label_dict = {
      "__label__NEGATIVE": { "label": "negative", "message": "Your tweet is offensive! Don't post it!"},
      "__label__NEUTRAL": { "label": "neutral", "message": "Your tweet is ok, I guess.." },
      "__label__POSITIVE": { "label": "positive", "message": "This is a good tweet. Go ahead :)" }
    }

    return label_dict[result]

  def test(self, tweet):
    [labels, scores] = self.model.predict([tweet],k=3)
    result = [label[0] for label in labels][0]
    return self.map_result(result)
