class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.__is_borrowed = False

    # 대여 상태를 확인하는 함수
    def is_borrowed(self):
        return self.__is_borrowed

    # 대여 처리 함수
    def borrow(self):
        if self.__is_borrowed:
            return False
        self.__is_borrowed = True
        return True

    # 반납 처리 함수
    def return_book(self):
        if not self.__is_borrowed:
            return False
        self.__is_borrowed = False
        return True

    # 도서 정보 출력 함수
    def get_info(self):
        status = "대여중" if self.__is_borrowed else "대여 가능"
        return f"제목: {self.title} | 저자: {self.author} | ISBN: {self.isbn} | 상태: {status} | 크기: {self.file_size}"
