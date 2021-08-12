cmake_minimum_required(VERSION 3.0)

project(hello_window)

find_package(glad)
find_package(glfw3)

add_executable(hello_window
    hello_window.cpp
    )

target_link_libraries(hello_window
    glad::glad
    glfw::glfw
    )
