cmake_minimum_required(VERSION 3.0)

project(hello_triangle)

find_package(glad)
find_package(glfw3)

add_executable(hello_triangle
    hello_triangle.cpp
    )

target_link_libraries(hello_triangle
    glad::glad
    glfw::glfw
    )
