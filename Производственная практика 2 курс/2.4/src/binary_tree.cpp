#include "binary_tree.h"
void BinaryTree::push(int) { throw std::logic_error("Not implemented"); }
int BinaryTree::pop() { throw std::logic_error("Not implemented"); }
bool BinaryTree::search(int) const noexcept { return false; }
bool BinaryTree::empty() const noexcept { return true; }
std::size_t BinaryTree::size() const noexcept { return 0; }
