from src.core.job.reducer import Reducer
import json

class VowelStatsReducer(Reducer):
    def reduce(self, key, values, emit):
        v_sum = c_sum = 0
        for v, c in values:
            v_sum += v
            c_sum += c
        total = v_sum + c_sum
        if total == 0:
            return
        emit(str(key), json.dumps({
            "vowels": v_sum,
            "consonants": c_sum,
            "vowels_pct": round(100*v_sum/total),
            "consonants_pct": 100 - round(100*v_sum/total)
        }, ensure_ascii=False))
