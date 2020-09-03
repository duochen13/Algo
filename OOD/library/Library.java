
class Library {



    public static class Book {
        int bookId;
        boolean status;
        Book(int bookId, boolean status) {
            this.bookId = bookId;
            this.status = status;
        }
    }

    public static void main(String[] args) {

        Library library = new Library();

        Book book = new Book(123, true);

        System.out.print("library");
    }

}