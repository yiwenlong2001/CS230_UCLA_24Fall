grammar cfg14;
s : s2;
s1 : 'a' 'b';
s2 : s1 s3;
s3 : s1 s4;
s4 :   | s1 s5;
s5 :   | s1 s6;
s6 :  ;

WS : [ \t\r\n]+ -> skip ;