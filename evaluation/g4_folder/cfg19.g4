grammar cfg19;
s : s1 s6;
s1 : 'a' s2;
s2 :   | 'a' s3;
s3 :  ;
s4 : 'b' | 'c';
s6 : s4 s7;
s7 : s4 s8;
s8 : s4;

WS : [ \t\r\n]+ -> skip ;