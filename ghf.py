class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0

        while i < len(words):
            line = []
            line_length = 0

            # Find words that can fit in this line
            while i < len(words):
                if line_length + len(words[i]) + len(line) > maxWidth:
                    break

                line.append(words[i])
                line_length += len(words[i])
                i += 1

            # Last line
            if i == len(words):
                result.append(" ".join(line).ljust(maxWidth))
                break

            # Only one word
            if len(line) == 1:
                result.append(line[0].ljust(maxWidth))
                continue

            # Distribute spaces
            total_spaces = maxWidth - line_length
            gaps = len(line) - 1

            spaces = total_spaces // gaps
            extra = total_spaces % gaps

            text = ""

            for j in range(gaps):
                text += line[j]
                text += " " * (spaces + (1 if j < extra else 0))

            text += line[-1]

            result.append(text)

        return result
