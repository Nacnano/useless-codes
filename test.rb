-8.upto(8){|i|print i%26>0?"# : "[[(i%26-13).abs,(i/8).abs].max%4]*2:$/}