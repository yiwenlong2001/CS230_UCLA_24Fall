grammar cfg21;
s : s3;
s1 : 'a' 'b' | 'c' 'd';
s3 : s1 s4;
s4 : s1 s5;
s5 :   | s1 s5;

WS : [ \t\r\n]+ -> skip ;