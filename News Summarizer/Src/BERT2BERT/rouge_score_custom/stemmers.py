import hazm
from nltk.stem import porter
from TurkishStemmer import TurkishStemmer
from nltk.stem.snowball import HungarianStemmer

stemmers = {
    "aa": None,
    "ab": None,
    "ae": None,
    "af": None,
    "ak": None,
    "am": None,
    "an": None,
    "ar": None,
    "as": None,
    "av": None,
    "ay": None,
    "az": None,
    "ba": None,
    "be": None,
    "bg": None,
    "bh": None,
    "bi": None,
    "bm": None,
    "bn": None,
    "bo": None,
    "br": None,
    "bs": None,
    "ca": None,
    "ce": None,
    "ch": None,
    "co": None,
    "cr": None,
    "cs": None,
    "cu": None,
    "cv": None,
    "cy": None,
    "da": None,
    "de": None,
    "dv": None,
    "dz": None,
    "ee": None,
    "el": None,
    "en": porter.PorterStemmer(),
    "eo": None,
    "es": None,
    "et": None,
    "eu": None,
    "fa": hazm.Stemmer(),
    "ff": None,
    "fi": None,
    "fj": None,
    "fo": None,
    "fr": None,
    "fy": None,
    "ga": None,
    "gd": None,
    "gl": None,
    "gn": None,
    "gu": None,
    "gv": None,
    "ha": None,
    "he": None,
    "hi": None,
    "ho": None,
    "hr": None,
    "ht": None,
    "hu": HungarianStemmer(),
    "hy": None,
    "hz": None,
    "ia": None,
    "id": None,
    "ie": None,
    "ig": None,
    "ii": None,
    "ik": None,
    "io": None,
    "is": None,
    "it": None,
    "iu": None,
    "ja": None,
    "jv": None,
    "ka": None,
    "kg": None,
    "ki": None,
    "kj": None,
    "kk": None,
    "kl": None,
    "km": None,
    "kn": None,
    "ko": None,
    "kr": None,
    "ks": None,
    "ku": None,
    "kv": None,
    "kw": None,
    "ky": None,
    "la": None,
    "lb": None,
    "lg": None,
    "li": None,
    "ln": None,
    "lo": None,
    "lt": None,
    "lu": None,
    "lv": None,
    "mg": None,
    "mh": None,
    "mi": None,
    "mk": None,
    "ml": None,
    "mn": None,
    "mr": None,
    "ms": None,
    "mt": None,
    "my": None,
    "na": None,
    "nb": None,
    "nd": None,
    "ne": None,
    "ng": None,
    "nl": None,
    "nn": None,
    "no": None,
    "nr": None,
    "nv": None,
    "ny": None,
    "oc": None,
    "oj": None,
    "om": None,
    "or": None,
    "os": None,
    "pa": None,
    "pi": None,
    "pl": None,
    "ps": None,
    "pt": None,
    "qu": None,
    "rm": None,
    "rn": None,
    "ro": None,
    "ru": None,
    "rw": None,
    "sa": None,
    "sc": None,
    "sd": None,
    "se": None,
    "sg": None,
    "si": None,
    "sk": None,
    "sl": None,
    "sm": None,
    "sn": None,
    "so": None,
    "sq": None,
    "sr": None,
    "ss": None,
    "st": None,
    "su": None,
    "sv": None,
    "sw": None,
    "ta": None,
    "te": None,
    "tg": None,
    "th": None,
    "ti": None,
    "tk": None,
    "tl": None,
    "tn": None,
    "to": None,
    "tr": TurkishStemmer(),
    "ts": None,
    "tt": None,
    "tw": None,
    "ty": None,
    "ug": None,
    "uk": None,
    "ur": None,
    "uz": None,
    "ve": None,
    "vi": None,
    "vo": None,
    "wa": None,
    "wo": None,
    "xh": None,
    "yi": None,
    "yo": None,
    "za": None,
    "zh": None,
    "zu": None,
}
