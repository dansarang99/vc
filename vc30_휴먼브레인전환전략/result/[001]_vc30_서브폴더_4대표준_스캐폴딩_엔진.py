# -*- coding: utf-8 -*-
"""
[001]_vc30_서브폴더_4대표준_스캐폴딩_엔진.py
--------------------------------------------------------------------------------
최고 의사결정권자: 본부장님 (USER / Chief Executive Officer)
작전 지휘: ADVISOR 총괄팀장
현장 총괄: 대장장이 (Factory Manager)
검수: QA 검수관 (0-Error 무결성 사수)

목적:
  C:\\Users\\note\\vc\\vc30_휴먼브레인전환전략 내에
  vc3000 ~ vc3030 (총 31개) 서브폴더를 자동 생성하고,
  각 서브폴더에 Rule 01 (4대 표준 폴더: conversation, prompt, result, upload) 및
  CONVERSATION_TOTAL.md, rule_01_file-folder.md를 무결점으로 스캐폴딩한다.
--------------------------------------------------------------------------------
"""

import os
import sys
import shutil
import datetime

# Windows 콘솔 utf-8 출력 보장
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

BASE_DIR = r"C:\Users\note\vc\vc30_휴먼브레인전환전략"
RULE_SOURCE = r"C:\Users\note\.gemini\rules\rule_01_file-folder.md"

STANDARD_FOLDERS = ["conversation", "prompt", "result", "upload"]

def scaffold_vc30():
    print("=" * 80)
    print("🏛️ [우리팀 AX-TWIN] vc30* 서브폴더 (vc3000~vc3030) Rule 01 스캐폴딩 가동")
    print("=" * 80)
    
    # 0. Rule 01 원천 내용 읽기
    with open(RULE_SOURCE, "r", encoding="utf-8") as f:
        rule_content = f.read()

    # 1. 루트 폴더 Rule 01 적용
    print("\n[Step 1] 루트 디렉토리(vc30_휴먼브레인전환전략) Rule 01 정비...")
    for sf in STANDARD_FOLDERS:
        sf_path = os.path.join(BASE_DIR, sf)
        os.makedirs(sf_path, exist_ok=True)
    
    root_conv_total = os.path.join(BASE_DIR, "conversation", "CONVERSATION_TOTAL.md")
    if not os.path.exists(root_conv_total):
        now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(root_conv_total, "w", encoding="utf-8") as f:
            f.write(f"""# 📜 [vc30_휴먼브레인전환전략] 단일 마스터 실록 (CONVERSATION_TOTAL.md)

> **최고 의사결정권자**: 본부장님  
> **총괄 작전 지휘관**: ADVISOR 총괄팀장  
> **현장 공장장**: 대장장이  
> **개설 일시**: {now_str}  
> **적용 규약**: Rule 01 (4대 표준 폴더 및 result [001]~[999] 결과물 단일화 절대 헌장)  

---

## 🏛️ 세션 기록
- **{now_str}**: vc3000~vc3030 31개 서브폴더 및 Rule 01 4대 표준 폴더 일괄 스캐폴딩 착수.
""")
        print(f"  - [생성] 루트 단일 실록: {root_conv_total}")

    # 비표준 빈 image 폴더 정리
    empty_image_dir = os.path.join(BASE_DIR, "image")
    if os.path.exists(empty_image_dir) and len(os.listdir(empty_image_dir)) == 0:
        os.rmdir(empty_image_dir)
        print("  - [정리] Rule 01 위배 빈 임의 폴더(image/) 소거 완료.")

    # 루트 rule01 동기화
    root_rule_target = os.path.join(BASE_DIR, "rule01_file-folder.md")
    with open(root_rule_target, "w", encoding="utf-8") as f:
        f.write(rule_content)
    print("  - [동기화] 최신 Rule 01 헌장 루트 동기화 완료.")

    # 2. vc3000 ~ vc3030 생성 및 스캐폴딩
    print("\n[Step 2] vc3000 ~ vc3030 (총 31개) 서브폴더 스캐폴딩 시작...")
    created_folders = []
    
    for i in range(3000, 3031):
        folder_name = f"vc{i}"
        folder_path = os.path.join(BASE_DIR, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        
        # 4대 표준 폴더 생성
        for sf in STANDARD_FOLDERS:
            os.makedirs(os.path.join(folder_path, sf), exist_ok=True)
            
        # conversation/CONVERSATION_TOTAL.md 생성
        conv_total_path = os.path.join(folder_path, "conversation", "CONVERSATION_TOTAL.md")
        if not os.path.exists(conv_total_path):
            now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(conv_total_path, "w", encoding="utf-8") as f:
                f.write(f"""# 📜 [{folder_name}] 단일 마스터 실록 (CONVERSATION_TOTAL.md)

> **최고 의사결정권자**: 본부장님 (Chief Executive Officer)  
> **총괄 작전 지휘관**: ADVISOR 총괄팀장 (MAIN AI)  
> **현장 공장장**: 대장장이 (Factory Manager)  
> **개설 일시**: {now_str}  
> **적용 규약**: Rule 01 (4대 표준 폴더 및 result [001]~[999] 결과물 단일화 절대 헌장)  

---

## 🏛️ 기본 운영 방침
1. **conversation/**: 본 단일 마스터 실록을 통해 모든 대화 및 세션 이력을 꼬리물기로 영구 누적한다.
2. **prompt/**: 원천 프롬프트 및 시스템 지침을 독립 보존한다.
3. **result/**: 모든 결과물은 [001]~[999] 순차 시리얼 번호를 부여하여 유일하게 보존한다.
4. **upload/**: 외부 원천 소스 및 참고 자료를 저장한다.

---

## 📌 세션 히스토리
- **{now_str}**: `{folder_name}` 서브폴더 개설 및 4대 표준 폴더 스캐폴딩 완료. `result/[001]` 대기 정렬.
""")

        # 서브폴더 내 rule01_file-folder.md 배치
        sub_rule_path = os.path.join(folder_path, "rule01_file-folder.md")
        with open(sub_rule_path, "w", encoding="utf-8") as f:
            f.write(rule_content)

        created_folders.append(folder_name)

    print(f"  - 총 {len(created_folders)}개 서브폴더 (vc3000 ~ vc3030) 스캐폴딩 완료.")

    # 3. QA 무결성 전수 검증
    print("\n[Step 3] 🛡️ [QA 검수관] 0-Error 전수 무결성 정밀 검증...")
    error_count = 0
    total_subdirs_checked = 0
    
    for i in range(3000, 3031):
        folder_name = f"vc{i}"
        folder_path = os.path.join(BASE_DIR, folder_name)
        
        if not os.path.isdir(folder_path):
            print(f"  [ERROR] 폴더 부재: {folder_name}")
            error_count += 1
            continue
            
        for sf in STANDARD_FOLDERS:
            sub_core = os.path.join(folder_path, sf)
            if not os.path.isdir(sub_core):
                print(f"  [ERROR] {folder_name} 내 {sf}/ 폴더 부재")
                error_count += 1
            total_subdirs_checked += 1
            
        conv_file = os.path.join(folder_path, "conversation", "CONVERSATION_TOTAL.md")
        if not os.path.isfile(conv_file) or os.path.getsize(conv_file) == 0:
            print(f"  [ERROR] {folder_name} CONVERSATION_TOTAL.md 파일 이상")
            error_count += 1
            
        rule_file = os.path.join(folder_path, "rule01_file-folder.md")
        if not os.path.isfile(rule_file) or os.path.getsize(rule_file) == 0:
            print(f"  [ERROR] {folder_name} rule01_file-folder.md 파일 이상")
            error_count += 1

    print(f"  - 검증 대상 코어 폴더 수: {total_subdirs_checked}개 (31개 서브폴더 × 4대 폴더)")
    print(f"  - 검출된 에러 건수: {error_count}건")
    
    if error_count == 0:
        print("\n🎉 [QA 무결성 판정: 100% PASS] 0-Error 전수 검증 통과!")
    else:
        print(f"\n❌ [QA 무결성 판정: FAIL] {error_count}건 이상 발생!")
        
    return error_count == 0

if __name__ == "__main__":
    success = scaffold_vc30()
    if not success:
        exit(1)
