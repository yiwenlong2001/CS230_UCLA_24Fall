grammar cfg22;
s : s1;
s1 : 'a' s3;
s3 : 'b' s6;
s6 : 'c' | 'd';

WS : [ \t\r\n]+ -> skip ;