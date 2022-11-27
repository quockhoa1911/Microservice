from .mail_template import template

class Htmlfilter:
    @classmethod
    def parse_html_text(cls) -> str:
        return template