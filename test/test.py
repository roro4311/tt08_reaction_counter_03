import cocotb
from cocotb.regression import TestFactory
from cocotb.regression import Simulation
from cocotb.result import TestFailure
from cocotb.regression import TestResult
import random

@cocotb.coroutine
def tt_um_tb(dut):
    # Reset the design
    dut.rst_n <= 0
    dut.clk <= 0
    dut.ui_in <= 0
    dut.ena <= 0
    yield cocotb.clock.Clock(dut.clk, 10, units="ns").start()
    yield cocotb.regression.ClockCycles(dut.clk, 2)
    dut.rst_n <= 1
    yield cocotb.regression.ClockCycles(dut.clk, 2)

    # Test case 1: Basic functionality
    dut.ui_in <= 8'hFF
    dut.ena <= 1
    yield cocotb.regression.ClockCycles(dut.clk, 10)
    
    # Check outputs
    if dut.uo_out.value != 8'hxx:
        raise TestFailure("uo_out did not match expected value")

    if dut.uio_out.value != 8'hxx:
        raise TestFailure("uio_out did not match expected value")

    if dut.uio_oe.value != 8'hxx:
        raise TestFailure("uio_oe did not match expected value")

    # Additional test cases can be added here

# Create TestFactory and add the test coroutine
tf = TestFactory(tt_um_tb)
tf.add_option("-sv")
tf.add_option("-g2012")
tf.generate_tests()
