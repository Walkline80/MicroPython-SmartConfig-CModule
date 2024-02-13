# Create an INTERFACE library for our C module.
add_library(usermod_smartconfig INTERFACE)

# Add our source files to the lib
target_sources(usermod_smartconfig INTERFACE
    ${CMAKE_CURRENT_LIST_DIR}/modsmartconfig.c
)

# Link our INTERFACE library to the usermod target.
target_link_libraries(usermod INTERFACE usermod_smartconfig)
