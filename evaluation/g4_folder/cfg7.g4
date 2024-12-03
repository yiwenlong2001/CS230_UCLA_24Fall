grammar cfg7;
s : s1;
s1 :   | 'b';

WS : [ \t\r\n]+ -> skip ;