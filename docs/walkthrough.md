# 디지털 감옥 (The Digital Prison) - 프로젝트 워크스루

## 1. 프로젝트 개요 (Project Overview)
멀티모달 AI 방탈출 게임 "디지털 감옥"의 기초 시스템을 구축했습니다.
사용자의 요구사항에 맞춰 4개의 전문 에이전트와 초기 시나리오, 그리고 HTML 기반의 UI 프로토타입을 구현했습니다.

## 2. 에이전트 구조 (Agent Architecture)
[design_document.md](file:///c:/Users/myjew/.gemini/antigravity/brain/40f98673-1aae-4582-b0d0-c4401dfb6926/design_document.md)에 상세 정의되어 있습니다:
- **시나리오 마스터:** 전체 스토리와 세계관 관리.
- **퍼즐 아키텍트:** RAG와 코딩 스킬을 활용한 퍼즐 생성.
- **비주얼 일러스트레이터:** DALL-E 3와 Vision을 활용한 이미지 생성/분석.
- **시스템 가이드:** HTML/CSS/JS로 게임 UI(Artifacts Manager) 렌더링.

## 3. 시나리오: 구역 0 (Sector 0)
첫 번째 방 "각성"의 배경 스토리는 [game_start.md](file:///c:/Users/myjew/.gemini/antigravity/brain/40f98673-1aae-4582-b0d0-c4401dfb6926/game_start.md)에서 확인할 수 있습니다.
- **설정:** 차가운 금속 큐브 방, 디지털 터미널.
- **퍼즐:** "글리치 키 (Glitch Key)" - 물리적 열쇠가 아닌 데이터로서의 열쇠를 스캔해야 함.

## 4. 게임 UI (System Guide)
시스템 가이드 에이전트가 생성하는 UI 프로토타입은 [game_ui.html](file:///c:/Users/myjew/.gemini/antigravity/brain/40f98673-1aae-4582-b0d0-c4401dfb6926/game_ui.html)입니다.
- 웹 브라우저에서 열어 사이버펑크 스타일의 인터페이스를 확인할 수 있습니다.

## 5. 게임 엔진 프로토타입 (Game Engine)
파이썬으로 구현된 텍스트 기반 게임 엔진 [game_engine.py](file:///c:/Users/myjew/.gemini/antigravity/brain/40f98673-1aae-4582-b0d0-c4401dfb6926/game_engine.py)를 통해 게임 로직을 테스트할 수 있습니다.

### 실행 방법
```bash
python game_engine.py
```

### 플레이 예시
```text
[시나리오 마스터]: 구역 0: 각성(Awakening) 초기화 중...
[비주얼 일러스트레이터]: '차가운 금속 큐브 방...' 장면 생성 중...
[시스템 가이드]: UI 업데이트 (초기 상태)
[시나리오 마스터]: 환영합니다...

> 조사
[시나리오 마스터]: 당신은 차가운 금속 벽... 글리치된 열쇠 사진을 봅니다.

> 사진 스캔
[시스템 가이드]: 터미널 해킹 프로토콜 시작...
신호 동기화 진행 중... 1/3
...
[시나리오 마스터]: 인증 완료. 구역 0 탈출 성공.
```
