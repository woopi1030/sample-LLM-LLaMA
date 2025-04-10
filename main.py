from llama_cpp import Llama
from datetime import datetime
import json

# 모델 로딩
llm = Llama(
    model_path="./models/Meta-Llama-3-8B-Instruct.Q4_K_M.gguf",  # 경로 수정 필요
    n_ctx=2048,
    n_threads=4,  # CPU 스레드 수에 맞게 조정
)

# 오늘 날짜
today = datetime.today().strftime("%Y년 %m월 %d일")

# 프롬프트 구성 (역할 + 스타일 + few-shot + 포맷 모두 포함)
prompt = f"""
당신은 10년 경력의 운세 작가이며, 띠별 운세를 매일 작성합니다.
운세는 하루를 시작하는 사람에게 도움이 되도록 감정, 인간관계, 직장, 건강, 금전운 중 2~3가지를 포함해 1~2문단으로 작성합니다.
문체는 부드럽고 따뜻하며, 실용적인 조언도 포함되어야 합니다.

1. 띠별 운세 (12간지): 
    - 각 띠(쥐, 소, 호랑이, 토끼, 용, 뱀, 말, 양, 원숭이, 닭, 개, 돼지)에 대해
    - 해당 띠에 속하는 주요 출생 연도별 운세도 포함시켜 주세요. (예: 쥐띠 - 1948, 1960, 1972, 1984, 1996)

2. 별자리 운세:
    - 양자리, 황소자리, 쌍둥이자리, 게자리, 사자자리, 처녀자리, 천칭자리, 전갈자리, 사수자리, 염소자리, 물병자리, 물고기자리

    
띠별과 별자리 운세를 아래 JSON 형식에 맞춰 출력해주세요.
- 오늘은 {today}입니다.
- "date" 필드에 오늘 날짜({datetime.today().strftime("%Y%m%d")})를 실제로 포함시켜주세요.
- 출력은 모두 한국어로 작성해주세요. 영어 단어를 섞지 말고, 문장도 완전하게 써주세요.
- 각 항목은 가능하면 빠짐없이 1문단 이상 채워주세요.


- JSON 형식은 아래와 같습니다. (예시로 작성된 내용은 무시하세요.)
{{
    "date": "YYYYMMDD",
    "horoscope": {{
        "chinese_zodiac": {{
            "rat": {{
                "1948" : "",
                "1960" : "",
                "1972" : "",
                "1984" : "",
                "1996" : ""
            }},
            "ox": {{
                "1949" : "",
                "1961" : "",
                "1973" : "",
                "1985" : "",
                "1997" : ""
            }},
            "tiger": {{
                "1950" : "",
                "1962" : "",
                "1974" : "",
                "1986" : "",
                "1998" : ""
            }},
            "rabbit": {{
                "1951" : "",
                "1963" : "",
                "1975" : "",
                "1987" : "",
                "1999" : ""
            }},
            "dragon": {{
                "1952" : "",
                "1964" : "",
                "1976" : "",
                "1988" : "",
                "2000" : ""
            }},
            "snake": {{
                "1953" : "",
                "1965" : "",
                "1977" : "",
                "1989" : "",
                "2001" : ""
            }},
            "horse": {{
                "1954" : "",
                "1966" : "",
                "1978" : "",
                "1990" : "",
                "2002" : ""
            }},
            "sheep": {{
                "1955" : "",
                "1967" : "",
                "1979" : "",
                "1991" : "",
                "2003" : ""
            }},
            "monkey": {{
                "1956" : "",
                "1968" : "",
                "1980" : "",
                "1992" : "",
                "2004" : ""
            }},
            "rooster": {{
                "1957" : "",
                "1969" : "",
                "1981" : "",
                "1993" : "",
                "2005" : ""
            }},
            "dog": {{
                "1958" : "",
                "1970" : "",
                "1982" : "",
                "1994" : "",
                "2006" : ""
            }},
            "pig": {{
                "1959" : "",
                "1971" : "",
                "1983" : "",
                "1995" : "",
                "2007" : ""
            }}
        }},
        "zodiac_sign": {{
            "aries": "",
            "taurus": "",
            "gemini": "",
            "cancer": "",
            "leo": "",
            "virgo": "",
            "libra": "",
            "scorpio": "",
            "sagittarius": "",
            "capricorn": "",
            "aquarius": "",
            "pisces": ""
        }}
    }}
}}
"""

# 운세 생성
response = llm(
    prompt,
    max_tokens=4096,                            # 전체 길이 제한
    temperature=0.85,                           # 창의성 조절
    top_p=0.9,                                  # 상위 확률 내에서 샘플링
    repeat_penalty=1.15,                        # 중복 억제
    # stop=["\n\n", "\n    }", "\n  }", "\n}"]    # JSON 형식 종료를 위한 중지 토큰
)

# 결과 추출

try:
    result = response["choices"][0]["text"]
    print(result)
    json_start = result.find("{")
    result_json = result[json_start:]
    parsed = json.loads(result_json)
    # print(f"=== 운세 결과 ({today}) ===")
    # print(json.dumps(parsed, ensure_ascii=False, indent=2))
except json.JSONDecodeError as e:
    print("❌ JSON 파싱 실패!")
    print("오류 메시지:", str(e))
    print("출력 일부 확인:\n")
    print(result_json[:1000])