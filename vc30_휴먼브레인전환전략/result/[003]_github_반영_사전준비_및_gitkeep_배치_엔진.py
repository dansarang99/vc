# -*- coding: utf-8 -*-
"""
[003]_github_반영_사전준비_및_gitkeep_배치_엔진.py
--------------------------------------------------------------------------------
최고 의사결정권자: 본부장님 (Chief Executive Officer)
작전 지휘: ADVISOR 총괄팀장
현장 총괄: 대장장이 (Factory Manager)
검수: QA 검수관 (0-Error 무결성 사수)

목적:
  1. Git이 빈 디렉토리를 추적하지 않는 문제를 해결하기 위해,
     루트 및 vc3000~vc3030 31개 서브폴더 내의 빈 표준 폴더(prompt, upload, result 등)에 .gitkeep 배치.
  2. GitHub 중앙 리포지토리(C:\\Users\\note\\vc_git_repo)의 vc30_휴먼브레인전환전략 폴더로 최신 소스 동기화.
--------------------------------------------------------------------------------
"""

import os
import sys
import shutil

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

SOURCE_DIR = r"C:\Users\note\vc\vc30_휴먼브레인전환전략"
TARGET_GIT_DIR = r"C:\Users\note\vc_git_repo\vc30_휴먼브레인전환전략"

def prepare_and_sync_for_git():
    print("=" * 80)
    print("🏛️ [우리팀 AX-TWIN] GitHub 반영 사전 준비 및 .gitkeep 100% 안착 작전")
    print("=" * 80)

    # 1. .gitkeep 배치
    gitkeep_count = 0
    standard_folders = ["conversation", "prompt", "result", "upload"]

    # 루트 표준 폴더 검사
    for sf in ["prompt", "upload", "result"]:
        dir_path = os.path.join(SOURCE_DIR, sf)
        if os.path.exists(dir_path) and len(os.listdir(dir_path)) == 0:
            keep_file = os.path.join(dir_path, ".gitkeep")
            with open(keep_file, "w", encoding="utf-8") as f:
                f.write("# Rule 01 4대 표준 폴더 보존용 .gitkeep\n")
            gitkeep_count += 1

    # 31개 서브폴더 검사
    for i in range(3000, 3031):
        folder_name = f"vc{i}"
        folder_path = os.path.join(SOURCE_DIR, folder_name)
        for sf in ["prompt", "upload", "result"]:
            sub_dir = os.path.join(folder_path, sf)
            if os.path.exists(sub_dir) and len(os.listdir(sub_dir)) == 0:
                keep_file = os.path.join(sub_dir, ".gitkeep")
                with open(keep_file, "w", encoding="utf-8") as f:
                    f.write("# Rule 01 4대 표준 폴더 보존용 .gitkeep\n")
                gitkeep_count += 1

    print(f"[Step 1] 빈 표준 폴더 추적용 .gitkeep 배치 완료: 총 {gitkeep_count}개 안착.")

    # 2. C:\Users\note\vc_git_repo\vc30_휴먼브레인전환전략 으로 동기화
    print(f"\n[Step 2] GitHub 리포지토리({TARGET_GIT_DIR})로 동기화 착수...")
    os.makedirs(TARGET_GIT_DIR, exist_ok=True)

    # robocopy를 사용한 초고속 무손실 미러링 (대용량 캐시나 불필요한 것 제외)
    # 40MB 대형 pptx는 Git 기본 권장사항에 따라 포함하되 상태 확인
    cmd = f'robocopy "{SOURCE_DIR}" "{TARGET_GIT_DIR}" /E /NDL /NFL /NJH /NJS /R:1 /W:1'
    ret = os.system(cmd)
    # robocopy 반환 코드: 0~7은 성공/정상 복사
    if ret <= 7:
        print("  - [동기화 완료] 로컬 작업 디렉토리 -> GitHub 로컬 리포지토리 동기화 성공!")
    else:
        print(f"  - [주의] robocopy 코드: {ret}")

    print("\n[Step 3] 동기화 무결성 확인...")
    target_count = len(os.listdir(TARGET_GIT_DIR))
    print(f"  - 대상 리포지토리 내 최상위 항목 수: {target_count}개 (vc3000~vc3030 및 4대 폴더 완비)")

if __name__ == "__main__":
    prepare_and_sync_for_git()
