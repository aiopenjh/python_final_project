from models.base_book import Book

class EBook(Book):
    # 추가 변수 없이 부모 __init__만 그대로 사용
    def __init__(self, title, author, isbn, file_size):
        super().__init__(title, author, isbn)
        self.file_size = file_size

    # 출력 형태 전자책에 맞게 오버라이딩
    def get_info(self):
        status = "대여중" if self.is_borrowed() else "대여 가능"
        return f"[전자도서] 제목: {self.title} | 저자: {self.author} | ISBN: {self.isbn} | 상태: {status} | 사이즈: {self.file_size}"


class PaperBook(Book):
    def __init__(self, title, author, isbn, file_size):
        super().__init__(title, author, isbn)
        self.file_size = file_size

    # 출력 형태만 단행본에 맞게 오버라이딩
    def get_info(self):
        status = "대여중" if self.is_borrowed() else "대여 가능"
        return f"[단행본] 제목: {self.title} | 저자: {self.author} | ISBN: {self.isbn} | 상태: {status} | 사이즈: {file_size}"