grammar cfg18;
s : 'a' s3 'd';
s1 : 'b' | 'c';
s3 : s1 | s1 s3;

WS : [ \t\r\n]+ -> skip ;