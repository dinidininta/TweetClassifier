import os
import fasttext

class Classification:
  def __init__(self):
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'model-en.ftz')
    
    self.model = fasttext.load_model(file_path)

  def test(self, tweet):
    [labels, scores] = self.model.predict([tweet],k=3)
    result = [label[0] for label in labels][0]
    return result
