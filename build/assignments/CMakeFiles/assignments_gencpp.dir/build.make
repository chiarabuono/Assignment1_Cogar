# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/abulanti/assign/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/abulanti/assign/build

# Utility rule file for assignments_gencpp.

# Include the progress variables for this target.
include assignments/CMakeFiles/assignments_gencpp.dir/progress.make

assignments_gencpp: assignments/CMakeFiles/assignments_gencpp.dir/build.make

.PHONY : assignments_gencpp

# Rule to build all files generated by this target.
assignments/CMakeFiles/assignments_gencpp.dir/build: assignments_gencpp

.PHONY : assignments/CMakeFiles/assignments_gencpp.dir/build

assignments/CMakeFiles/assignments_gencpp.dir/clean:
	cd /home/abulanti/assign/build/assignments && $(CMAKE_COMMAND) -P CMakeFiles/assignments_gencpp.dir/cmake_clean.cmake
.PHONY : assignments/CMakeFiles/assignments_gencpp.dir/clean

assignments/CMakeFiles/assignments_gencpp.dir/depend:
	cd /home/abulanti/assign/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/abulanti/assign/src /home/abulanti/assign/src/assignments /home/abulanti/assign/build /home/abulanti/assign/build/assignments /home/abulanti/assign/build/assignments/CMakeFiles/assignments_gencpp.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : assignments/CMakeFiles/assignments_gencpp.dir/depend

