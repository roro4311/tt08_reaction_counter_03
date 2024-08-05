import cocotb
from cocotb.regression import TestFactory
from cocotb.result import TestFailure

@cocotb.coroutine
def tt_um_reaction_timer_tb(dut):
    # Reset the design
    dut.rst_n <= 0
    await cocotb.delays.Timer(10, units='ns')
    dut.rst_n <= 1
    await cocotb.delays.Timer(10, units='ns')

    # Enable the design
    dut.ena <= 1

    # Apply test vectors
    dut.ui_in <= 0b00000001  # Button pressed
    await cocotb.delays.Timer(10, units='ns')
    assert dut.uio_out == expected_value_for_button_pressed, "Test failed for button press"

    dut.ui_in <= 0b00000010  # LED turned on
    await cocotb.delays.Timer(10, units='ns')
    assert dut.uio_out == expected_value_for_led_on, "Test failed for LED turned on"

    dut.ui_in <= 0b00000000  # Reset button and LED
    await cocotb.delays.Timer(50, units='ns')
    assert dut.uio_out == expected_value_for_reset, "Test failed for button and LED reset"

    print("All tests passed")

# Run the test
tf = TestFactory(tt_um_reaction_timer_tb)
tf.add_option("-sv")  # Specify SystemVerilog if needed
tf.generate_tests()
