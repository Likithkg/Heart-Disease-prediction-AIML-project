from manager.ModelManager import ModelManager
import numpy as np

class DiseasesPrediction:
    def __init__(self):
        self.mm = ModelManager()

    def predict_diseases(self, user_input):
        input_data = np.array(user_input).reshape(1, -1)
        self.mm.load_models()
        predictions = self.mm.predict(input_data)
        final_prediction = self.mm.get_best_prediction(predictions)
        return final_prediction
