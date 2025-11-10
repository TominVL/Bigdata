from src.core.job.mapper import Mapper
import re
TOKEN_RE = re.compile(r"[A-Za-zА-Яа-яІіЇїЄєҐґ]+(?:[-'][A-Za-zА-Яа-яІіЇїЄєҐґ]+)*")

class LongWordsMapper(Mapper):
    def map(self, record, emit):
        for token in TOKEN_RE.findall(str(record).lower()):
            if len(token) > 5:
                emit("TOTAL_LONG_WORDS", 1)
