grammar cfg8;
s : s2;
s1 : 'a' 'b';
s2 : s1 | s1 s2;

WS : [ \t\r\n]+ -> skip ;