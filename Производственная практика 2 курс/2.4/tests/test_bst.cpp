#include <gtest/gtest.h>
#include <type_traits>
#include "binary_tree.h"

TEST(BinaryTree_Interface, Signatures) {
  static_assert(std::is_same_v<decltype(&BinaryTree::push), void(BinaryTree::*)(int)>);
  static_assert(std::is_same_v<decltype(&BinaryTree::pop), int(BinaryTree::*)()>);
  static_assert(std::is_same_v<decltype(&BinaryTree::search), bool(BinaryTree::*)(int) const>);
  static_assert(std::is_same_v<decltype(&BinaryTree::empty), bool(BinaryTree::*)() const>);
  static_assert(std::is_same_v<decltype(&BinaryTree::size), std::size_t(BinaryTree::*)() const>);
  SUCCEED();
}

TEST(DISABLED_BinaryTree_Behavior, InsertSearchAndPopMin) {
  BinaryTree t;
  t.push(10);
  t.push(4);
  t.push(15);
  t.push(7);
  EXPECT_TRUE(t.search(7));
  EXPECT_FALSE(t.search(100));
  EXPECT_EQ(t.pop(), 4);  // pop() должен удалять минимальный элемент
  EXPECT_FALSE(t.search(4));
}
