from conans import ConanFile, CMake, tools


class taskflowConan(ConanFile):
    name = "taskflow"
    version = "2.2.0"
    license = "MIT"
    author = "Edgar Edgar@AnotherFoxGuy.com"
    url = "https://github.com/AnotherFoxGuy/conan-taskflow"
    description = "A fast C++ header-only library to help you quickly write parallel programs with complex task dependencies"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def source(self):
        git = tools.Git()
        git.clone("https://github.com/cpp-taskflow/cpp-taskflow.git", "v2.2.0")

    def build(self):
        cmake = CMake(self)
        cmake.definitions['TF_BUILD_EXAMPLES'] = 'OFF'
        cmake.definitions['TF_BUILD_TESTS'] = 'OFF'
        cmake.definitions['TF_BUILD_BENCHMARKS'] = 'OFF'
        cmake.configure()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.includedirs = 'include'
        self.cpp_info.libs = tools.collect_libs(self)
