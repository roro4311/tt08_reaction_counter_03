import cocotb
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_tt_um(dut):
    """Test for the tt_um module"""

    # Apply reset
    dut.rst_n.value = 0
    await Timer(10, units='ns')
    dut.rst_n.value = 1
    await Timer(10, units='ns')

    # Ensure initial values
    assert dut.ui_in.value == 0, f"Expected 0, got {dut.ui_in.value}"
    assert dut.uo_out.value == 0, f"Expected 0, got {dut.uo_out.value}"
    assert dut.uio_out.value == 0, f"Expected 0, got {dut.uio_out.value}"
    assert dut.uio_oe.value == 0b11111111, f"Expected 0b11111111, got {dut.uio_oe.value}"

    # Initialize SPI signals
    spi_mosi_expected = 0
    spi_clk_expected = 0
    spi_cs_expected = 1

    # Apply test stimulus
    dut.ui_in.value = 0xAA  # Example input data
    dut.ena.value = 1
    await RisingEdge(dut.clk)
    await Timer(10, units='ns')

    # Wait for some cycles to allow SPI transmission
    for _ in range(16):  # Adjust the number of cycles based on your clock divider
        await RisingEdge(dut.clk)

    # Check SPI signals
    assert dut.spi_clk.value == spi_clk_expected, f"Expected {spi_clk_expected}, got {dut.spi_clk.value}"
    assert dut.spi_mosi.value == spi_mosi_expected, f"Expected {spi_mosi_expected}, got {dut.spi_mosi.value}"
    assert dut.spi_cs.value == spi_cs_expected, f"Expected {spi_cs_expected}, got {dut.spi_cs.value}"

    # Additional test cases
    dut.ui_in.value = 0x55  # Example different input data
    dut.ena.value = 1
    await RisingEdge(dut.clk)
    await Timer(10, units='ns')

    for _ in range(16):  # Adjust based on clock divider
        await RisingEdge(dut.clk)

    # Check SPI signals again
    spi_mosi_expected = 1  # Expected value after new input is processed
    spi_cs_expected = 1  # Chip select should be high after transmission

    assert dut.spi_clk.value == spi_clk_expected, f"Expected {spi_clk_expected}, got {dut.spi_clk.value}"
    assert dut.spi_mosi.value == spi_mosi_expected, f"Expected {spi_mosi_expected}, got {dut.spi_mosi.value}"
    assert dut.spi_cs.value == spi_cs_expected, f"Expected {spi_cs_expected}, got {dut.spi_cs.value}"
