#include <gtest/gtest.h>
#include <type_traits>
#include "queue.h"

TEST(Queue_Interface, Signatures) {
  static_assert(std::is_same_v<decltype(&Queue::push), void(Queue::*)(int)>);
  static_assert(std::is_same_v<decltype(&Queue::pop), int(Queue::*)()>);
  static_assert(std::is_same_v<decltype(&Queue::empty), bool(Queue::*)() const>);
  static_assert(std::is_same_v<decltype(&Queue::size), std::size_t(Queue::*)() const>);
  SUCCEED();
}

TEST(DISABLED_Queue_Behavior, FifoOrder) {
  Queue q;
  q.push(10);
  q.push(20);
  EXPECT_EQ(q.pop(), 10);
  EXPECT_EQ(q.pop(), 20);
  EXPECT_TRUE(q.empty());
}

TEST(DISABLED_Queue_Behavior, PopOnEmptyThrows) {
  Queue q;
  EXPECT_THROW(q.pop(), std::underflow_error);
}
