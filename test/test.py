import cocotb
from cocotb.regression import TestFactory
from cocotb.regression import TestFactory
from cocotb.regression import TestFactory
from cocotb.regression import TestFactory

@cocotb.coroutine
async def test_spi_driver(dut):
    # Reset the DUT
    dut.rst_n <= 0
    dut.data_in <= 0xAA  # Example data to be sent
    await cocotb.start_soon(cocotb.regression.RunConcurrent(dut))

    # Apply reset
    await cocotb.delays.Timer(10, units='ns')
    dut.rst_n <= 1
    await cocotb.delays.Timer(10, units='ns')

    # Test 1: Check SPI Clock and Data Transmission
    # Wait for a few clock cycles
    await cocotb.delays.Timer(100, units='ns')

    # Check signals
    assert dut.spi_mosi == 1  # Example check: assert SPI MOSI is high
    assert dut.spi_cs == 1    # Example check: assert SPI CS is high

    # More tests can be added to verify the SPI behavior

# Create a TestFactory
factory = TestFactory(test_spi_driver)

# Run the testbench
if __name__ == "__main__":
    factory.generate_tests()
