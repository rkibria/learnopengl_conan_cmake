# learnopengl_conan_cmake
Build the examples from learnopengl.com with conan package manager and CMake

## Step by step instructions
- Install conan from https://conan.io/downloads.html
- Install CMake https://cmake.org/download/
- Install https://ninja-build.org/
- Open a terminal with conan, CMake, ninja and the C++ compiler in path
- cd to checkout directory
- Install/build (append `--build=glad` and/or `--build=glfw` to first command if conan finds no prebuilt binaries for your configuration)
```
conan install -if bld_01_hello_window 01_hello_window
conan build -if bld_01_hello_window -bf bld_01_hello_window 01_hello_window
```
- Run hello_window executable in bld_01_hello_window
