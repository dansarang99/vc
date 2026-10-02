# 🎨 5대 마스터 대본 작성 공식 & 비즈니스 프롬프트 가이드

각 AI 생성 도구(Google Flow, Midjourney, Flux, Imagen 3, Runway, Luma, Google Vids 등)의 특성에 맞춘 비즈니스 실무 최적화 프롬프트 작성 공식입니다.

---

## 1. 이미지 생성 프롬프트 공식 (비즈니스 실사 스타일)

```text
[스타일 키워드] + [고정 캐릭터 앵커 Visual DNA] + [동작 및 자세] + [환경 및 소품] + [조명 및 분위기] + [카메라 렌즈 및 구도] + [파라미터]
```

### 실사 스타일 필수 키워드:
- **스타일**: `Photo-realistic cinematic shot`, `Professional corporate photography`, `Documentary style`
- **조명**: `Soft corporate studio lighting`, `Cinematic window light`, `Golden hour exterior lighting`
- **화질/해상도**: `8k resolution`, `Sharp focus`, `DSLR quality`
- **비율**: `--ar 16:9` (유튜브 롱폼), `--ar 9:16` (쇼츠/릴스)

### 3D 스타일 필수 키워드:
- **스타일**: `3D animation render`, `Pixar & Disney style`, `Unreal Engine 5`
- **조명**: `Cinematic volumetric lighting`, `Soft key light`
- **화질**: `8k resolution`, `Octane render`, `Raytracing`

---

## 2. 비디오 모션 프롬프트 공식 (Runway Gen-3, Luma, Kling, Veo 2)

```text
[카메라 무브먼트] + [피사체 주요 모션] + [배경 환경 요소의 움직임] + [빛 & 셔터 템포]
```

### 비즈니스 씬용 카메라 무브먼트 키워드:
- **의전·회의**: `Slow smooth dolly in towards confident executive's face`
- **악수·서명**: `Medium shot rack focus from handshake to both executives smiling`
- **투어·이동**: `Tracking shot following CEO through modern exhibition hall`
- **연설·발표**: `Wide establishing shot slowly pushing in on presenter at podium`
- **감동 클로즈업**: `Extreme close-up slow motion on the moment of agreement`

---

## 3. TTS / 나레이션 대본 작성 팁 (Google Vids, Vrew)

- **호흡 조절**: 쉼표(`,`)를 적극적으로 사용하여 인공지능 성우의 어색한 연속 발음을 방지합니다.
- **문장 길이**: 한 문장이 너무 길어지지 않도록 15~25음절 내외로 간결하게 끊어줍니다.
- **감정 지시문**: Google Vids TTS에서는 `Professional Narrator` 또는 `Warm Storyteller` 톤을 선택합니다.
- **비즈니스 어조**: 과장되지 않고, 신뢰감 있는 전문적 어조를 유지합니다.

---

## 4. 자막(Captions) 작성 규칙 (Vrew, CapCut)

- **줄바꿈 규칙**: 1회 표시당 최대 2줄, 한 줄당 최대 18~20자 이내.
- **핵심 키워드 강조**: 수치(10억 달성!), 감탄어(마침내, 역사적 순간 등)에 굵은 텍스트 또는 색상 강조.
- **가독성 확보**: 비즈니스 배경이 복잡할 경우 반투명 배경 바 또는 텍스트 외곽선(Stroke) 적용.

---

## 5. 비즈니스 사운드 디자인(SFX & BGM) 큐시트

- **돌발 대사 가이드라인**: 비즈니스 현장의 자연스러운 대사 (너무 연출된 느낌 방지)
- **SFX 영문 검색 키워드**:
  - 명함 교환: `Business card exchange sound`
  - 박수·환호: `Corporate applause`, `Conference room clapping`
  - 계약 서명: `Pen signing on paper`, `Stamp sound`
  - 샴페인: `Champagne pop`, `Celebration toast`
  - 비행기/공항: `Airport ambience`, `Airplane takeoff`
  - 도심: `City ambience`, `Modern office sound`
- **BGM 무드 설정**:
  - 힘차고 자신감 있는 오프닝: `Corporate motivational, Uplifting orchestra, BPM 110`
  - 진지한 협상: `Tension corporate, Minimalist piano, BPM 90`
  - 결정적 순간: `Epic cinematic build-up, Orchestral swell, BPM 100`
  - 성공·축하 엔딩: `Triumphant brass fanfare, Warm strings, BPM 120`
