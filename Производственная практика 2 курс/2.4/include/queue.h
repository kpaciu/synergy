#pragma once
#include <cstddef>
#include <stdexcept>

// Очередь целых чисел (FIFO).
// Контракт:
//  - push(int): добавить элемент в конец очереди.
//  - pop(): удалить и вернуть самый ранний элемент; на пустой очереди — std::underflow_error.
//  - empty(): true если очередь пуста.
//  - size(): текущее количество элементов.
class Queue {
public:
  void push(int value);
  int pop();
  bool empty() const noexcept;
  std::size_t size() const noexcept;
};
