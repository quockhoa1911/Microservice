from rest_framework import parsers
import json

class Mutilpart_Json_Parsers(parsers.MultiPartParser):
    def parse(self, stream, media_type=None, parser_context=None):
        result = super().parse(stream=stream,media_type=media_type,parser_context=parser_context)
        data = json.loads(result.data['data'])
        return parsers.DataAndFiles(data=data,files=result.files)