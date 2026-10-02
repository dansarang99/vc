# 🎬 Google Vids 6~10단계 실전 영상 편집 & 완성 가이드

이 문서는 `vc2030-01`에서 생성된 5대 마스터 대본을 **Google Vids에서 실제 영상으로 완성**하는 상세 실무 가이드입니다.

---

## ■ [6단계] 영상 클립 배치 & 타임라인 연결

1. **준비물 확인**:
   - Google Flow / Runway / Luma에서 생성한 무성 비디오 클립 (Scene 1~8)
   - `vc2030-01` 스킬에서 생성된 5대 마스터 대본 파일

2. **Google Vids 접속**: vids.google.com → `새 동영상 만들기` 클릭

3. **클립 업로드 & 배치**:
   ```
   Scene 1 클립 → Scene 2 클립 → ... → Scene 8 클립
   (좌측 [업로드] 패널 → 메인 타임라인 드래그 앤 드롭)
   ```

4. **비즈니스 영상 전환 효과 추천**:
   - 오프닝~중반부: `Dissolve 0.5초` (자연스러운 전환)
   - 계약 체결 순간: `Cut (전환 없음)` (임팩트 강조)
   - 엔딩 크레딧: `Fade to Black 1.0초`

---

## ■ [7단계] AI TTS 나레이션 생성

### Google Vids TTS 사용법:
```
우측 상단 [Script] → 각 Scene별 Track 3 대본 입력
→ [Voice Settings] → 한국어(Korean) → 'Professional Narrator' 선택
→ [Generate Voiceover] → 오디오 파형 확인
```

### AI Studio TTS 대안 (더 정교한 음성):
```
studio.ai.google.com → Text-to-Speech
→ 언어: 한국어 → 음성: ko-KR-Neural2-C (여성) 또는 ko-KR-Neural2-B (남성)
→ 속도: 1.0 (기본) / 감정 강조 구간: 0.95
→ WAV 파일로 저장 → Google Vids 오디오 트랙에 임포트
```

### 비즈니스 나레이션 톤 가이드:
| 장면 유형 | 권장 TTS 설정 |
|-----------|---------------|
| 오프닝 (인물 소개) | Warm, Medium pace |
| 협상 장면 | Serious, Slightly slower |
| 클라이맥스 (성공 순간) | Excited, Slightly faster |
| 엔딩 (교훈/비전) | Warm, Slow, Emotional |

---

## ■ [8단계] 자막 생성 & 가독성 스타일링

### 자막 배치 순서:
```
[텍스트(Text)] → 직사각형 배경 박스 추가 (하단 1/6 영역)
→ 배경: #000000 투명도 60% → 자막 텍스트 입력
→ 폰트: Noto Sans KR Bold → 크기: 30pt → 색상: #FFFFFF
```

### 비즈니스 강조 자막 스타일:
- **수치 강조**: 수출액·달성 목표 등 숫자에 `#FFD700 (골드)` 적용
- **핵심 키워드**: 인물명·브랜드명에 굵기(Bold) 강조
- **이모지 자막**: 🎉 같은 이모지를 자막 시작 또는 끝에 배치하여 시각적 임팩트 부여

---

## ■ [9단계] SFX & 돌발대사 합성

### 비즈니스 SFX 배치 큐시트:

| 장면 | SFX 검색 키워드 | 배치 타이밍 |
|------|----------------|-------------|
| Scene 1 (첫 만남) | `Business card exchange`, `Exhibition ambience` | 명함 교환 순간 |
| Scene 2 (포트폴리오) | `Tablet swipe`, `Office ambience` | 화면 스와이프 시 |
| Scene 4 (협상) | `Pen clicking`, `Document shuffle`, `Hotel ambience` | 대화 중 |
| Scene 5 (라이브) | `Conference applause`, `Microphone tap` | 발표 시작/끝 |
| Scene 8 (계약) | `Champagne pop`, `Triumphant applause`, `Pen signing` | 축하 순간 |

### 오디오 더킹(Audio Ducking) 설정:
```
BGM 트랙 선택 → [오디오 더킹] 활성화
→ 나레이션 구간: BGM 볼륨 자동 20% 감쇄
→ 효과: 나레이션이 명확하게 들리는 전문적 사운드 믹싱
```

---

## ■ [10단계] 최종 검토 & MP4 내보내기

### 4중 싱크 체크리스트:
- [ ] 비디오 클립 — 나레이션 TTS 길이 일치 확인
- [ ] 자막 — 나레이션과 2~3초 이내 동기화
- [ ] SFX — 비디오 해당 장면과 타이밍 일치
- [ ] BGM — 더킹이 제대로 작동하는지 확인

### 내보내기 설정:
```
상단 우측 [공유 및 내보내기] → [동영상 다운로드]
→ 해상도: 1080p Full HD
→ 파일명: [001]_프로젝트명_완성.mp4
→ 저장 위치: ./result/ 폴더
```

### 최종 파일 명명 규칙:
```
[001]_이안나대표_해외출장_마스터영상.mp4
[002]_이안나대표_해외출장_쇼츠버전.mp4  ← 9:16 세로 편집 버전 (선택)
```

---

## 📋 완성 후 배포 채널별 최적화

| 채널 | 포맷 | 해상도 | 러닝타임 | 자막 |
|------|------|--------|----------|------|
| YouTube 롱폼 | MP4 16:9 | 1080p | 2~3분 | SRT 별도 업로드 |
| YouTube Shorts | MP4 9:16 | 1080p | 60초 이하 | 번인 자막 |
| Instagram Reels | MP4 9:16 | 1080p | 90초 이하 | 번인 자막 |
| LinkedIn | MP4 16:9 | 720p~1080p | 1~3분 | 번인 자막 |
| 카카오 채널 | MP4 | 720p | 1~2분 | 번인 자막 |
