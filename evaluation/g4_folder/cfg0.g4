grammar cfg0;
s : s1 s3;
s1 : 'a' | 'b';
s3 :   | 'c' s3;

WS : [ \t\r\n]+ -> skip ;