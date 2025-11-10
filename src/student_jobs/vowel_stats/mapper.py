from src.core.job.mapper import Mapper
import re
TOKEN_RE = re.compile(r"[A-Za-zА-Яа-яІіЇїЄєҐґ]+(?:[-'][A-Za-zА-Яа-яІіЇїЄєҐґ]+)*")
VOWELS = set("aeiouаеєиіїоуюя")

class VowelStatsMapper(Mapper):
    def map(self, record, emit):
        for token in TOKEN_RE.findall(str(record).lower()):
            letters = [ch for ch in token if ch.isalpha()]
            if not letters:
                continue
            L = len(letters)
            v = sum(1 for ch in letters if ch in VOWELS)
            c = L - v
            emit(L, (v, c))
