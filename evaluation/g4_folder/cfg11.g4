grammar cfg11;
s : s1;
s1 : 'a' s2;
s2 : 'a' s3;
s3 : 'a';

WS : [ \t\r\n]+ -> skip ;