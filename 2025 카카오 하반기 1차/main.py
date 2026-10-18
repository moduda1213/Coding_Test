from collections import Counter
import re

def find_impr_words(message, spoiler_ranges):
    words = message.split()
    find_words = []

    for match in re.finditer(r"\S+", message):
        word = match.group()
        word_start = match.start()
        word_end = match.end()  # 마지막 글자의 다음 인덱스

        for range_start, range_end in spoiler_ranges:
            # 단어와 스포일러 범위가 한 글자 이상 겹침
            if word_start <= range_end and range_start < word_end:
                find_words.append(word)
                break

    # 전체 문장의 단어별 등장 횟수
    words_counts = Counter(words)

    # 스포일러 범위에서 발견된 단어별 횟수
    find_counts = Counter(find_words)

    # 모든 등장 위치가 스포일러 범위에 포함된 단어만 선택
    impr_words = [
        word
        for word, total_count in words_counts.items()
        if find_counts[word] == total_count
    ]

    print(f"전체 횟수: {words_counts}")
    print(f"발견 횟수: {find_counts}")
    print(f"스포일러 방지 단어: {impr_words}")

    return len(impr_words)
if __name__ == "__main__":
    # message = "here is muzi here is a secret message"
    # spoiler_ranges = [[0, 3], [23, 28]]
    message = "my phone number is 01012345678 and may i have your phone number"
    spoiler_ranges = [[5, 5], [25, 28], [34, 40], [53, 59]]
    result = find_impr_words(message, spoiler_ranges)
    print(f"최종: {result}")