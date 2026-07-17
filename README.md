# Edusync

교육 신청 데이터를 기반으로 업무용 Excel 파일 생성을 자동화하기 위한 Python 기반 프로젝트입니다.

---

## 1. Project Overview

Edusync는 웹사이트에서 다운로드한 교육 신청 데이터를 자동으로 처리하여 반복적인 문서 작성 업무를 줄이는 것을 목표로 하는 프로젝트입니다.

현재 업무 과정에서는 신청자 정보를 확인하고 여러 Excel 양식에 직접 입력하는 작업이 필요합니다.

본 프로젝트의 목표는 다음과 같습니다.

```
웹사이트 데이터 수집
        ↓
신청 데이터 분석 및 정제
        ↓
업무용 데이터 변환
        ↓
Excel 문서 자동 생성
```

최종적으로 사용자는 최소한의 입력만으로 필요한 업무 문서를 생성할 수 있도록 하는 것을 목표로 합니다.

---

## 2. Development Environment

- Python 3.x
- Visual Studio Code
- Git / GitHub
- Python Virtual Environment (`venv`)

---

## 3. Dependencies

현재 사용 중인 주요 라이브러리:

| Package | Purpose |
| --- | --- |
| pandas | 데이터 처리 및 분석 |
| lxml | HTML 데이터 분석 |
| xlrd | Excel 파일 처리 지원 |

설치 방법:

```bash
pip install -r requirements.txt
```

---

## 4. Project Structure

현재 프로젝트 구조:

    Edusync
    │
    ├── main.py
    ├── requirements.txt
    ├── .gitignore
    └── README.md

---

## 5. Current Version

## Version 0.2 - Source Data Import

현재 구현 완료된 기능:

- [x] Python 프로젝트 생성
- [x] 가상환경 구성
- [x] GitHub Repository 연결
- [x] 교육 신청 리스트 파일 분석
- [x] HTML 기반 `.xls` 파일 구조 확인
- [x] pandas DataFrame 변환

---

## 6. Source Data Format

웹사이트에서 다운로드한 신청 리스트 파일은 `.xls` 확장자를 가지고 있지만, 실제 Excel Binary 파일이 아닌 HTML 기반 테이블 데이터입니다.

따라서 일반적인 Excel 읽기 방식인 `read_excel()` 대신 HTML Parser 방식을 사용하여 데이터를 불러옵니다.

```python
pd.read_html()
```

변환 과정:

```
웹사이트 다운로드 파일
        ↓
HTML Table 데이터
        ↓
pandas DataFrame 변환
```

이를 통해 신청 데이터를 Python 환경에서 처리할 수 있는 형태로 변환했습니다.
---

# 7. Development Roadmap

## Version 0.1 - Project Setup

목표:

프로젝트 개발 환경 구축

구현:

- Python 프로젝트 생성
- 가상환경 구성
- GitHub 연결

Status:

Completed

---

## Version 0.2 - Source Data Import

목표:

웹사이트에서 다운로드한 신청 데이터를 Python에서 활용 가능한 형태로 변환

구현:

- HTML 기반 `.xls` 파일 분석
- 데이터 인코딩 확인
- pandas DataFrame 변환

Status:

Completed

---

## Version 0.3 - Data Cleaning & Standardization

목표:

원본 데이터를 프로그램 내부에서 사용할 표준 데이터 형태로 변환

예정 기능:

- 컬럼명 정리
- 이름 정렬
- 빈 데이터 처리
- 중복 데이터 제거
- 데이터 형식 통일

Status:

Planned

---

## Version 0.4 - Data Processing Logic

목표:

업무에 필요한 데이터 처리 기능 구현

예정 기능:

- 교육별 인원 계산
- 조건별 검색
- 신청자 데이터 분석
- 입금 여부 관리

Status:

Planned

---

## Version 0.5 - Excel Template Generator

목표:

기존 업무용 Excel 양식 자동 생성

예정 기능:

- 입교명단 생성
- 출석부 생성
- 입금확인 파일 생성
- 점수관리 파일 생성

Status:

Planned

---

## Version 0.6 - Template Management

목표:

다양한 기존 Excel 양식 지원

예정 기능:

- 템플릿 관리
- 양식별 자동 입력
- 여러 교육 과정 대응

Status:

Planned

---

## Version 0.7 - Web Automation

목표:

웹사이트 데이터 다운로드 과정 자동화

예정 기능:

- Playwright 기반 웹 접근
- 로그인 자동화
- 파일 다운로드 자동화

Status:

Planned

---

## Version 0.8 - GUI Application

목표:

비개발자도 사용할 수 있는 프로그램 형태 제공

예정 기능:

- 파일 선택 기능
- 실행 버튼 제공
- 결과 파일 관리

Status:

Planned

---

## Version 0.9 - Production Release

목표:

실제 업무 환경에서 사용할 수 있는 프로그램 완성

예정 기능:

- 오류 처리
- 사용자 환경 설정
- 실행 파일 배포

Status:

Planned

---

## 8. Future Goal

최종 목표:

```
웹사이트
    ↓
신청 데이터 자동 다운로드
    ↓
데이터 정제 및 분석
    ↓
업무용 Excel 자동 생성
    ↓
반복 업무 최소화
```

---

## 9. Version Control

본 프로젝트는 Git을 이용하여 버전을 관리합니다.

주요 Git 작업:

```bash
git add .
git commit -m "commit message"
git push
```

관리 제외 파일:

- Python 가상환경 (`venv/`)
- Python 캐시 파일 (`__pycache__/`)
- 개인정보가 포함된 원본 데이터 파일

---

## Author

gg-biny