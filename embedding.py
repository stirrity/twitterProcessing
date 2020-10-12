
class Embedder(object):
    def __init__(self, embeddings_dict):
        self.dict = embeddings_dict

    def embed(self, tweet_text, text_length = 20, vector_size = 300, embedding_type = 'vector'):        
        types = {'glove': 0, 'vector': 1}

        cur_type = types[embedding_type]

        embedded_text = []
        for text in tweet_text:
            cur_text = []
            words = text.split()

            for ch in words:
                if ch == ' ':
                    continue    
                try:
                    item = self.dict[ch]
                except:
                    item = [0] * vector_size

                if cur_type == 0:
                    cur_text += list(item)
                elif cur_type == 1:
                    cur_text.append(list(item))

            if cur_type == 0:
                total_length = text_length * vector_size
                if len(cur_text) > total_length:
                    cur_text = cur_text[:total_length]
                else:
                    cur_text += [0] * (total_length - len(cur_text))
            else:
                if len(cur_text) > text_length:
                    cur_text = cur_text[:text_length]
                else:
                    cur_text += [[0] * vector_size] * (text_length - len(cur_text))           

            embedded_text.append(cur_text)
        return embedded_text