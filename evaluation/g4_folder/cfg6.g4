grammar cfg6;
s : s1;
s1 : 'a' | 'a' s1;

WS : [ \t\r\n]+ -> skip ;