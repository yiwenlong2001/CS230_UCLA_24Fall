grammar cfg10;
s : s1 s2 s3;
s1 : 'a' s1 | EOF;
s2 : 'b' | 'b' s2;
s3 : 'c' | EOF;

WS : [ \t\r\n]+ -> skip ;