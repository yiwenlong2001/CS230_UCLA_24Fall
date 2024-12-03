grammar cfg15;
s : s1 s2 s8;
s1 : 'a';
s10 : 'c' s11;
s11 : 'c' s11 | EOF;
s2 : 'b' s3;
s3 : 'b' s4;
s4 : 'b' s5 | EOF;
s5 : 'b' s6 | EOF;
s6 : 'b' s7 | EOF;
s7 : EOF;
s8 : 'c' s9;
s9 : 'c' s10;

WS : [ \t\r\n]+ -> skip ;