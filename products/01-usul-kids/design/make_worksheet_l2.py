"""Lesson 2 worksheet "Allah Created Us": 3 versions (A, B, C) for the owner.

Style and rules: worksheet_lib.py (owner's Lesson 3 feedback). Content only from
sources/lesson-02-allah-created-us.md (verified, fixes applied):
- the first matter, matn as quoted by Ibn Baz: «أَنَّ اللهَ خَلَقَنَا وَرَزَقَنَا ولم يتركنا هملاً», printed p. 29
  (harakat on «لَمْ يَتْرُكْنَا هَمَلًا» added for children; owner confirms).
- Ibn Baz: «الله خلق الخلق ليعبدوه فلم يخلقهم هملاً...» "Allah created us to worship Him. He did not create
  us for nothing." printed p. 29.
- al-Uthaymeen: «فلأننا لا نعيش إلا على طعام وشراب، والطعام والشراب خلقه الله» "We can't live without food and
  drink, and Allah is the One who created our food and drink." printed p. 30.
- The provision hadith is ON HOLD (no hadith number yet) and is not used.
- Circle activities only offer choices that come from the scholar's own sentence, so no made-up
  wrong statement about Allah is printed.
"""
from worksheet_lib import write

BASE = {
    "lesson": 2, "title": "Allah Created Us",
    "trace": [("خَلَقَنَا", "He created us"), ("رَزَقَنَا", "He provides for us")],
    "trace_size": 68, "row_h": 108, "base": 74, "label_w": 128,
    "match_left": ["خَلَقَنَا", "رَزَقَنَا", "لَمْ يَتْرُكْنَا هَمَلًا"],
    "match_right": ["He did not leave us without purpose", "He created us", "He provides for us"],
    "match_h": 186, "match_lw": 290, "match_rw": 250, "match_ar_size": 42,
    "bank": {"words": ["رَزَقَنَا", "لَمْ يَتْرُكْنَا هَمَلًا", "خَلَقَنَا"],
             "meanings": ["He created us", "He provides for us", "He did not leave us without purpose"],
             },
    "bank_box_h": 70,
}
WHY = {"kind": "circle", "said": "Shaykh Ibn Baz said:", "question": "Why did Allah create us?",
       "choices": ["To worship Him", "For nothing"]}
WHY_SRC = ("Meaning of the book's words \"Allah created us, provides for us, and did not leave us without purpose,\"\n"
           "      and of Shaykh Ibn Baz's words \"Allah created us to worship Him. He did not create us for nothing.\"\n"
           "      <i>Sharh Thalathat al-Usul</i>, Shaykh Abdul-Aziz Ibn Baz, Dar al-Masir, 1st ed., p. 29.")
FOOD = {"kind": "fill", "said": "Shaykh al-Uthaymeen said:", "before": "We cannot live without food and",
        "choices": ["drink", "toys", "shoes"]}
FOOD_SRC = ("Meaning of Shaykh al-Uthaymeen's words: \"We cannot live without food and drink, and Allah is the One who\n"
            "      created our food and drink.\" <i>Sharh Thalathat al-Usul</i>, Shaykh Muhammad ibn Salih al-Uthaymeen,\n"
            "      Dar al-Thurayya, 4th ed., p. 30. Matching words: Shaykh Ibn Baz's <i>Sharh</i>, Dar al-Masir, 1st ed., p. 29.")

VERSIONS = {
    "A": {**BASE, "acts": ["trace", "match", "act3"], "act3": WHY, "source": WHY_SRC},
    "B": {**BASE, "acts": ["trace", "bank", "act3"], "act3": WHY, "source": WHY_SRC},
    "C": {**BASE, "acts": ["trace", "match", "act3"], "act3": FOOD, "source": FOOD_SRC},
}

if __name__ == "__main__":
    for v, spec in VERSIONS.items():
        write(spec, f"lesson-02-worksheet-allah-created-us-v{v}")
    print("worksheets written")
