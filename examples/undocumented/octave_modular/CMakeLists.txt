FILE(GLOB OCTAVE_EXAMPLES RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} *.m)

FOREACH(EXAMPLE ${OCTAVE_EXAMPLES})
	STRING(REGEX REPLACE "(.*).m" "\\1" EXAMPLE_NAME ${EXAMPLE})
	add_test(NAME octave_modular-${EXAMPLE_NAME}
			WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
			COMMAND ${OCTAVE_EXECUTABLE} ${EXAMPLE})
	set_property(TEST octave_modular-${EXAMPLE_NAME} PROPERTY
		ENVIRONMENT "OCTAVE_PATH=${OCTAVE_MODULAR_BINARY_DIR}:${CMAKE_CURRENT_SOURCE_DIR}/tools")
ENDFOREACH()