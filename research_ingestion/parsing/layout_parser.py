def group_words_into_lines(words, y_tolerance=3):
    lines = []

    for word in words:
        placed = False

        for line in lines:
            if abs(line["top"] - word["top"]) < y_tolerance:
                line["words"].append(word)
                placed = True
                break

        if not placed:
            lines.append({
                "top": word["top"],
                "words": [word]
            })

    return lines


def build_text_lines(lines):
    output = []

    for line in lines:
        sorted_words = sorted(line["words"], key=lambda x: x["x0"])
        text = " ".join([w["text"] for w in sorted_words])
        output.append(text)

    return output


def detect_columns(words, page_width):
    left = []
    right = []

    midpoint = page_width / 2

    for word in words:
        if word["x0"] < midpoint:
            left.append(word)
        else:
            right.append(word)

    return left, right