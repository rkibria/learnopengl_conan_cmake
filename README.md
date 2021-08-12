# learnopengl_conan_cmake
Build the examples from learnopengl.com with conan package manager and CMake

C++ sources taken from https://learnopengl.com/ created by Joey de Vries https://twitter.com/JoeyDeVriez

All code samples, unless explicitly stated otherwise, are licensed under the terms of the CC BY-NC 4.0 license. You can find a human-readable format of the license here https://creativecommons.org/licenses/by-nc/4.0/ and the full license here https://creativecommons.org/licenses/by-nc/4.0/legalcode

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
