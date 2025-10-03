cmake_minimum_required(VERSION 3.16)
project(practice_gtest CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/refs/tags/v1.14.0.zip
)
# Для MSVC
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

add_library(core
  src/queue.cpp
  src/heap.cpp
  src/binary_tree.cpp
)
target_include_directories(core PUBLIC include)

enable_testing()
add_executable(tests
  tests/test_queue.cpp
  tests/test_heap.cpp
  tests/test_bst.cpp
)
target_link_libraries(tests PRIVATE core GTest::gtest_main)
include(GoogleTest)
gtest_discover_tests(tests)
