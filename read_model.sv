//测试模块   test123123123
module  test (
	input           clk,
	input           rst_n,
	input           enable,
	
	   
	input           wr_req,
   input  [7:0]    gray_data_in,
   input  [14:0]   gray_data_addra,
//	input           vs,
//	input           cv_de,

	
	//Image data has been processd
//   output        pos1	
	output  reg [9:0]   object1,
	output  reg [9:0]   object2,
	output  reg [9:0]   object3,
	output  reg [9:0]   object4,
	output  reg [9:0]   object5 
	
);
begin
	wr_req = 0 ;
	gray_data_in =0 ;
	gray_data_addra = 0 ;
end
//这里是实现相应的测试功能

endmodule

//实现数据读取
module read_rom(
	input clk,
	input rst_n,
	input rom_enable,
	input [7:0] gray_image_in,
	input [14:0] gray_addr_in,
	output reg [9:0] data
	)

//这个是一个ram是预先设定的ram，其参数是需要在开始设定的
gray_ram gray_ram_m0
(
      .clka     (clk),
      .addra    (gray_data_addra),
      .dina     (gray_data_in),
      .wea      (wr_req & (~enable)),
      .ena      (wr_req & (~enable)),
      .addrb    (gray_addra1),
      .clkb     (clk),
      .enb      (1),
      .doutb    (gray1)
 );
//窗口数据存储RAM
gray_1024bit gray_1024bit_m0
(
      .clka     (clk),
      .addra    (gray_in_addra),
      .dina     (gray1),
      .wea      (cut_en),
      .ena      (cut_en),
      .addrb    (gray_addra),
      .clkb     (clk),
      .enb      (1),
      .doutb    (gray));
}
//这个是实现对数据的读取，而且一帧数据的读取
always@(posedge clk or negedge rst_n)
begin
	if(!rst_n)
		cut_cnt <= 11'd0;
		cal_en  <= 1'd0;//表示开关信号，表示是否可以进行数据的读取
	else if ((enable)&(~cal_en))
		begin
			if(cut_cnt < 1025) 
				begin
					cut_cnt = cal_cnt + 1;
				end
			else
				begin//这里表示数据读取完毕，完成了一帧数据的读取
					cal_en = 1;
					cut_cnt = 0 ;
				end

		end
	else
		cut_cnt <= 0;
end

//行触发信号的实现
always@(posedge clk or negedge rst_n)
begin
	if(!rst_n /*| (~start)*/)
		begin
			line_cnt <= 5'd0;
		end
	else
	  if((col_cnt==26) & (addr_cnt == 1023))
			begin
				line_cnt <= line_cnt + 1;
		end
	  else
			begin
				line_cnt <= 5'd0;
			end
end




module map_conv(
   input           clk,
	input           rst_n,
	input           enable,
	
	
	input           wr_req,
   input  [7:0]    gray_data_in,
   input  [14:0]   gray_data_addra,
//	input           vs,
//	input           cv_de,

	
	//Image data has been processd
//   output        pos1	
	output  reg [9:0]   object1,
	output  reg [9:0]   object2,
	output  reg [9:0]   object3,
	output  reg [9:0]   object4,
	output  reg [9:0]   object5 
    );	 
/////////////////////////////////////////////////////////////////////////////////////
reg cstate;//当前状态
reg nstate;//下一状态

reg test_en;
reg test_en2;
   //wangyu test
reg cal_en;//一幅32*32计算使能 1表示计算中 待修改
reg cut_en;//32*32切割使能 1表示切割中

reg [14:0]gray_addra1;//240*130数据读出地址
wire [7:0]gray1;
gray_ram gray_ram_m0
(
      .clka     (clk),
      .addra    (gray_data_addra),
      .dina     (gray_data_in),
      .wea      (wr_req & (~enable)),
      .ena      (wr_req & (~enable)),
      .addrb    (gray_addra1),
      .clkb     (clk),
      .enb      (1),
      .doutb    (gray1)
 );

////////////////////////////Cut部分/////////////////////////////

reg[10:0] cut_cnt;//cut持续时间计数
always@(posedge clk or negedge rst_n)
begin
	if(!rst_n)
		cut_cnt <= 11'd0;
	else if ((enable)&(~cal_en))
		begin
		cut_cnt <= (cut_cnt < 1025) ? cut_cnt + 1 : 0;
		end
	else
		cut_cnt <= 0;
end


always@(posedge clk or negedge rst_n)
begin
	if(!rst_n)
		cut_en <= 1'd0;
	else if((enable)&(~cal_en)&(cut_cnt))
		cut_en <= 1'd1;
	else
		cut_en <= 1'd0;
end

//**********32*32窗口读取基地址计算部分***********
reg [9:0]addr_cnt;
reg [4:0]line_cnt,col_cnt;
//窗口像素读取计数，32*32窗口共1024个像素，对其进行计数
always@(posedge clk or negedge rst_n)
begin
	if(!rst_n)
		addr_cnt <= 10'd0;
	else
	  if(cut_en)
		addr_cnt <= addr_cnt + 1;
	  else
	   addr_cnt <= 10'd0;
end



always@(posedge clk or negedge rst_n)
begin
	if(!rst_n /*| (~start)*/) 
		begin 
			col_cnt <= 5'd0;
		end
	else
	  if(col_cnt < 27)
			begin
				col_cnt <= (addr_cnt == 1023) ? col_cnt + 1 : col_cnt;
			end
	  else
			begin
			col_cnt <= 5'd0;
			end
end

always@(posedge clk or negedge rst_n)
begin
	if(!rst_n /*| (~start)*/)
		begin
			line_cnt <= 5'd0;
		end
	else
	  if((col_cnt==26) & (addr_cnt == 1023))
			begin
				line_cnt <= line_cnt + 1;
		end
	  else
			begin
				line_cnt <= 5'd0;
			end
end



reg [14:0] base_addr;//base_addr为输入图像当前窗口起始地址
always@(posedge clk or negedge rst_n)
begin
	if(!rst_n)
		base_addr <= 15'd0;
	else
	  if(cut_cnt == 1)
		base_addr <= {line_cnt,3'b000}*240 + {col_cnt,3'b000};
	  else
	   base_addr <= base_addr;
end   //wangyu test
//gray_addra1为窗口当前像素读取地址
always@(posedge clk or negedge rst_n)
begin
	if(!rst_n)
		gray_addra1 <= 15'd0;
	else
	   gray_addra1 <= base_addr + 240*addr_cnt[9:5] + addr_cnt[4:0];
end
wire [9:0] gray_addra;
wire [7:0] gray;
assign gray_addra = ((cut_cnt > 1) && (cut_cnt < 1025)) ? cut_cnt - 2 : 0 ;//窗口数据读取地址


//////////////////////////////////////////////////////////////////
endmodule