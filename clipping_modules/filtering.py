# !python -m spacy download en_core_web_lg
import json
import pandas as pd
import spacy
import statistics

nlp = spacy.load("en_core_web_lg")


class FilteringModule:
    def __init__(self):
        self.captions = []
        self.matrix = []
        self.matrix2 = []
        self.start_time = []
        self.end_time = []
        self.final_captions = []
        self.final_end = []
        self.final_start = []

    def similtude_matrix(self):
        for oracion in self.captions:
            valores = []
            for oracion2 in self.captions:
                valores.append(nlp(oracion).similarity(nlp(oracion2)))
                self.matrix2.append(nlp(oracion).similarity(nlp(oracion2)))
            self.matrix.append(valores)

    def phrase_filter(self):
        for k in range(len(self.matrix)):
            for j in range(k + 1):
                if self.matrix[k][j] > statistics.mean(self.matrix2) and \
                        (abs(self.start_time[k] - self.start_time[j]) < 1 or
                         abs(self.end_time[k] - self.end_time[j]) < 1 or
                         abs(self.end_time[k] - self.start_time[j]) < 1 or
                         abs(self.end_time[j] - self.start_time[k]) < 1):
                    self.captions[j] = self.captions[k]
                    minimo = min(self.start_time[k], self.start_time[j])
                    maximo = max(self.end_time[k], self.end_time[j])
                    self.start_time[k] = minimo
                    self.start_time[j] = minimo
                    self.end_time[k] = maximo
                    self.end_time[j] = maximo

        for element in list(set(self.captions)):
            index = self.captions.index(element)
            inicio = self.start_time[index]
            fin = self.end_time[index]
            self.final_captions.append(element)
            self.final_start.append(inicio)
            self.final_end.append(fin)

    def clear_vars(self):
        self.captions = []
        self.matrix = []
        self.matrix2 = []
        self.start_time = []
        self.end_time = []
        self.final_captions = []
        self.final_end = []
        self.final_start = []

    def filter_file(self, input_path, output_path, tiempo=30):
        df = pd.read_json(input_path, orient='records')

        for item in df.video_id.unique():
            print("Filtering video:", item)
            
            suma = 0
            for i in range(1, len(df[df['video_id'] == item]['captions'])):
                suma = suma + df[df['video_id'] == item]['duration'].reset_index(drop=True)[i - 1]
                for j in range(len(df[df['video_id'] == item]['captions'].reset_index(drop=True)[i])):
                    df[df['video_id'] == item]['captions'].reset_index(drop=True)[i][j]['start'] = \
                        df[df['video_id'] == item]['captions'].reset_index(drop=True)[i][j][
                            'start'] + suma  # df[df['video_id'] == item]['duration'].reset_index(drop=True)[i-1]
                    df[df['video_id'] == item]['captions'].reset_index(drop=True)[i][j]['end'] = \
                        df[df['video_id'] == item]['captions'].reset_index(drop=True)[i][j]['end'] + suma  # df[d
                    self.captions.append(
                        df[df['video_id'] == item]['captions'].reset_index(drop=True)[i][j]['sentence'])
                    self.start_time.append(df[df['video_id'] == item]['captions'].reset_index(drop=True)[i][j]['start'])
                    self.end_time.append(df[df['video_id'] == item]['captions'].reset_index(drop=True)[i][j]['end'])
            self.similtude_matrix()
            self.phrase_filter()
            captions_obj = {
                "video_id": item,
                "captions": [],
                "duration": df[df['video_id'] == item]['duration'].sum()
            }

            for num in range(len(self.final_captions)):
                captions_obj['captions'].append(
                    {'start': self.final_start[num],
                     'end': self.final_end[num],
                     'sentence': self.final_captions[num]}
                )

            # output_file_path = '/content/clips-223.json'
            with open(output_path, "r") as f:
                stored_captions = json.load(f)

            stored_captions.append(captions_obj)

            with open(output_path, "w") as f:
                json.dump(stored_captions, f)

            self.clear_vars()
