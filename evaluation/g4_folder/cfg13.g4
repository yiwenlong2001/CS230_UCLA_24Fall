grammar cfg13;
s : s1;
s1 : 'c' s2;
s2 :   | 'c' s3;
s3 :   | 'c' s4;
s4 :  ;

WS : [ \t\r\n]+ -> skip ;