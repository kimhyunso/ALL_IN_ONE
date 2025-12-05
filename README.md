# ALL_IN_ONE

## 리스트 종류

1. Static array
2. Dynamic array - 코딩테스트에서 주로 사용됨

|                 | Static array | Dynamic array    |
| --------------- | ------------ | ---------------- |
| access / update | $O(1)$       | $O(1)$           |
| insert_back     | $O(1)$       | amortized $O(1)$ |
| delete_back     | $O(1)$       | $O(1)$           |
| insert_at       | $O(n)$       | $O(n)$           |
| delete_at       | $O(n)$       | $O(n)$           |

## 연결리스트 종류

1. single linked list
2. doubly linked list

|               | Linked list | Array      |
| ------------- | ----------- | ---------- | -------------------- |
| access/update | **$O(n)$**  | **$O(1)$** |
| insert_front  | **$O(1)$**  | **$O(n)$** |
| insert_at     | **$O(n)$**  | $O(n)$     |
| insert_back   | \*\*$O(n)$  | $O(1)$\*\* | **$O(1)$** amortized |
| remove_front  | **$O(1)$**  | **$O(n)$** |
| remove_at     | **$O(n)$**  | **$O(n)$** |
| remove_back   | \*\*$O(n)$  | $O(1)$\*\* | **$O(1)$**           |
