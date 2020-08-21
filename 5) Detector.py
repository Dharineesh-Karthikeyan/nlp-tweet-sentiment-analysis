## Emoticon Detector
class EmoticonDetector:
    emoticons = {}

    def __init__(self, emoticon_file="data/emoticons.txt"):
        from pathlib import Path
        content = Path(emoticon_file).read_text()
        positive = True
        for line in content.split("\n"):
            if "positive" in line.lower():
                positive = True
                continue
            elif "negative" in line.lower():
                positive = False
                continue

            self.emoticons[line] = positive

    def is_positive(self, emoticon):
        if emoticon in self.emoticons:
            return self.emoticons[emoticon]
        return False

    def is_emoticon(self, to_check):
        return to_check in self.emoticons


## word Detector

class wordDetector:
    words = {}

    def __init__(self, word_file="data/words.txt"):
        from pathlib import Path
        content = Path(word_file).read_text()
        positive = True
        for line in content.split("\n"):
            if "positive" in line.lower():
                positive = True
                continue
            elif "negative" in line.lower():
                positive = False
                continue

            self.words[line] = positive

    def is_positive(self, word):
        if word in self.words:
            return self.words[word]
        return False

    def is_word(self, to_check):
        return to_check in self.words
    
