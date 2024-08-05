module tt_um_reaction_timer (
    input wire clk,
    input wire rst_n,
    input wire [7:0] ui_in,
    output wire [7:0] uo_out,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input wire [7:0] uio_in,
    input wire ena
);

    wire miso, cs;
    wire [7:0] data_out;
    wire button = ui_in[0];     // Assuming ui_in[0] is the button input
    wire led_on = ui_in[1];     // Assuming ui_in[1] is the LED indicator
    wire [7:0] reaction_time;
    wire spi_clk;
    wire spi_mosi;
    wire spi_miso;
    wire spi_cs;

   // Instantiate the spi_driver module
    spi spi_inst (
        .clk(clk),
        .rst_n(rst_n),
        .data_in(time_out), // Connect reaction_timer output to spi input
        .spi_clk(spi_clk),
        .spi_mosi(spi_mosi),
        .spi_miso(spi_miso),
        .spi_cs(spi_cs)
    );

    // Instantiate the reaction_timer module
    reaction_timer reaction_timer_inst (
        .clk(clk),
        .rst_n(rst_n),
        .button(button),
        .led_on(led_on),
        .time_out(reaction_time)
    );

    // Logic to handle outputs
    assign uo_out = 8'b0;           // Default uo_out to 0
    assign uio_out = (ena) ? data_out : 8'b0;
    assign uio_oe = 8'b11111111;    // Example: set all as outputs

    // Debugging
    initial begin
        $monitor("At time %t, ui_in = %h, miso = %b, cs = %b, data_out = %h, uo_out = %h, uio_out = %h, uio_oe = %h", $time, ui_in, miso, cs, data_out, uo_out, uio_out, uio_oe);
    end

    // Additional logic goes here

endmodule
