module spi_driver (
    input wire clk,
    input wire rst_n,
    input wire [7:0] data_in, // Input data to be sent via SPI
    output reg spi_clk,        // SPI Clock
    output reg spi_mosi,       // Master Out Slave In
    input wire spi_miso,       // Master In Slave Out (from slave)
    output reg spi_cs          // Chip Select
);

    reg [7:0] shift_reg;       // Shift register for SPI data
    reg [3:0] bit_cnt;         // Bit counter for SPI transmission
    reg [15:0] clk_div;        // Clock divider for SPI clock generation
    localparam DIVIDE_BY = 16; // Divider value for generating SPI clock

    // SPI Clock generation (simple clock divider)
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            clk_div <= 0;
            spi_clk <= 0;
        end else begin
            if (clk_div == DIVIDE_BY - 1) begin
                clk_div <= 0;
                spi_clk <= ~spi_clk;
            end else begin
                clk_div <= clk_div + 1;
            end
        end
    end

    // SPI Data shift and transmission
    always @(posedge spi_clk or negedge rst_n) begin
        if (!rst_n) begin
            spi_mosi <= 0;
            spi_cs <= 1; // Deactivate CS initially
            bit_cnt <= 0;
            shift_reg <= 8'b0;
        end else begin
            if (bit_cnt == 0) begin
                // Load data into shift register on CS activation
                spi_cs <= 0;
                shift_reg <= data_in;
                bit_cnt <= 8;
            end else begin
                // Shift data out
                spi_mosi <= shift_reg[7];
                shift_reg <= shift_reg << 1;
                bit_cnt <= bit_cnt - 1;
                if (bit_cnt == 1) begin
                    spi_cs <= 1; // Deactivate CS when transmission is complete
                end
            end
        end
    end

endmodule
