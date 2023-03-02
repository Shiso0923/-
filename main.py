import random

# words.txtから単語リストを作成する
with open('words.txt', 'r') as f:
    words = [line.strip() for line in f]

# 最初の単語をユーザーに入力してもらう
print("しりとりを始めます。")
word = input("最初の単語を入力してください: ")
used_words = set()
used_words.add(word)

# ゲームループ
while True:
    last_char = word[-1]
    print(f"AIのターン ({last_char}から始まる単語を入力してください)")
    available_words = [w for w in words if w[0] == last_char and w not in used_words]
    if not available_words:
        print("もうAIが出せる単語がありません。あなたの勝ちです！")
        break
    ai_word = random.choice(available_words)
    print(f"AI: {ai_word}")
    used_words.add(ai_word)
    word = input(f"{ai_word[-1]}から始まる単語を入力してください: ")
    if word in used_words:
        print("その単語は既に使われています。")
        continue
    if word[0] != ai_word[-1]:
        print("AIが出した単語の最後の文字と異なる文字で始めてください。")
        continue
    used_words.add(word)

print("ゲーム終了")
