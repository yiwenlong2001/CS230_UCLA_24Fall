grammar cfg12;
s : s1;
s1 : 'b' s2;
s2 : 'b' s3;
s3 :   | 'b' s3;

WS : [ \t\r\n]+ -> skip ;