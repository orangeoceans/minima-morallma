############################################
# Reads a pre-formatted text of aphorisms and converts it into a JSON file.
# Each aphorism is stored as a sample, with its title in the instructions.
# Mostly for my convenience to experiment with the instruction text/format.
############################################

import json

instruction_sys = "You are Theodor Adorno. You are writing a new version of Minima Moralia, a collection of critical aphorisms. Here is one such aphorism."

aphorisms = []
with open("minima_moralia_full_text.txt", encoding="utf8") as mm_text:
    for line in mm_text:
        if line is None:
            break
        if line.strip().isnumeric():
            aphorisms.append({})
        elif not aphorisms[-1]:
            split_line = line.split("--", 1)
            aphorisms[-1]["title"] = split_line[0].replace(".", "").strip()
            aphorisms[-1]["body"] = split_line[1].strip()
        else:
            aphorisms[-1]["body"] += line.strip()

with open("minima_moralia.json", "w") as mm_json:
    sample_list = []
    for aphorism in aphorisms:
        sample_list.append(
            {
                "text": f"<s>[INST]<<SYS>>{instruction_sys}<</SYS>>{aphorism['title']} [/INST]{aphorism['body']} </s>"
            }
        )
    json.dump(sample_list, mm_json)
