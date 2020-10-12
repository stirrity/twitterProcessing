from textacy.preprocessing import replace, remove

class TextPreprocess(object):
    def __init__(self):
        pass

    def process(self, tweets, replace_urls=True, replace_phone_numbers=True, replace_currency_symbols=True, remove_accent=True, remove_punctuation=True):
        tweet_text = tweets['text'].values
        clean_text = [x.lower() for x in tweet_text]

        if replace_urls:
            clean_text = [replace.replace_urls(x, 'url') for x in clean_text]

        if replace_phone_numbers:
            clean_text = [replace.replace_phone_numbers(x) for x in clean_text]

        if replace_currency_symbols:
            clean_text = [replace.replace_currency_symbols(x) for x in clean_text]

        if remove_accent:
            clean_text = [remove.remove_accents(x) for x in clean_text]

        if remove_punctuation:
            clean_text = [remove.remove_punctuation(x) for x in clean_text]

        return clean_text