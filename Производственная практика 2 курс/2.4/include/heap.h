#pragma once
#include <cstddef>
#include <stdexcept>

// Бинарная куча целых чисел (max-heap).
// Контракт:
//  - push(int): добавить элемент.
//  - pop(): удалить и вернуть наибольший элемент; на пустой куче — std::underflow_error.
//  - empty(): true если куча пуста.
//  - size(): текущее количество элементов.
class Heap {
public:
  void push(int value);
  int pop();
  bool empty() const noexcept;
  std::size_t size() const noexcept;
};
