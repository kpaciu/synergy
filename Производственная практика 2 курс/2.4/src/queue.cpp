#include "queue.h"
void Queue::push(int) { throw std::logic_error("Not implemented"); }
int Queue::pop() { throw std::logic_error("Not implemented"); }
bool Queue::empty() const noexcept { return true; }
std::size_t Queue::size() const noexcept { return 0; }
