module spi_driver (
    input wire clk,
    input wire rst_n,
    output reg miso,
    output reg cs,
    output reg [7:0] data_out
);
    // Simple SPI driver for testing
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            miso <= 1'b0;
            cs <= 1'b0;
            data_out <= 8'h00;
        end else begin
            miso <= ~miso;
            cs <= ~cs;
            data_out <= data_out + 1;
        end
    end
endmodule

