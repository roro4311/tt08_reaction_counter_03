`timescale 1ns / 1ps
`default_nettype none

module tb;

    reg clk;
    reg rst_n;
    reg [7:0] ui_in;
    reg ena;
    wire [7:0] uo_out;
    wire [7:0] uio_out;
    wire [7:0] uio_oe;

    // Additional signals for reaction_timer
    reg button;
    reg led_on;
    wire [7:0] time_out;

    // Instantiate the tt_um_reaction_timer module
    tt_um_reaction_timer dut (
        .clk(clk),
        .rst_n(rst_n),
        .ui_in(ui_in),
        .uo_out(uo_out),
        .uio_out(uio_out),
        .uio_oe(uio_oe),
        .ena(ena)
    );

    // Instantiate the reaction_timer module
    reaction_timer rt (
        .clk(clk),
        .rst_n(rst_n),
        .button(button),
        .led_on(led_on),
        .time_out(time_out)
    );

    initial begin
        // Initialize inputs
        clk = 0;
        rst_n = 0;
        ui_in = 8'b0;
        ena = 0;
        button = 0;
        led_on = 0;

        // Apply reset
        #10 rst_n = 1;
    end

    always #5 clk = ~clk; // Generate clock signal

endmodule

