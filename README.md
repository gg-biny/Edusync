# Edusync

교육 신청 리스트 데이터를 자동으로 처리하고 관리하기 위한 Python 기반 데이터 처리 프로젝트입니다.

---

## 1. Project Overview

Edusync는 교육 신청 데이터를 효율적으로 관리하고 분석하기 위한 자동화 프로젝트입니다.

현재 수작업으로 확인하고 처리하는 교육 신청 리스트 데이터를 Python으로 불러와 데이터 정제, 검색, 분석 및 결과 생성이 가능한 형태로 발전시키는 것을 목표로 합니다.

현재 단계에서는 데이터 처리 환경을 구축하고, 원본 데이터 파일의 구조를 분석하여 Python에서 활용 가능한 형태로 변환하는 작업을 진행하고 있습니다.

---

## 2. Development Environment

- Python 3.x
- Visual Studio Code
- Git / GitHub
- Python Virtual Environment (`venv`)

---

## 3. Dependencies

현재 프로젝트에서 사용하는 주요 라이브러리입니다.

| Package | Purpose |
| --- | --- |
| pandas | 데이터 처리 및 DataFrame 분석 |
| lxml | HTML 기반 데이터 분석 |
| xlrd | Excel 파일 처리 지원 |

패키지 설치:

```bash
pip install -r requirements.txt
```

---

## 4. Project Structure

현재 프로젝트 구조:

    Edusync
    │
    ├── main.py                 # 데이터 처리 실행 코드
    ├── requirements.txt        # Python 패키지 목록
    ├── .gitignore              # Git 관리 제외 파일 설정
    └── README.md               # 프로젝트 설명 문서

※ Python 가상환경(`venv`) 및 원본 데이터 파일은 Git 관리 대상에서 제외합니다.

---

## 5. Current Progress

현재까지 진행된 작업입니다.

### Development Environment

- [x] Python 설치 및 개발 환경 구성
- [x] VS Code 기반 프로젝트 생성
- [x] Python 가상환경(`venv`) 구성
- [x] 프로젝트 의존성 관리 환경 구축

### Data Processing

- [x] 교육 신청 리스트 파일 구조 확인
- [x] `.xls` 파일 내부 구조 분석
- [x] HTML 기반 테이블 데이터 확인
- [x] pandas DataFrame 변환 성공
- [x] UTF-8 인코딩 문제 해결

### Version Control

- [x] Git 설치 및 초기 설정
- [x] Git Repository 생성
- [x] GitHub Repository 연결
- [x] 프로젝트 버전 관리 적용

---

## 6. Data Processing Issue

초기에는 `.xls` 파일을 Excel 파일로 판단하여 pandas의 `read_excel()` 함수를 사용했습니다.

```python
pd.read_excel()
```

하지만 다음 오류가 발생했습니다.

```
ValueError:
Excel file format cannot be determined, you must specify an engine manually
```

파일 내부 구조를 확인한 결과, 해당 파일은 실제 Excel Binary 파일이 아니라 HTML 기반 테이블 데이터였습니다.

따라서 Excel Reader 방식이 아닌 HTML Table Parser 방식을 사용하여 데이터를 처리했습니다.

변경 방식:

```python
pd.read_html()
```

이를 통해 HTML 테이블 데이터를 pandas DataFrame 형태로 변환할 수 있었습니다.

---

## 7. Current Implementation

현재 구현된 기능:

- 웹 기반 교육 신청 리스트 파일 읽기
- HTML 테이블 데이터 분석
- pandas DataFrame 변환
- 데이터 출력 및 구조 확인
- Python 기반 데이터 처리 환경 구축

---

## 8. Future Development

향후 다음 기능을 단계적으로 추가할 예정입니다.

### Data Processing

- 신청자 데이터 정제
- 불필요한 데이터 제거
- 중복 데이터 처리
- 데이터 형식 통일

### Analysis Features

- 교육별 신청 인원 분석
- 조건별 신청자 검색
- 통계 데이터 생성

### Automation

- 결과 파일 자동 생성
- 반복 업무 자동화
- 데이터 처리 과정 자동화

---

## 9. Version Control

본 프로젝트는 Git을 이용하여 버전을 관리합니다.

주요 작업:

```bash
git add .
git commit -m "commit message"
git push
```

관리 제외 파일:

- Python 가상환경 (`venv/`)
- Python 캐시 파일 (`__pycache__/`)
- 개인정보가 포함될 수 있는 원본 데이터 파일

---

## Author

gg-biny