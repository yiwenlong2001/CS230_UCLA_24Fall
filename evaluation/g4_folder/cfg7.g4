grammar cfg7;
s : s1;
s1 : 'b' | EOF;

WS : [ \t\r\n]+ -> skip ;