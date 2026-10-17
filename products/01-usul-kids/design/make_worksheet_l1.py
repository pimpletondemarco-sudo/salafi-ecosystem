"""Lesson 1 worksheet "The Four Things We Must Learn" (المسائل الأربع): 3 versions (A, B, C) for the owner.

Style and rules: worksheet_lib.py (owner's Lesson 3 feedback). Content only from
sources/lesson-01-four-matters.md (verified, fixes applied):
- the four matters, headed in al-Uthaymeen's Sharh Thalathat al-Usul: العلم، العمل به، الدعوة إليه،
  الصبر على الأذى فيه (printed pp. 19-24). The worksheet uses the head nouns; harakat added for children
  (owner confirms with the religious-content approval).
- al-Uthaymeen: «والعمل في الحقيقة هو ثمرة العلم» "Action is the fruit of knowledge." printed p. 22.
- Ibn Baz: «هذه المسائل يجب أن يتعلمها المؤمن والمؤمنة صغارا وكبارا» "Every believer, male and female,
  young and old, must learn these matters." printed p. 21.
"""
from worksheet_lib import write

AR = ["الْعِلْمُ", "الْعَمَلُ", "الدَّعْوَةُ", "الصَّبْرُ"]
BASE = {
    "lesson": 1, "title": "The Four Things We Must Learn",
    "trace": list(zip(AR, ["Knowledge", "Action", "Calling", "Patience"])),
    "trace_size": 60, "row_h": 86, "base": 58,
    "match_left": AR, "match_right": ["Patience", "Knowledge", "Calling others to it", "Acting on it"],
    "match_h": 196, "match_ar_size": 38, "match_rw": 230,
    "bank": {"words": ["الصَّبْرُ", "الْعِلْمُ", "الدَّعْوَةُ", "الْعَمَلُ"],
             "meanings": ["Knowledge", "Acting on it", "Calling others to it", "Patience"]},
}
FRUIT = {"kind": "fill", "said": "Shaykh al-Uthaymeen said:", "before": "Action is the fruit of",
         "choices": ["water", "knowledge", "sleep"]}
FRUIT_SRC = ("Meaning of Shaykh al-Uthaymeen's words: \"Action is the fruit of knowledge.\"\n"
             "      <i>Sharh Thalathat al-Usul</i>, Shaykh Muhammad ibn Salih al-Uthaymeen, Dar al-Thurayya, 4th ed., p. 22.")
WHO = {"kind": "circle", "said": "Shaykh Ibn Baz said:",
       "question": "Who must learn these four things?", "choices": ["Every believer, young and old", "Only grown-ups"]}
WHO_SRC = ("Meaning of Shaykh Ibn Baz's words: \"Every believer, male and female, young and old, must learn these matters.\"\n"
           "      <i>Sharh Thalathat al-Usul</i>, Shaykh Abdul-Aziz Ibn Baz, Dar al-Masir, 1st ed., p. 21.")

VERSIONS = {
    "A": {**BASE, "acts": ["trace", "match", "act3"], "act3": FRUIT, "source": FRUIT_SRC},
    "B": {**BASE, "acts": ["trace", "bank", "act3"], "act3": FRUIT, "source": FRUIT_SRC},
    "C": {**BASE, "acts": ["trace", "match", "act3"], "act3": WHO, "source": WHO_SRC},
}

if __name__ == "__main__":
    for v, spec in VERSIONS.items():
        write(spec, f"lesson-01-worksheet-four-things-v{v}")
    print("worksheets written")
