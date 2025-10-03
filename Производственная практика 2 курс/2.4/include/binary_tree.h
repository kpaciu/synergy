#pragma once
#include <cstddef>
#include <stdexcept>

// Бинарное дерево поиска (BST) для целых чисел.
// Контракт:
//  - push(int): вставка значения.
//  - pop(): удалить и вернуть минимальный элемент; на пустом дереве — std::underflow_error.
//  - search(int): true, если значение присутствует.
//  - empty(): true если дерево пусто.
//  - size(): количество элементов.
class BinaryTree {
public:
  void push(int value);
  int pop();
  bool search(int value) const noexcept;
  bool empty() const noexcept;
  std::size_t size() const noexcept;
};
