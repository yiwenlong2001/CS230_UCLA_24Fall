grammar cfg5;
s : s4;
s1 : 'a' s3;
s3 : 'b' | 'c';
s4 :   | s1 s4;

WS : [ \t\r\n]+ -> skip ;