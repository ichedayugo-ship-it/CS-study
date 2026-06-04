# app.py

import streamlit as st

QUESTIONS = [
    # A. 明示性
    {"id": 1, "text": "相手の発表や成果物に問題があると感じたら、その問題点をはっきり言う方だ。", "category": "clarity"},
    {"id": 2, "text": "相手に改善してほしい点があるとき、遠回しな表現よりも直接伝える方がよいと思う。", "category": "clarity"},
    {"id": 3, "text": "フィードバックでは、相手が誤解しないように、問題点を明確に言葉にするべきだと思う。", "category": "clarity"},
    {"id": 4, "text": "「少し気になるところがあります」よりも、「ここに問題があります」と伝える方が自分には自然だ。", "category": "clarity"},
    {"id": 5, "text": "相手が傷つく可能性があっても、必要な指摘ははっきり伝えるべきだと思う。", "category": "clarity"},
    {"id": 6, "text": "改善点を曖昧に伝えると、相手のためにならないと感じる。", "category": "clarity"},
    {"id": 7, "text": "相手の意見に反対するとき、自分は比較的はっきり反対意見を言う方だ。", "category": "clarity"},
    {"id": 8, "text": "フィードバックでは、良い点よりも先に問題点を伝えることに抵抗が少ない。", "category": "clarity"},
    {"id": 9, "text": "相手が気づいていない問題は、こちらから明確に指摘する必要があると思う。", "category": "clarity"},
    {"id": 10, "text": "「もう少し工夫できるかも」という言い方より、「ここを直した方がよい」という言い方の方が分かりやすいと思う。", "category": "clarity"},

    # B. 主導性
    {"id": 11, "text": "フィードバックをするとき、自分は改善方法まで示すことが多い。", "category": "leadership"},
    {"id": 12, "text": "相手が迷わないように、何をどう直すべきかをこちらから伝える方がよいと思う。", "category": "leadership"},
    {"id": 13, "text": "改善の方向性は、相手に考えさせるよりも、経験のある人が示した方が効率的だと思う。", "category": "leadership"},
    {"id": 14, "text": "相手の成果物に問題があるとき、「こう直してください」と具体的に指示する方だ。", "category": "leadership"},
    {"id": 15, "text": "フィードバックでは、相手に自由に考えさせるよりも、明確な修正方針を与える方が親切だと思う。", "category": "leadership"},
    {"id": 16, "text": "相手が改善に時間をかけすぎないように、こちらが進め方を決めた方がよい場面が多いと思う。", "category": "leadership"},
    {"id": 17, "text": "相手に質問を投げかけるよりも、先に自分の考える改善案を伝えることが多い。", "category": "leadership"},
    {"id": 18, "text": "グループ作業では、改善点が見えた人が修正方針を決めるべきだと思う。", "category": "leadership"},
    {"id": 19, "text": "相手の成長を考える場合でも、まずは正しいやり方を示すことが大切だと思う。", "category": "leadership"},
    {"id": 20, "text": "フィードバック後に相手が迷わないように、次の進め方はこちらから指定する方がよいと思う。", "category": "leadership"},

    # C. 行動具体性
    {"id": 21, "text": "フィードバックでは、相手が次に何をすればよいかまで伝えるようにしている。", "category": "concreteness"},
    {"id": 22, "text": "「もっと分かりやすく」だけでなく、どこをどう変えるべきかまで伝える方がよいと思う。", "category": "concreteness"},
    {"id": 23, "text": "改善点を伝えるときは、できるだけ具体例を出すようにしている。", "category": "concreteness"},
    {"id": 24, "text": "相手にフィードバックをするとき、実際に使える表現や修正案を示すことが多い。", "category": "concreteness"},
    {"id": 25, "text": "問題点を指摘するだけではなく、次の行動に結びつくアドバイスをするべきだと思う。", "category": "concreteness"},
    {"id": 26, "text": "「説得力が足りない」と言うだけでなく、どこに根拠を足すべきかまで伝える方がよいと思う。", "category": "concreteness"},
    {"id": 27, "text": "相手がすぐ行動に移せるフィードバックが、良いフィードバックだと思う。", "category": "concreteness"},
    {"id": 28, "text": "抽象的な感想よりも、具体的な改善案を伝える方が相手の役に立つと思う。", "category": "concreteness"},
    {"id": 29, "text": "フィードバックでは、「何が問題か」だけでなく「どうすればよくなるか」まで示したい。", "category": "concreteness"},
    {"id": 30, "text": "自分のフィードバックを聞いた相手が、次に何をすればよいか分かる状態にしたい。", "category": "concreteness"},

    # D. 配慮対象
    {"id": 31, "text": "相手との関係が少し悪くなっても、成果物を良くするために必要なことは言うべきだと思う。", "category": "priority"},
    {"id": 32, "text": "フィードバックでは、相手の気持ちよりも、課題や成果の改善を優先することが多い。", "category": "priority"},
    {"id": 33, "text": "相手が落ち込む可能性があっても、問題点を正確に伝えることの方が大切だと思う。", "category": "priority"},
    {"id": 34, "text": "関係を守るために指摘を弱めると、かえって相手の成長を妨げると思う。", "category": "priority"},
    {"id": 35, "text": "フィードバックの目的は、まず成果物や行動を改善することだと思う。", "category": "priority"},
    {"id": 36, "text": "相手が受け入れやすい言い方を考えるよりも、必要な情報を正確に伝えることを重視する。", "category": "priority"},
    {"id": 37, "text": "厳しい指摘でも、相手のためになるなら伝えるべきだと思う。", "category": "priority"},
    {"id": 38, "text": "フィードバックでは、場の空気よりも、改善すべき内容を優先する方だ。", "category": "priority"},
    {"id": 39, "text": "相手に遠慮して大事な問題点を言わないのは、良いフィードバックではないと思う。", "category": "priority"},
    {"id": 40, "text": "フィードバックでは、相手にどう受け取られるかよりも、何を改善すべきかを重視する。", "category": "priority"},

    # E-1. 面子・上下関係配慮
    {"id": 41, "text": "自分より立場が上の人に反対意見を言うことには抵抗がある。", "category": "face"},
    {"id": 42, "text": "人前で注意されたり、問題点を指摘されたりすることに強い抵抗がある。", "category": "face"},
    {"id": 43, "text": "相手との関係を悪くするくらいなら、問題点をはっきり言わない方がよいと思う。", "category": "face"},
    {"id": 44, "text": "自分の育ってきた環境では、相手の面子や立場を守ることが大切にされていた。", "category": "face"},
    {"id": 45, "text": "フィードバックを受けるときは、まず良い点を言ってもらえると受け入れやすい。", "category": "face"},

    # E-2. 率直性・明確性志向
    {"id": 46, "text": "率直に意見を言い合えることは、信頼関係がある証拠だと思う。", "category": "direct_preference"},
    {"id": 47, "text": "遠回しに言われると、何を直せばよいのか分からなくなることがある。", "category": "direct_preference"},
    {"id": 48, "text": "自分の育ってきた環境では、効率よく問題点を指摘することが大切にされていた。", "category": "direct_preference"},
    {"id": 49, "text": "フィードバックを受けるときは、遠回しな表現よりも、はっきり言ってもらう方が助かる。", "category": "direct_preference"},
    {"id": 50, "text": "フィードバックを受けるとき、相手の本音が分からない言い方をされると不安になる。", "category": "direct_preference"},

    # E-3. 状況適応・空気読み
    {"id": 51, "text": "相手の表情や空気を読んで、自分の言い方を変えることが多い。", "category": "adaptability"},
    {"id": 52, "text": "一対一で伝える場合と、人前で伝える場合では、フィードバックの言い方を変える方だ。", "category": "adaptability"},
    {"id": 53, "text": "相手の文化的背景や価値観が分からないときは、まず相手が受け入れやすそうな言い方を選ぶ。", "category": "adaptability"},
    {"id": 54, "text": "締切が近い、危険がある、ミスが重大であるなど緊急性が高い場面では、普段よりもはっきり伝える方だ。", "category": "adaptability"},
    {"id": 55, "text": "相手が自分で考えたいタイプか、具体的な指示を求めるタイプかによって、改善案の出し方を変える。", "category": "adaptability"},
]


TYPE_RESULTS = {
    "DGCT": {
        "name": "実行命令型",
        "style": "直接的・指示的・具体的・課題優先",
        "summary": "問題点をはっきり伝え、改善方法も具体的に示すタイプです。成果物や行動を良くすることを重視します。",
        "strength": "明確で実行に移しやすいフィードバックができます。",
        "risk": "相手によっては、厳しい、命令されている、否定されたと受け取られる可能性があります。",
        "advice": "最初に相手の努力や意図を一言認めてから、改善点を伝えるとよいです。",
        "phrase": "全体としてここまで形にできているのは良いと思います。そのうえで、次はこの部分を直す必要があります。"
    },
    "DGCR": {
        "name": "配慮ある実行指示型",
        "style": "直接的・指示的・具体的・関係配慮",
        "summary": "問題点をはっきり伝えながらも、相手が受け入れやすい形で改善方法を示すタイプです。",
        "strength": "明確さと配慮のバランスがあります。",
        "risk": "改善方法をこちらが決めすぎると、相手が自分で考える余地を失うことがあります。",
        "advice": "改善案を出すときは「一つの方法として」と添えるとよいです。",
        "phrase": "ここは少し直すともっと良くなりそうです。一つの方法として、この部分に具体例を追加してみるのはどうでしょうか。"
    },
    "DGAT": {
        "name": "厳格評価型",
        "style": "直接的・指示的・抽象的・課題優先",
        "summary": "問題点をはっきり伝え、改善の必要性も強く示すタイプです。",
        "strength": "課題を見逃さず、改善が必要な部分を明確に指摘できます。",
        "risk": "改善方法が抽象的だと、相手がどう直せばよいか分からなくなることがあります。",
        "advice": "必ず具体例を一つ加えるとよいです。",
        "phrase": "この部分はまだ説得力が弱いです。特に、理由の説明が足りません。"
    },
    "DGAR": {
        "name": "慎重な改善指摘型",
        "style": "直接的・指示的・抽象的・関係配慮",
        "summary": "相手に配慮しながらも、必要な問題点は比較的はっきり伝えるタイプです。",
        "strength": "関係を壊しすぎずに、改善の必要性を伝えられます。",
        "risk": "具体的な行動が不足すると、相手が何をすればよいか分からないことがあります。",
        "advice": "最後に一つだけ具体的な行動を付け加えるとよいです。",
        "phrase": "全体の方向性は悪くないですが、少し伝わりにくい部分があります。まずは最初に結論を入れてみるとよいと思います。"
    },
    "DSCT": {
        "name": "率直な伴走改善型",
        "style": "直接的・提案的・具体的・課題優先",
        "summary": "問題点をはっきり伝えながらも、改善方法を一方的に決めず、相手に考える余地を残すタイプです。",
        "strength": "明確さ、具体性、対話性を同時に持っています。",
        "risk": "課題優先の姿勢が強く出ると、冷たく感じられることがあります。",
        "advice": "問題点を伝える前に、相手の意図を確認するとよいです。",
        "phrase": "ここは少し伝わりにくいと感じました。意図としては何を一番伝えたかったですか。"
    },
    "DSCR": {
        "name": "対話的改善型",
        "style": "直接的・提案的・具体的・関係配慮",
        "summary": "問題点を比較的はっきり伝えながらも、相手に考える余地を残し、具体的な改善につなげるタイプです。",
        "strength": "明確さ、具体性、相手への配慮のバランスが良いです。",
        "risk": "遠慮深い相手には、率直さが少し強く感じられることがあります。",
        "advice": "相手の反応を見ながら、必要に応じて言い換えるとよいです。",
        "phrase": "全体の方向性はとても良いと思います。そのうえで、ここを一つ変えるともっと伝わりやすくなりそうです。"
    },
    "DSAT": {
        "name": "率直な問いかけ型",
        "style": "直接的・提案的・抽象的・課題優先",
        "summary": "問題点をはっきり伝えつつ、改善方法は相手に考えさせるタイプです。",
        "strength": "相手に考える機会を与えられます。",
        "risk": "改善案が抽象的になりやすく、経験の少ない相手は迷うことがあります。",
        "advice": "問いかけのあとに具体例を一つ添えるとよいです。",
        "phrase": "この部分は少し説得力が弱いと思います。どこに具体例を入れられそうですか。"
    },
    "DSAR": {
        "name": "対話重視の率直型",
        "style": "直接的・提案的・抽象的・関係配慮",
        "summary": "相手との関係に配慮しながら、問題点は比較的はっきり伝えるタイプです。",
        "strength": "相手を尊重しながら率直に話せます。",
        "risk": "具体性が不足すると、相手が次に何をすればよいか分からないことがあります。",
        "advice": "話し合いの最後に、次の一歩を確認するとよいです。",
        "phrase": "この部分は少し伝わりにくいかもしれません。どう直せそうだと思いますか。"
    },
    "IGCT": {
        "name": "柔らかい実務指示型",
        "style": "間接的・指示的・具体的・課題優先",
        "summary": "問題点を強く言いすぎないようにしながら、改善方法は具体的に示すタイプです。",
        "strength": "相手に強い圧をかけずに、次の行動を示せます。",
        "risk": "間接的な表現が多くなると、問題の重要度が伝わりにくいことがあります。",
        "advice": "重要な点だけは少し明確に言うとよいです。",
        "phrase": "かなり良くなってきています。さらに良くするために、ここは少し修正した方がよさそうです。"
    },
    "IGCR": {
        "name": "サポート指示型",
        "style": "間接的・指示的・具体的・関係配慮",
        "summary": "相手に配慮しながら、具体的な改善方法を示すタイプです。",
        "strength": "安心感のあるフィードバックができます。",
        "risk": "柔らかすぎると、相手が必ず直すべき点だと気づかないことがあります。",
        "advice": "優先順位をはっきり示すとよいです。",
        "phrase": "全体として良い方向に進んでいると思います。まず一つ直すなら、この部分を短くするとよさそうです。"
    },
    "IGAT": {
        "name": "遠回しな改善要求型",
        "style": "間接的・指示的・抽象的・課題優先",
        "summary": "成果や改善を重視しながらも、問題点を強く言いすぎないようにするタイプです。",
        "strength": "衝突を避けながら改善の方向へ導こうとできます。",
        "risk": "成果を求めているのに、相手には重要度が伝わらない可能性があります。",
        "advice": "具体性を大きく上げるとよいです。",
        "phrase": "もう少し良くできそうです。特に、説明の順番を変えると分かりやすくなると思います。"
    },
    "IGAR": {
        "name": "やわらかい方向づけ型",
        "style": "間接的・指示的・抽象的・関係配慮",
        "summary": "相手を傷つけないように気を配りながら、改善の方向へ導こうとするタイプです。",
        "strength": "相手に安心感を与えやすいです。",
        "risk": "問題点と改善方法の両方が曖昧になりやすいです。",
        "advice": "柔らかい言い方のままでよいので、一つだけ具体的な行動を入れるとよいです。",
        "phrase": "全体的にはよくまとまっていると思います。もし少しだけ直すなら、最初に結論を入れるとよいと思います。"
    },
    "ISCT": {
        "name": "柔らかい伴走改善型",
        "style": "間接的・提案的・具体的・課題優先",
        "summary": "問題点を強く言いすぎず、相手に考える余地を残しながら、具体的な改善案を出すタイプです。",
        "strength": "相手の主体性を尊重しながら、行動につながるヒントを渡せます。",
        "risk": "重要度が参考意見程度に受け取られることがあります。",
        "advice": "改善の優先順位を明確にするとよいです。",
        "phrase": "さらに良くするなら、まずこの部分を変えるのが効果的だと思います。"
    },
    "ISCR": {
        "name": "伴走サポート型",
        "style": "間接的・提案的・具体的・関係配慮",
        "summary": "相手に配慮しながら、具体的な改善案を提案するタイプです。",
        "strength": "安心感と実用性の両方があります。",
        "risk": "緊急性が高い場面では、やや弱く見えることがあります。",
        "advice": "重要な場面では、明示性を少し上げるとよいです。",
        "phrase": "とても良い方向に進んでいると思います。さらに伝わりやすくするなら、ここを少し変えるとよさそうです。"
    },
    "ISAT": {
        "name": "遠回しな問いかけ型",
        "style": "間接的・提案的・抽象的・課題優先",
        "summary": "成果を良くしたい気持ちはありながらも、問題点を強く言わず、改善方法も相手に考えてもらおうとするタイプです。",
        "strength": "相手に考える余白を与えられます。",
        "risk": "意図が伝わりにくく、問題の重要性が理解されない可能性があります。",
        "advice": "抽象的な問いかけだけで終わらせず、具体的な選択肢を一つ出すとよいです。",
        "phrase": "もう少し伝わりやすくできそうです。どこを変えるとよいと思いますか。"
    },
    "ISAR": {
        "name": "やさしい対話型",
        "style": "間接的・提案的・抽象的・関係配慮",
        "summary": "相手との関係を大切にしながら、柔らかく対話的にフィードバックするタイプです。",
        "strength": "相手に安心感を与えやすいです。",
        "risk": "改善点が伝わりにくく、相手が特に問題はなかったと受け取る可能性があります。",
        "advice": "最後に具体的な改善点を一つだけ残すとよいです。",
        "phrase": "全体的に良いと思います。もし一つだけ変えるなら、最初に結論を入れるともっと分かりやすくなりそうです。"
    },
}


def calculate_scores(answers):
    scores = {
        "clarity": 0,
        "leadership": 0,
        "concreteness": 0,
        "priority": 0,
        "face": 0,
        "direct_preference": 0,
        "adaptability": 0,
    }

    for question in QUESTIONS:
        scores[question["category"]] += answers[question["id"]]

    return scores


def judge_main_type(scores):
    clarity_code = "D" if scores["clarity"] >= 31 else "I"
    leadership_code = "G" if scores["leadership"] >= 31 else "S"
    concreteness_code = "C" if scores["concreteness"] >= 31 else "A"
    priority_code = "T" if scores["priority"] >= 31 else "R"
    return clarity_code + leadership_code + concreteness_code + priority_code


def describe_axis_score(score, low_label, high_label):
    if score <= 24:
        return f"{low_label}の傾向が強い"
    elif score <= 34:
        if score >= 31:
            return f"中間・状況依存。やや{high_label}寄り"
        else:
            return f"中間・状況依存。やや{low_label}寄り"
    else:
        return f"{high_label}の傾向が強い"


def describe_correction_score(score):
    if score <= 11:
        return "低い"
    elif score <= 18:
        return "中間"
    else:
        return "高い"


def get_correction_message(face_level, direct_level, adaptability_level):
    messages = []

    if face_level == "高い":
        messages.append("面子・上下関係配慮が高いです。相手の立場や人前での見え方に敏感で、関係を壊さない伝え方が得意です。ただし、配慮しすぎると改善点が曖昧になることがあります。")
    elif face_level == "中間":
        messages.append("面子・上下関係配慮は中間です。相手や場面によって、率直さと配慮を使い分ける傾向があります。")
    else:
        messages.append("面子・上下関係配慮は低めです。率直に伝えることに抵抗が少ない一方で、相手によっては少し強く聞こえる場合があります。")

    if direct_level == "高い":
        messages.append("率直性・明確性志向が高いです。遠回しな表現よりも、はっきりしたフィードバックを好む傾向があります。異文化場面では、最初に一言クッションを入れると受け入れられやすくなります。")
    elif direct_level == "中間":
        messages.append("率直性・明確性志向は中間です。相手や場面によって、はっきり言うことと柔らかく伝えることを使い分けられます。")
    else:
        messages.append("率直性・明確性志向は低めです。柔らかい伝え方を好む傾向がありますが、相手によっては意図が伝わりにくくなることがあります。")

    if adaptability_level == "高い":
        messages.append("状況適応・空気読みが高いです。相手との関係性、場面、緊急性に応じて伝え方を変えられる力があります。")
    elif adaptability_level == "中間":
        messages.append("状況適応・空気読みは中間です。ある程度は相手や場面に合わせられますが、強い緊張や急ぎの場面では普段のスタイルが出やすいかもしれません。")
    else:
        messages.append("状況適応・空気読みは低めです。自分のスタイルが一貫している一方で、異文化場面では相手に合わせた調整が課題になることがあります。")

    return messages


def show_question_section(title, category):
    st.subheader(title)

    answers = {}

    for question in QUESTIONS:
        if question["category"] == category:
            answers[question["id"]] = st.radio(
                f"Q{question['id']}. {question['text']}",
                options=[1, 2, 3, 4, 5],
                format_func=lambda x: {
                    1: "1：まったく当てはまらない",
                    2: "2：あまり当てはまらない",
                    3: "3：どちらともいえない",
                    4: "4：やや当てはまる",
                    5: "5：とても当てはまる",
                }[x],
                index=2,
                key=f"q_{question['id']}",
            )

    return answers


def main():
    st.set_page_config(
        page_title="異文化フィードバック・スタイル診断",
        page_icon="🗣️",
        layout="centered"
    )

    st.title("異文化フィードバック・スタイル診断")
    st.write(
        "この診断では、あなたのフィードバック傾向を、"
        "明示性・主導性・行動具体性・配慮対象の4軸から分析します。"
        "さらに、文化背景や状況適応の傾向も補正情報として表示します。"
    )

    st.info("回答はすべて5段階評価です。迷った場合は「3：どちらともいえない」を選んでください。")

    with st.expander("回答基準を見る"):
        st.write("1：まったく当てはまらない")
        st.write("2：あまり当てはまらない")
        st.write("3：どちらともいえない")
        st.write("4：やや当てはまる")
        st.write("5：とても当てはまる")

    all_answers = {}

    with st.expander("A. 明示性：間接的 / 直接的", expanded=True):
        all_answers.update(show_question_section("A. 明示性", "clarity"))

    with st.expander("B. 主導性：提案的 / 指示的"):
        all_answers.update(show_question_section("B. 主導性", "leadership"))

    with st.expander("C. 行動具体性：抽象的 / 具体的"):
        all_answers.update(show_question_section("C. 行動具体性", "concreteness"))

    with st.expander("D. 配慮対象：関係配慮 / 課題優先"):
        all_answers.update(show_question_section("D. 配慮対象", "priority"))

    with st.expander("E-1. 面子・上下関係配慮"):
        all_answers.update(show_question_section("E-1. 面子・上下関係配慮", "face"))

    with st.expander("E-2. 率直性・明確性志向"):
        all_answers.update(show_question_section("E-2. 率直性・明確性志向", "direct_preference"))

    with st.expander("E-3. 状況適応・空気読み"):
        all_answers.update(show_question_section("E-3. 状況適応・空気読み", "adaptability"))

    st.divider()

    if st.button("診断結果を見る", type="primary"):
        scores = calculate_scores(all_answers)
        type_code = judge_main_type(scores)
        result = TYPE_RESULTS[type_code]

        face_level = describe_correction_score(scores["face"])
        direct_level = describe_correction_score(scores["direct_preference"])
        adaptability_level = describe_correction_score(scores["adaptability"])
        correction_messages = get_correction_message(face_level, direct_level, adaptability_level)

        st.header("診断結果")

        st.subheader(f"{type_code}型：{result['name']}")
        st.write(f"**{result['style']}**")

        st.success(result["summary"])

        st.subheader("4軸スコア")
        col1, col2 = st.columns(2)

        with col1:
            st.metric("明示性", f"{scores['clarity']} / 50")
            st.write(describe_axis_score(scores["clarity"], "間接的", "直接的"))

            st.metric("主導性", f"{scores['leadership']} / 50")
            st.write(describe_axis_score(scores["leadership"], "提案的", "指示的"))

        with col2:
            st.metric("行動具体性", f"{scores['concreteness']} / 50")
            st.write(describe_axis_score(scores["concreteness"], "抽象的", "具体的"))

            st.metric("配慮対象", f"{scores['priority']} / 50")
            st.write(describe_axis_score(scores["priority"], "関係配慮", "課題優先"))

        st.subheader("文化・性格補正スコア")
        col3, col4, col5 = st.columns(3)

        with col3:
            st.metric("面子・上下関係配慮", f"{scores['face']} / 25")
            st.write(face_level)

        with col4:
            st.metric("率直性・明確性志向", f"{scores['direct_preference']} / 25")
            st.write(direct_level)

        with col5:
            st.metric("状況適応・空気読み", f"{scores['adaptability']} / 25")
            st.write(adaptability_level)

        st.subheader("強み")
        st.write(result["strength"])

        st.subheader("異文化間で起きやすいズレ")
        st.write(result["risk"])

        st.subheader("おすすめ調整")
        st.write(result["advice"])

        st.subheader("おすすめフレーズ")
        st.info(result["phrase"])

        st.subheader("文化補正メッセージ")
        for message in correction_messages:
            st.write(f"- {message}")


if __name__ == "__main__":
    main()