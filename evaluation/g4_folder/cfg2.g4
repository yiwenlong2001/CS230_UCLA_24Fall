grammar cfg2;
s : s1 'd';
s1 :   | 'a' s1;

WS : [ \t\r\n]+ -> skip ;