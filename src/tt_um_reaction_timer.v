module tt_um_reaction_timer (
    input wire clk,
    input wire rst_n,
    input wire [7:0] ui_in,
    output wire [7:0] uo_out,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input wire ena
);

    wire miso, cs;
    wire [7:0] data_out;

    spi_driver spi_inst (
        .clk(clk),
        .rst_n(rst_n),
        .miso(miso),
        .cs(cs),
        .data_out(data_out)
    );

    // Debugging
    initial begin
        $monitor("At time %t, ui_in = %h, miso = %b, cs = %b, data_out = %h", $time, ui_in, miso, cs, data_out);
    end

    // Additional logic goes here

endmodule

