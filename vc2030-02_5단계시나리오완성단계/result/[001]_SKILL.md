---
name: vc2030-02-vids-completion
description: "vc2030-01 스킬에서 생성된 5대 마스터 대본을 실제 영상으로 완성하는 6~10단계 Google Vids 편집 완성 파이프라인. (6)Google Vids 영상 배치 & 타임라인 연결 (7)AI TTS 나레이션 생성 (8)자막 가독성 디자인 (9)SFX & 돌발대사 합성 (10)MP4 렌더링 & 다운로드까지 비즈니스 실무 영상 제작의 완성 단계. Vrew, CapCut, AI Studio TTS 연동 가이드 포함. Google Vids 편집, TTS 나레이션 생성, 자막 삽입, SFX 합성, MP4 완성 요청 시 반드시 활성화할 것."
---

# 🎬 비즈니스 실무 AI 영상 — Google Vids 완성 파이프라인 (vc2030-02)

이 스킬은 **`vc2030-01` 스킬에서 생성된 5대 마스터 대본**을 실제 완성 MP4 영상으로 만드는 **6~10단계 Google Vids 편집 완성 프로토콜**입니다.

> **전제 조건**: `vc2030-01_5단계시나리오생성스킬`이 먼저 실행되어 5대 마스터 대본(이미지/영상/나레이션/자막/효과음 대본)이 준비된 상태여야 합니다.

---

## 🎯 6~10단계 완성 파이프라인 워크플로우

```
[5단계 완성 대본 준비]
        │
        ▼
[6단계] Google Vids — 영상 클립 배치 & 타임라인 연결
        │
        ▼
[7단계] AI TTS 나레이션 생성 (Track 3 → Google Vids Script 패널)
        │
        ▼
[8단계] 자막 생성 & 가독성 스타일링 (Track 4 → 하단 텍스트 박스)
        │
        ▼
[9단계] SFX 효과음 & 돌발 대사 합성 (Track 5 → 오디오 트랙)
        │
        ▼
[10단계] 최종 검토 & MP4 렌더링 / 다운로드
        │
        ▼
[완성] 최종 MP4 파일 → result/ 폴더 저장
```

---

## 📋 6~10단계 상세 실행 가이드

### [6단계] Google Vids — 영상 클립 배치 & 타임라인 연결

**실행 위치**: Google Vids (vids.google.com) → 새 동영상 만들기

1. **Google Flow / Runway / Luma에서 생성한 무성 비디오 클립** 1~N번을 Scene 순서대로 준비합니다.
2. 좌측 패널 `[업로드(Uploads)]`에서 비디오 클립을 모두 업로드합니다.
3. 메인 타임라인에 Scene 1부터 차례로 드래그 앤 드롭합니다.
4. **전환(Transition) 효과 설정**:
   - 일반 장면 전환 (협상·투어): 부드러운 `디졸브(Dissolve, 0.5초)`
   - 극적인 성공/계약 순간: 전환 효과 없음(`Cut/None`)
   - 타임랩스·이동 장면: `크로스 페이드(Cross-fade, 0.3초)`
5. 각 클립의 **길이를 나레이션 TTS 길이에 맞게** 조정합니다.

### [7단계] AI TTS 나레이션 생성

**실행 위치**: Google Vids `[대본(Script)]` 패널

1. 우측 상단 `[Script]` 메뉴를 활성화합니다.
2. `vc2030-01`에서 생성한 **Track 3 [나레이션용 대본]**을 각 Scene별 대본 칸에 복사합니다.
3. 음성 설정(Voice Settings):
   - 언어: **한국어 (Korean)**
   - 톤: **'전문 나레이터 / 따뜻한 스토리텔러 (Professional Narrator / Warm)'** 선택
4. `[Generate Voiceover]` 클릭 후 오디오 파형이 비디오 클립 길이와 맞는지 확인합니다.
5. 길이가 맞지 않는 경우: 비디오 클립 트림 또는 TTS 재생 속도 조절 (±10%)

> **대안 — AI Studio TTS** (더 정교한 음성):
> - studio.ai.google.com → TTS API 또는 Notebook LM
> - 생성된 WAV 파일을 Google Vids 오디오 트랙에 임포트

### [8단계] 자막 생성 & 가독성 스타일링

**실행 위치**: Google Vids `[텍스트(Text)]` 도구

1. 배경 가독성 확보:
   - `[Shape]`에서 직사각형을 선택, 하단에 배치
   - 배경색: 반투명 검정 (`#000000`, 투명도 60%) 또는 라운드 박스
2. **Track 4 [자막용 대본]** 문구를 텍스트 상자에 입력합니다.
3. **비즈니스 영상 권장 텍스트 서식**:
   - 폰트: `Noto Sans KR`, `Pretendard`, `나눔고딕` (깔끔한 고딕 계열)
   - 크기: 28~32pt (화면 중앙 하단 정렬)
   - 색상: 흰색(`#FFFFFF`) / 핵심 수치 강조: 골드(`#FFD700`)
   - 스타일: 텍스트 외곽선(Stroke) 2px Black 적용으로 가독성 확보

### [9단계] SFX 효과음 & 돌발 대사 합성

**실행 위치**: Google Vids `[오디오(Audio)]` 트랙

1. **돌발 대사(Character Voice Dialogue)**:
   - 각 인물의 짧은 대사는 별도 오디오 클립 또는 TTS로 제작 후 배치
2. **SFX 라이브러리 검색 키워드** (Track 5 기준):
   - 비즈니스 악수: `Business handshake`, `Meeting greeting`
   - 전시장 분위기: `Exhibition hall ambience`, `Trade fair crowd`
   - 계약 서명: `Pen writing on paper`, `Document shuffle`
   - 축하: `Champagne pop`, `Celebration applause`
   - 비행기/이동: `Airport ambience`, `City walking`
3. **BGM 배경음악**:
   - 장면 무드에 맞는 Corporate / Cinematic 음악 트랙 추가
   - **오디오 더킹(Audio Ducking)** 활성화: 나레이션 구간에 BGM 볼륨 20%로 자동 감쇄
4. **오디오 레벨 믹싱 권장**:
   - 나레이션 TTS: 100%
   - 돌발 대사: 80%
   - SFX: 60%
   - BGM: 20~30%

### [10단계] 최종 검토 & MP4 렌더링

**실행 위치**: Google Vids 상단 `[내보내기(Export)]`

1. **4중 싱크 최종 점검** (전체 프리뷰 재생):
   - ✅ 화면 (비디오 클립)
   - ✅ 나레이션 TTS
   - ✅ 자막
   - ✅ SFX & BGM
2. 상단 우측 `[공유 및 내보내기(Export)]` → `[동영상 다운로드(Download as MP4)]` 클릭
3. 해상도: **1080p (Full HD)** 선택 후 렌더링
4. 렌더링 완료 후:
   - Google Drive 자동 저장 확인
   - 로컬 PC `result/` 폴더에 최종 MP4 파일 저장
   - 파일명: `[001]_이안나대표_해외출장_마스터영상.mp4` (순차 번호 부여)

---

## 🛠️ 대안 툴 연동 안내 (Vrew · CapCut · Filmora)

| 단계 | Google Vids | Vrew | CapCut |
|------|-------------|------|--------|
| **나레이션** | Script 패널 TTS | 텍스트→비디오 자동 | AI 음성 생성 |
| **자막** | Text 도구 수동 입력 | 자동 자막 동기화 | 자막 템플릿 |
| **SFX** | Audio 라이브러리 | 효과음 추가 | 오디오 라이브러리 |
| **내보내기** | MP4 1080p | MP4 / MOV | MP4 / MP4 HD |

### Vrew 사용 시:
1. `[텍스트로 비디오 만들기]` → Track 3 나레이션 전체 붙여넣기
2. AI 목소리와 자막 자동 동기화 후, 비디오 클립을 Track 1/2 결과물로 교체
3. Track 5 SFX와 BGM 추가 후 내보내기

### CapCut 사용 시:
1. 타임라인에 비디오 클립 배치
2. Track 4 자막을 SRT 파일(`./scripts/extract_to_srt.py`)로 변환 후 임포트
3. 오디오 라이브러리에서 Track 5 SFX 키워드로 검색 후 매칭

---

## 📁 파일 참조 (100% 상대 경로)

- Google Vids 실전 가이드: `./workflows/03_google_vids_completion.md`
- SRT 자막 자동 변환 스크립트: `../vc2030-01_5단계시나리오생성스킬/scripts/extract_to_srt.py`
- 완성 결과물 저장: `./result/`
