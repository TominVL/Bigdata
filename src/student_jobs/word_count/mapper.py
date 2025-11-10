from src.core.job.mapper import Mapper
import re
TOKEN_RE = re.compile(r"[A-Za-zА-Яа-яІіЇїЄєҐґ]+(?:[-'][A-Za-zА-Яа-яІіЇїЄєҐґ]+)*")

class WordCountMapper(Mapper):
    def map(self, record, emit):
        for token in TOKEN_RE.findall(str(record).lower()):
            emit(token, 1)
