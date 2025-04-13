# sample-LLM-LLaMA
sample-LLM-LLaMA

# 🐉 띠/별자리 운세 생성기 (LLaMA 3 8B 기반)

매일 자정, Meta의 **LLaMA 3 8B Instruct 모델**을 사용해  
오늘의 **띠별 운세**와 **별자리 운세**를 자동으로 생성하고 저장하는 프로젝트입니다.

---

## ✅ 주요 기능

- 🧠 **LLaMA 3 8B** LLM 기반 운세 생성
- 📆 매일 자정 운세 자동 생성
- 🐭 띠별 12개 + 🌌 별자리 12개 총 24개 운세 생성
- 📦 DB 또는 파일로 저장 가능 (확장 가능)
- 🔁 재실행 시 매일 다른 운세 생성 (temperature 설정)

---

## 🧠 LLaMA 3 8B (GGUF) - Windows 환경 CPU-only 실행 가이드

Meta의 LLaMA 3 8B Instruct 모델을 Windows 환경의 CPU-only 서버에서 실행하기 위해  
**양자화된 GGUF 포맷**과 **`llama-cpp-python`** 라이브러리를 사용합니다.

---

### ✅ 1. llama-cpp-python 설치

Windows에서는 Python에서 GGUF 모델을 실행하기 위해 컴파일이 필요하므로,
Visual Studio C++ Build Tools가 선행되어야 합니다.

#### 1-1. Visual C++ 빌드 도구 설치

1. [Microsoft C++ Build Tools 다운로드](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
2. 설치 마법사에서 **"C++ build tools" 체크**
3. 필수 구성 요소:
   - MSVC v142 이상
   - Windows 10 SDK
   - CMake (선택 사항)
4. 설치 후 PC 재부팅

#### 1-2. pip로 설치

```bash
pip install llama-cpp-python



#### ✅ 2. 모델 다운로드 (GGUF 포맷)

이 프로젝트에서는 Meta의 LLaMA 3 8B Instruct 모델을 사용합니다.  
CPU-only 환경에서 효율적으로 실행하기 위해 **양자화된 GGUF 포맷 모델**을 사용합니다.

#### 📥 모델 다운로드 링크

- Hugging Face: [QuantFactory/Meta-Llama-3-8B-Instruct-GGUF](https://huggingface.co/models?sort=trending&search=Meta-Llama-3-8B-Instruct)

#### 📌 추천 모델 파일 (4bit 양자화)

| 파일명 | 설명 |
|--------|------|
| `Meta-Llama-3-8B-Instruct.Q4_K_M.gguf` | 4bit 양자화, 성능과 속도의 균형이 가장 좋음 |

> `Q4_K_M`은 CPU 실행 시 많이 사용되는 양자화 버전입니다.  
> 다른 버전도 사용할 수 있으나, Q4 또는 Q5 계열이 일반적으로 추천됩니다.

#### 📁 모델 저장 위치 예시

모델 파일을 다음과 같은 구조로 저장하는 것을 권장합니다:
project-root/ 
        ├── models/ 
        │ └── Meta-Llama-3-8B-Instruct.Q4_K_M.gguf 
        ├── your_code.py 
        └── README.md
