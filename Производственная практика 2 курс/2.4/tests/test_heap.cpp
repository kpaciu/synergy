#include <gtest/gtest.h>
#include <type_traits>
#include "heap.h"

TEST(Heap_Interface, Signatures) {
  static_assert(std::is_same_v<decltype(&Heap::push), void(Heap::*)(int)>);
  static_assert(std::is_same_v<decltype(&Heap::pop), int(Heap::*)()>);
  static_assert(std::is_same_v<decltype(&Heap::empty), bool(Heap::*)() const>);
  static_assert(std::is_same_v<decltype(&Heap::size), std::size_t(Heap::*)() const>);
  SUCCEED();
}

TEST(DISABLED_Heap_Behavior, PopReturnsMax) {
  Heap h;
  h.push(5);
  h.push(42);
  h.push(7);
  EXPECT_EQ(h.pop(), 42);
  EXPECT_EQ(h.pop(), 7);
  EXPECT_EQ(h.pop(), 5);
  EXPECT_TRUE(h.empty());
}

TEST(DISABLED_Heap_Behavior, PopOnEmptyThrows) {
  Heap h;
  EXPECT_THROW(h.pop(), std::underflow_error);
}
