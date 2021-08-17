from conans import ConanFile, tools, CMake

class LearnOpenGLHelloTriangleConan(ConanFile):
    name = "LearnOpenGLHelloTriangle"
    version = "0.1"
    requires = "glfw/3.3.4", "glad/0.1.34"
    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake_find_package"
    url = "https://learnopengl.com/Getting-started/Hello-Triangle"

    def build(self):
        cmake = CMake(self, generator="Ninja")
        cmake.configure()
        cmake.build()
