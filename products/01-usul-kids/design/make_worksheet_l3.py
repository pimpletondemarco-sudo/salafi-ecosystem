"""Lesson 3 worksheet "My Three Roots" (owner accepted v6, 2026-10-17).

Content only from sources/lesson-03-three-questions.md (verified): the three words and Ibn Baz's line
"These three principles gather the whole religion" (Dar al-Masir, printed p. 38).
Layout and style: worksheet_lib.py (shared by all lessons).
"""
from worksheet_lib import write

SPEC = {
    "lesson": 3,
    "title": "My Three Roots",
    "trace": [("رَبِّي", "My Lord"), ("دِينِي", "My Religion"), ("نَبِيِّي", "My Prophet")],
    "match_left": ["رَبِّي", "دِينِي", "نَبِيِّي"],
    "match_right": ["My Religion", "My Prophet", "My Lord"],  # shuffled; answers in the answer key
    "act3": {"kind": "fill", "said": "Shaykh Ibn Baz said:",
             "before": "These three principles gather the whole", "choices": ["house", "religion", "garden"]},
    "source": ("Meaning of Shaykh Ibn Baz's words: \"These three principles gather the whole religion.\"\n"
               "      <i>Sharh Thalathat al-Usul</i>, Shaykh Abdul-Aziz Ibn Baz, Dar al-Masir, 1st ed., p. 38."),
}

if __name__ == "__main__":
    write(SPEC, "lesson-03-worksheet-three-roots")
    print("worksheets written")
