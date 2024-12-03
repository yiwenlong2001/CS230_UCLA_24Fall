grammar cfg17;
s : 'a' s3 'f';
s1 : 'b' 'c' | 'd' 'e';
s3 :   | s1 s3;

WS : [ \t\r\n]+ -> skip ;