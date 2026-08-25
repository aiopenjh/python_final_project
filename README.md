# 📚 파이썬 도서 관리 시스템 (CLI Library Management System)

> `uv` 기반 가상환경 및 모듈화 설계를 적용한 대화형 콘솔 도서 관리 프로그램입니다.

---

## 📌 1. 프로젝트 개요
* 프로젝트명: 파이썬 대화형 도서 관리 프로그램
* 개발 환경: Python 3.13.x, `uv` 패키지 매니저
* 주요 목적: 파이썬 기본 문법(자료구조, 제어문, 예외 처리) 및 객체지향/모듈화 설계를 바탕으로 도서 등록, 검색, 대여/반납 로직을 구현합니다.

---

## 🛠️ 2. 주요 기능
1. 도서 등록 (Register)
   - 신규 도서의 제목 및 정보를 입력받아 저장소에 등록
2. 전체 도서 조회 (List)
   - 현재 등록된 모든 도서의 목록 및 대여 상태(대여 가능 / 대여 중) 출력
3. 도서 검색 (Search)
   - 특정 키워드(도서명 등)를 기반으로 일치하는 도서 정보 탐색
4. 대여 및 반납 처리 (Rent / Return)
   - 등록 도서의 대여 상태(`is_borrowed`) 플래그 전환 및 예외 상태 안내
5. 프로그램 종료 (Exit)
   -  CLI 종료


## 📁 3. 디렉토리 구조
```text
python_final_project/
├── models/                     # 데이터 모델 및 클래스 정의 모듈
│   ├── __init__.py
│   ├── base_book.py
│   └── specialized_books.py
├── utils/                      # 보조 함수 및 유틸리티 모듈
│   ├── __init__.py
│   └── helpers.py
├── main.py                     # CLI 진입점 및 메뉴 제어 흐름
├── pyproject.toml              # 프로젝트 메타데이터 및 설정 파일
├── uv.lock                     # 의존성 고정 Lock 파일
└── README.md                   # 프로젝트 설명 문서
```


## 실행
<img width="563" height="158" alt="image" src="https://github.com/user-attachments/assets/a1a54570-a788-4124-8032-9fda44965f3d" />
## 도서 등록 & 전체 도서 조회
<img width="475" height="299" alt="image" src="https://github.com/user-attachments/assets/e07cd46a-a4e4-46a6-a6e1-543fa85508a4" />

## 도서 검색
<img width="472" height="187" alt="image" src="https://github.com/user-attachments/assets/cd318de2-f6ba-4ba0-8f69-be17fc6ea581" />
## 도서 대여/반납
<img width="209" height="442" alt="image" src="https://github.com/user-attachments/assets/d1a0b01e-8fe2-47e3-ad30-b7c408b8adf6" />
## 프로그램 종료
<img width="494" height="169" alt="image" src="https://github.com/user-attachments/assets/1bdc8dc3-4692-4ded-bc39-64ca76f6773f" />




