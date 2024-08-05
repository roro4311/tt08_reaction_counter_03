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

    wire [7:0] reaction_time;
    wire spi_clk;
    wire spi_mosi;
    wire spi_miso;
    wire spi_cs;

    // Assuming ui_in[0] is the button and ui_in[1] is the LED indicator
    wire button = ui_in[0];
    wire led_on = ui_in[1];

    // Instantiate the SPI module
    spi_driver spi_inst (
        .clk(clk),
        .rst_n(rst_n),
        .data_in(reaction_time),  // Connect reaction_timer output to SPI input
        .spi_clk(spi_clk),
        .spi_mosi(spi_mosi),
        .spi_miso(spi_miso),
        .spi_cs(spi_cs)
    );

    // Instantiate the Reaction Timer module
    reaction_timer reaction_timer_inst (
        .clk(clk),
        .rst_n(rst_n),
        .button(button),
        .led_on(led_on),
        .time_out(reaction_time)
    );

    // Outputs handling
    assign uo_out = 8'b0;           // Default uo_out to 0
    assign uio_out = (ena) ? reaction_time : 8'b0; // Use reaction_time if enabled
    assign uio_oe = 8'b11111111;    // Example: set all as outputs

    // Debugging
    initial begin
        $monitor("At time %t, ui_in = %h, spi_mosi = %b, spi_miso = %b, spi_clk = %b, spi_cs = %b, reaction_time = %h, uo_out = %h, uio_out = %h, uio_oe = %h", 
                 $time, ui_in, spi_mosi, spi_miso, spi_clk, spi_cs, reaction_time, uo_out, uio_out, uio_oe);
    end

endmodule
