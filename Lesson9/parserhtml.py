import requests as r
class ParseHTML:
    def __init__(self, url : str):
        self.Counter : int = 0
        self.Url = url
        self.Result : dict = {}
    def ParseCoin(self, separator1:str, separator2:str, prefix:str):
        response = r.get(self.Url)
        response_text = response.text
        sequence1 = response_text.split(separator1)
        for parse_element_1 in sequence1:
            if parse_element_1.startswith(prefix):
                sequence2 = parse_element_1.split(separator2)
                for parse_element_2 in sequence2:
                    if parse_element_2.startswith(prefix) and parse_element_2[1].isdigit():
                        self.Result[self.Counter] = parse_element_2
                        self.Counter += 1
        self.Counter = 0

#test method Home work
    def ParseNBU(self, separator1:str, separator2:str):
        response = r.get(self.Url)
        response_text = response.text
        sequence1 = response_text.split(separator1)
        for parse_element_1 in sequence1:
            sequence2 = parse_element_1.split(separator2)
            for parse_element_2 in sequence2:
                if parse_element_2.isdigit():
                    self.Result[self.Counter] = parse_element_2
                    self.Counter += 1
        self.Counter = 0


