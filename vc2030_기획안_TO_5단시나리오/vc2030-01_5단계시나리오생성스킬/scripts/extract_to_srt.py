"""
extract_to_srt.py — Track 4 자막 자동 SRT 변환기 (vc2030-01 전용)

사용법:
  python scripts/extract_to_srt.py                              # 기본 예시 변환
  python scripts/extract_to_srt.py [대본파일경로.md] [출력.srt]  # 직접 지정

출력: ./result/subtitles.srt
"""

import re
import sys
from pathlib import Path

def extract_captions(md_text: str) -> list[str]:
    """마크다운 대본에서 Track 4 [자막용 대본] 항목만 추출합니다."""
    captions = []
    # '자막용' 키워드 이후 줄에서 > "..." 또는   > "..." 패턴 추출
    pattern = re.compile(
        r'\[자막용[^\]]*\][^\n]*\n\s*>\s*"?(.+?)"?\s*$',
        re.MULTILINE
    )
    for match in pattern.finditer(md_text):
        caption_text = match.group(1).strip().strip('"').strip()
        # 빈 문자열 및 마크다운 구조 문자 제외
        if caption_text and not caption_text.startswith('[') and len(caption_text) > 2:
            captions.append(caption_text)
    return captions


def generate_srt(captions: list[str], scene_duration_sec: int = 20) -> str:
    """자막 목록을 SRT 형식으로 변환합니다."""
    lines = []
    for i, caption in enumerate(captions, start=1):
        start_sec = (i - 1) * scene_duration_sec
        end_sec = i * scene_duration_sec - 1
        
        start_ts = f"{start_sec // 3600:02d}:{(start_sec % 3600) // 60:02d}:{start_sec % 60:02d},000"
        end_ts = f"{end_sec // 3600:02d}:{(end_sec % 3600) // 60:02d}:{end_sec % 60:02d},000"
        
        lines.append(str(i))
        lines.append(f"{start_ts} --> {end_ts}")
        lines.append(caption)
        lines.append("")
    
    return "\n".join(lines)


def main():
    # 입력 파일 경로 결정
    if len(sys.argv) >= 2:
        input_path = Path(sys.argv[1])
    else:
        # 기본값: examples 폴더의 이안나대표 예시 파일
        input_path = Path(__file__).parent.parent / "examples" / "이안나대표_해외출장_마스터.md"
    
    # 출력 파일 경로 결정
    if len(sys.argv) >= 3:
        output_path = Path(sys.argv[2])
    else:
        output_path = Path(__file__).parent.parent / "result" / "subtitles.srt"
    
    if not input_path.exists():
        print(f"[오류] 입력 파일을 찾을 수 없습니다: {input_path}")
        sys.exit(1)
    
    # 파일 읽기
    md_text = input_path.read_text(encoding="utf-8")
    
    # 자막 추출
    captions = extract_captions(md_text)
    if not captions:
        print("[경고] 자막(Track 4) 항목을 찾지 못했습니다. 마크다운 형식을 확인해 주세요.")
        sys.exit(1)
    
    # SRT 생성
    srt_content = generate_srt(captions)
    
    # 출력 디렉토리 생성
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(srt_content, encoding="utf-8")
    
    print(f"[완료] 변환 성공! 총 {len(captions)}개 자막 -> {output_path}")


if __name__ == "__main__":
    main()
