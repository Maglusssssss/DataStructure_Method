package hus.oop.basicstatistics;

public class MyLinkedList extends MyAbstractList {
    private MyLinkedListNode head;

    /**
     * Khởi tạo dữ liệu mặc định.
     */
    public MyLinkedList() {
        /* TODO */
    }

    /**
     * Lấy kích thước của list.
     * @return
     */
    @Override
    public int size() {
        /* TODO */
    }

    /**
     * Lấy phần tử ở vị trí index trong list.
     * @param index
     * @return
     */
    @Override
    public Object get(int index) {
        /* TODO */
    }

    /**
     * Xóa phần tử của list ở vị trí index.
     * @param index
     */
    @Override
    public void remove(int index) {
        /* TODO */
    }

    /**
     * Thêm vào cuối list phần tử có dữ liệu payload.
     * @param payload
     */
    @Override
    public void append(Object payload) {
        /* TODO */
    }

    /**
     * Thêm vào list phần tử có dữ liệu payload ở vị trí index.
     * @param payload
     * @param index
     */
    @Override
    public void insert(Object payload, int index) {
        /* TODO */
    }

    /**
     * Tạo iterator để cho phép duyệt qua các phần tử của list.
     * @return
     */
    @Override
    public MyIterator iterator() {
        /* TODO */
    }

    /**
     * Lấy node ở vị trí index.
     * @param index
     * @return
     */
    private MyLinkedListNode getNodeByIndex(int index) {
        /* TODO */
    }

    private class MyLinkedListIterator implements MyIterator {
        /*
         * MyLinkedListIterator cần phải tham chiếu đến node hiện tại của MyLinkedList để có thể duyệt qua
           các phần tử còn lại trong MyLinkedList.
        */
        private MyLinkedListNode currentNode;

        /**
         * Khởi tạo dữ liệu cho Iterator là node hiện tại trong MyLinkedList.
         * @param node
         */
        public MyLinkedListIterator(MyLinkedListNode node) {
            /* TODO */
        }

        /**
         * Kiểm tra trong MyLinkedList có còn phần tử tiếp theo không.
         * Nếu còn thì trả về true, nếu không còn thì trả về false.
         * @return
         */
        @Override
        public boolean hasNext() {
            /* TODO */
        }

        /**
         * iterator dịch chuyển sang phần tử kế tiếp của MyLinkedList và trả ra dữ liệu (payload) của phần tử hiện tại của MyLinkedList.
         * @return payload của phần tử hiện tại.
         */
        @Override
        public Object next() {
            /* TODO */
        }

        @Override
        public void remove() {
            /* TODO */
        }
    }
}
