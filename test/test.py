import cocotb
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_reaction_timer(dut):
    """Test for the reaction_timer module"""

    # Apply reset
    dut.rst_n.value = 0
    await Timer(10, units='ns')
    dut.rst_n.value = 1
    await Timer(10, units='ns')

    # Ensure initial values
    assert dut.time_out.value == 0, f"Expected 0, got {dut.time_out.value}"

    # Test case 1: LED on and button press
    dut.led_on.value = 1
    await RisingEdge(dut.clk)
    await Timer(10, units='ns')

    for i in range(10):
        await RisingEdge(dut.clk)

    dut.button.value = 1
    await RisingEdge(dut.clk)
    await Timer(10, units='ns')
    dut.button.value = 0

    # Check the time_out value
    expected_value = 10  # Adjust this based on your test case
    assert dut.time_out.value == expected_value, f"Expected {expected_value}, got {dut.time_out.value}"

    # Test case 2: LED on and off without button press
    dut.led_on.value = 1
    await RisingEdge(dut.clk)
    await Timer(10, units='ns')

    for i in range(5):
        await RisingEdge(dut.clk)

    dut.led_on.value = 0
    await RisingEdge(dut.clk)
    await Timer(10, units='ns')

    # Check the time_out value
    expected_value = 5  # Adjust this based on your test case
    assert dut.time_out.value == expected_value, f"Expected {expected_value}, got {dut.time_out.value}"

@cocotb.test()
async def test_tt_um_reaction_timer(dut):
    """Test for the tt_um_reaction_timer module"""

    # Apply reset
    dut.rst_n.value = 0
    await Timer(10, units='ns')
    dut.rst_n.value = 1
    await Timer(10, units='ns')

    # Set ui_in and enable
    dut.ui_in.value = 0xAA
    dut.ena.value = 1
    await Timer(10, units='ns')
    dut.ena.value = 0
    await Timer(10, units='ns')

    # Add more stimulus and checks as needed
    # ...

