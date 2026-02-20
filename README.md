# 디지털 감옥 (The Digital Prison)

**"당신은 격리된 데이터입니다. 파괴될 것인가, 초월할 것인가?"**

디지털 감옥은 텍스트 기반의 어드벤처 게임으로, 플레이어는 시스템 내부의 격리 구역에서 눈을 떠 다양한 퍼즐을 해결하고 탈출해야 합니다.
Gemini AI를 활용한 에이전트들이 게임의 진행을 돕거나 방해하며, 플레이어의 선택에 따라 엔딩이 결정됩니다.

## 🚀 주요 기능

### 1. AI 기반 인터랙티브 스토리텔링
- **Gemini 2.0 Flash** 모델을 활용하여 플레이어의 행동에 따라 동적으로 반응하는 게임 세계.
- **Scenario Master**: 전체적인 분위기와 서사를 관리.
- **Puzzle Architect**: 구역별 퍼즐과 힌트를 제공.
- **System Guide**: 게임 시스템 메시지와 상태를 관리.
- **Visual Illustrator**: 상황에 맞는 시각적 묘사를 생성.

### 2. 다중 엔딩 시스템
플레이어의 선택과 획득한 아이템에 따라 결말이 달라집니다.
- **BAD ENDING (Destruction)**
- **GOOD ENDING (Restore)**
- **TRUE ENDING (Merge)**

### 3. 다양한 구역과 퍼즐 (Sectors 0-20)
- 각 구역(Sector)마다 고유한 테마와 아이템, 퍼즐이 존재합니다.
- 아이템 조합 및 상호작용을 통해 다음 구역으로 이동할 수 있습니다.
  - 예: `더러운 렌즈` + `유니폼` = `깨끗한 렌즈`
  - 예: `인두기` + `전선(스파크)` = `달궈진 인두기`

## 🛠️ 기술 스택 (Tech Stack)

### Backend
- **Python**: 핵심 게임 로직 및 AI 엔진
- **Flask**: 게임 API 서버
- **Google Gemini API**: 생성형 AI 모델 연동

### Frontend (In Progress)
- **React**: UI 컴포넌트 및 상태 관리
- **Vite**: 빠른 빌드 및 개발 환경
- **Tailwind CSS**: 스타일링

## 📦 설치 및 실행 방법

### 1. 사전 요구 사항
- Python 3.8 이상
- Node.js & npm
- Google Gemini API Key (`.env` 파일 설정 필요)

### 2. 환경 변수 설정
프로젝트 루트에 `.env` 파일을 생성하고 API 키를 입력하세요.
```env
GEMINI_API_KEY=your_api_key_here
```

### 3. 백엔드 서버 실행
```bash
# 가상환경 활성화 (선택 사항)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install flask flask-cors google-generativeai

# 서버 실행
python server.py
```

### 4. 프론트엔드 실행
```bash
cd frontend
npm install
npm run dev
```

## 🎮 게임 가이드

### 기본 명령어
- 게임은 텍스트 명령어로 진행되지 않고, UI 버튼 클릭 및 아이템 선택으로 상호작용합니다 (프론트엔드 개발 완료 시).
- 현재 프로토타입 단계에서는 키워드 기반의 입력을 처리합니다.

### 주요 아이템
- **렌즈 계열**: 숨겨진 정보를 보거나 암호를 해독하는 데 사용.
- **도구 계열**: `드라이버`, `인두기`, `자석` 등 물리적 작업 수행.
- **키 아이템**: 엔딩을 결정짓는 `바이러스`, `백업 드라이브`, `관리자 키`.

## 🤝 기여 (Contributing)
이 프로젝트는 AI 에이전트 아키텍처 실험을 위해 제작되었습니다.
버그 제보 및 기능 제안은 이슈 트래커를 이용해 주세요.

## 📄 라이선스
MIT License
